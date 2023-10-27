""" This script is used to prepare the data for training the model.
    It splits the data into train, test and validation sets.
    --data "../../../data/processed/data.csv" --test_size 0.10 --val_size 0.10
"""
import os
import argparse
import logging
import pandas as pd
from datasets import load_dataset
from sklearn.model_selection import train_test_split
from transformers import AutoTokenizer
import numpy as np
import mlflow
import pickle

# Define all paths as constants
TRAIN_DATA_PATH = "train_data"
TEST_DATA_PATH = "test_data"
VAL_DATA_PATH = "val_data"

# Define max length for tokenization
MAX_LENGTH = 128


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=str, help="path to input data")
    parser.add_argument("--test_size", type=float, required=False, default=0.2)
    parser.add_argument("--val_size", type=float, required=False, default=0.2)
    parser.add_argument("--tokenizer", type=str, required=False, default="bert-base-uncased")
    parser.add_argument("--encoded_dataset", type=str, required=False)
    parser.add_argument("--labels", type=str, required=False)
    parser.add_argument("--labels2id", type=str, required=False)
    parser.add_argument("--id2label", type=str, required=False)
    return parser.parse_args()


def create_dirs(*dir_paths):
    """Create necessary directories."""
    for dir_path in dir_paths:
        os.makedirs(dir_path, exist_ok=True)


def load_and_split_data(filepath, test_size, val_size):
    """Load data from csv file and split into train, test, and validation."""
    df = pd.read_csv(filepath)

    train_val_df, test_df = train_test_split(df, test_size=test_size)
    train_df, val_df = train_test_split(train_val_df, test_size=val_size / (1 - test_size))

    return train_df, test_df, val_df


def save_datasets(datasets, *filepaths):
    """Save pandas DataFrames to csv files."""
    for dataset, filepath in zip(datasets, filepaths):
        dataset.to_csv(filepath, index=False)


def load_datasets(*filepaths):
    """Load datasets using the `datasets` library."""
    dataset_files = {name: path for name, path in zip(['train', 'test', 'validation'], filepaths)}
    return load_dataset("csv", data_files=dataset_files)


def preprocess_data(dataset, tokenizer, labels):
    """Preprocess the data for training."""
    def preprocess_batch(examples):
        text = examples["text"]
        encoding = tokenizer(text, padding="max_length", truncation=True, max_length=MAX_LENGTH)

        labels_batch = {k: examples[k] for k in examples.keys() if k in labels}
        labels_matrix = np.zeros((len(text), len(labels)))
        for idx, label in enumerate(labels):
            labels_matrix[:, idx] = labels_batch[label]

        encoding["labels"] = labels_matrix.tolist()
        return encoding

    return dataset.map(preprocess_batch, batched=True, remove_columns=dataset['train'].column_names)


def save_pickle(obj, filepath):
    """Save object to a pickle file."""
    with open(filepath, "wb") as file:
        pickle.dump(obj, file)


def main():
    """Main function of the script."""
    args = parse_args()

    create_dirs(TRAIN_DATA_PATH, TEST_DATA_PATH, VAL_DATA_PATH)

    logging.info("Starting data preparation")

    # Start Logging
    mlflow.start_run()

    train_df, test_df, val_df = load_and_split_data(args.data, args.test_size, args.val_size)

    mlflow.log_metric("num_samples", train_df.shape[0] + test_df.shape[0] + val_df.shape[0])
    mlflow.log_metric("num_features", train_df.shape[1] - 1)

    save_datasets([train_df, test_df, val_df],
                  os.path.join(TRAIN_DATA_PATH, "data.csv"),
                  os.path.join(TEST_DATA_PATH, "data.csv"),
                  os.path.join(VAL_DATA_PATH, "data.csv"))

    dataset = load_datasets(os.path.join(TRAIN_DATA_PATH, "data.csv"),
                            os.path.join(TEST_DATA_PATH, "data.csv"),
                            os.path.join(VAL_DATA_PATH, "data.csv"))

    labels = [label for label in dataset['train'].features.keys() if label not in ['id', 'text']]
    id2label = {idx: label for idx, label in enumerate(labels)}
    label2id = {label: idx for idx, label in enumerate(labels)}

    tokenizer = AutoTokenizer.from_pretrained(args.tokenizer)

    encoded_dataset_dict = preprocess_data(dataset, tokenizer, labels)

    encoded_dataset_dict.set_format("torch")

    encoded_dataset_dict.save_to_disk(os.path.join(args.encoded_dataset, "encoded_dataset"))

    save_pickle(labels, os.path.join(args.labels, 'labels_pickle.pkl'))
    save_pickle(label2id, os.path.join(args.labels2id, 'labels2id_pickle.pkl'))
    save_pickle(id2label, os.path.join(args.id2label, 'id2label_pickle.pkl'))

    mlflow.end_run()
    logging.info("Data preparation completed")


if __name__ == "__main__":
    log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    logging = logging.getLogger(__name__)
    main()
