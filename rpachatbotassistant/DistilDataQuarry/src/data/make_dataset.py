""" Script to read data from raw and save it in processed folder in csv
"""
import argparse
import logging
from pathlib import Path

import pandas as pd

intentions = ["greetings", "goodbye_prompt", "change_nib_or_iban", "request_time_off",
              "request_office_table_office", "request_parking_lot", "nothing_related"]


def read_lines(file_path):
    """Reads lines from a text file and returns a list."""
    with open(file_path, "r") as f:
        lines = f.readlines()
    return [line.strip() for line in lines]


def remove_duplicates(lines):
    """Removes duplicate lines from a list."""
    return list(set(lines))


class DataProcessor:
    def __init__(self, raw_data_path, processed_data_path):
        self.raw_data_path = raw_data_path
        self.processed_data_path = processed_data_path
        self.data = []

    def load_data(self):
        """Loads data from raw text files."""
        logging.debug("Loading data from raw text files")
        files = {
            "goodbye.txt": {"goodbye_prompt": True},
            "greeting.txt": {"greetings": True},
            "NIB.txt": {"change_nib_or_iban": True},
            "parking_lot.txt": {"request_parking_lot": True},
            "rooms.txt": {"request_office_table_office": True},
            "time_off.txt": {"request_time_off": True},
            "nothing_related.txt": {"nothing_related": True}
        }

        all_attributes = {
            "greetings": False,
            "goodbye_prompt": False,
            "change_nib_or_iban": False,
            "request_parking_lot": False,
            "request_office_table_office": False,
            "request_time_off": False,
            "nothing_related": False
        }

        for file_name, attributes in files.items():
            file_path = self.raw_data_path / file_name
            lines = read_lines(file_path)
            lines = remove_duplicates(lines)

            for line in lines:
                entry = {"text": line}
                entry.update(all_attributes)  # Set all attributes to False initially
                entry.update(attributes)  # Update with the specific attributes
                self.data.append(entry)
        logging.debug("Loaded data from raw text files")

    def process_data(self):
        """Processes the loaded data."""
        logging.debug("Processing data.")
        dataframe = pd.DataFrame(self.data)
        dataframe = dataframe.sample(frac=1).reset_index(drop=True)
        dataframe.reset_index(inplace=True)
        dataframe.rename(columns={"index": "id"}, inplace=True)
        dataframe.to_csv(self.processed_data_path / "data.csv", index=False)
        logging.debug("Finished processing data.")
        # return path to processed data
        return self.processed_data_path / "data.csv"

    def run(self):
        """Runs the data processing pipeline."""
        logging.debug("making final data set from raw data.")

        self.load_data()
        self.process_data()

        logging.debug("Finished making final data set from raw data.")
        return self.processed_data_path / "data.csv"


def main(raw_data_path, processed_data_path) -> Path:
    """Runs the data processing pipeline."""
    processor = DataProcessor(Path(raw_data_path), Path(processed_data_path))
    path_processed_data = processor.run()
    return path_processed_data


if __name__ == "__main__":
    log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.DEBUG, format=log_fmt)
    logging = logging.getLogger(__name__)

    parser = argparse.ArgumentParser(description="Data Processing Script")
    parser.add_argument("--raw-data", type=str, default="../../data/raw",
                        help="Path to raw data folder")
    parser.add_argument("--processed-data", type=str, default="../../data/processed",
                        help="Path to the processed data folder")
    args = parser.parse_args()

    main(Path(args.raw_data), Path(args.processed_data))
