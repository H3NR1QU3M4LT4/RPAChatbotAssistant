""" Train the model and log the metrics to the workspace.
    --dataset "../data_prep/encoded_dataset" --labels "../data_prep/labels_pickle"
    --label2id "../data_prep/labels2id_pickle"
    --id2label "../data_prep/id2label_pickle"
"""
import argparse
import os
import mlflow
from datasets import load_from_disk
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from transformers import TrainingArguments, Trainer
from sklearn.metrics import f1_score, roc_auc_score, accuracy_score
from transformers import EvalPrediction
import torch
import numpy as np
from transformers import EarlyStoppingCallback
from transformers import pipeline
import pickle



# enable autologging
mlflow.transformers.autolog()

os.makedirs("./outputs", exist_ok=True)


def select_first_file(path):
    """Selects first file in folder, use under assumption there is only one file in folder
    Args:
        path (str): path to directory or file to choose
    Returns:
        str: full path of selected file
    """
    files = os.listdir(path)
    return os.path.join(path, files[0])


def multi_label_metrics(predictions, labels, threshold=0.5):
    # first, apply sigmoid on predictions which are of shape (batch_size, num_labels)
    sigmoid = torch.nn.Sigmoid()
    probs = sigmoid(torch.Tensor(predictions))
    # next, use threshold to turn them into integer predictions
    y_pred = np.zeros(probs.shape)
    y_pred[np.where(probs >= threshold)] = 1
    # finally, compute metrics
    y_true = labels
    f1_micro_average = f1_score(y_true=y_true, y_pred=y_pred, average="micro")
    roc_auc = roc_auc_score(y_true, y_pred, average="micro")
    accuracy = accuracy_score(y_true, y_pred)
    # return as dictionary
    metrics = {"f1": f1_micro_average,
               "roc_auc": roc_auc,
               "accuracy": accuracy}
    return metrics


def compute_metrics(p: EvalPrediction):
    predictions = p.predictions[0] if isinstance(p.predictions, tuple) else p.predictions
    result = multi_label_metrics(
        predictions=predictions,
        labels=p.label_ids)
    return result


def main():
    """Main function of the script."""
    # Start Logging
    mlflow.start_run()

    # input and output arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", type=str, required=True, help="path to dataset")
    parser.add_argument("--labels", type=str, required=True, help="path to test data")
    parser.add_argument("--labels2id", type=str, required=True, help="path to pickle file with label2id")
    parser.add_argument("--id2label", type=str, required=True, help="path to pickle file with id2label")
    parser.add_argument("--train_batch_size", type=int, required=False, default=16)
    parser.add_argument("--eval_batch_size", type=int, required=False, default=8)
    parser.add_argument("--num_train_epochs", type=int, required=False, default=1)
    parser.add_argument("--learning_rate", type=float, required=False, default=2e-5)
    parser.add_argument("--registered_model_name", type=str, required=False, default="bert-rpa-intentions",
                        help="model name")
    parser.add_argument("--model_name", type=str, required=False, default="bert-base-uncased",
                        help="model name in huggingface")
    parser.add_argument("--model", type=str, required=False, help="model name in huggingface")
    args = parser.parse_args()

    with open(select_first_file(args.labels), "rb") as f:
        labels = pickle.load(f)

    with open(select_first_file(args.labels2id), "rb") as f:
        label2id = pickle.load(f)

    with open(select_first_file(args.id2label), "rb") as f:
        id2label = pickle.load(f)

    dataset = load_from_disk(f"{args.dataset}/encoded_dataset")

    # define model
    tokenizer = AutoTokenizer.from_pretrained(args.model_name)
    model = AutoModelForSequenceClassification.from_pretrained(args.model_name,
                                                               problem_type="multi_label_classification",
                                                               num_labels=len(labels),
                                                               id2label=id2label,
                                                               label2id=label2id)

    # define trainer
    training_arguments = TrainingArguments(
        f"bert-fine-tuned-text-classification-intentions",
        evaluation_strategy="epoch",
        save_strategy="epoch",
        learning_rate=2e-5,
        per_device_train_batch_size=args.train_batch_size,
        per_device_eval_batch_size=args.eval_batch_size,
        num_train_epochs=args.num_train_epochs,
        weight_decay=0.01,
        load_best_model_at_end=True,
        metric_for_best_model="accuracy",
    )

    trainer = Trainer(
        model,
        training_arguments,
        train_dataset=dataset["train"],
        eval_dataset=dataset["validation"],
        tokenizer=tokenizer,
        compute_metrics=compute_metrics,
        callbacks=[EarlyStoppingCallback(early_stopping_patience=5)])

    trainer.train()
    trainer.evaluate()
    trainer.save_model(args.registered_model_name)
    pipe = pipeline(task="text-classification",
                    model=AutoModelForSequenceClassification.from_pretrained(args.registered_model_name),
                    batch_size=1,
                    tokenizer=tokenizer)

    # Registering the model to the workspace
    print("Registering the model via MLFlow")
    mlflow.transformers.log_model(
        transformers_model=pipe,
        registered_model_name=args.registered_model_name,
        artifact_path=args.registered_model_name,
    )

    # Saving the model to a file
    mlflow.transformers.save_model(
        transformers_model=pipe,
        path=os.path.join(args.model, "trained_model"),
    )


    # Stop Logging
    mlflow.end_run()


if __name__ == "__main__":
    main()
