""" Script to load data processed folder in csv
"""
import argparse
import logging
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pathlib import Path


columns = ["id", "text", "greetings", "goodbye_prompt", "change_nib_or_iban", "request_time_off",
           "request_office_table_office", "request_parking_lot", "nothing_related"]


def main(csv_path):
    """Runs the data processing pipeline."""
    logging.info("Loading data from csv file")
    df = pd.read_csv(csv_path)
    logging.info("Data loaded successfully")

    logging.info("Analysing data")
    print(df.head().to_string(max_rows=None))
    print("================== Shape =======================")
    print(df.shape, "\n")
    print("=================== Columns ======================")
    print(df.columns, "\n")
    print("==================== Info =====================")
    print(df.info(), "\n")
    print("=================== Describe ======================")
    print(df.describe(), "\n")
    print("================== Intention Value Counts =======================")
    for intention in columns[2:]:
        print(f"Intention: {intention}")
        print(df[intention].value_counts(), "\n")
    print("=================== Intention Percentage ======================")
    for intention in columns[2:]:
        print(f"Intention: {intention}")
        print(df[intention].value_counts(normalize=True), "\n")
    print("================== Most Frequent Intention =======================")
    print(df[columns[2:]].sum().idxmax())
    print("==================  Class Imbalance =======================")
    for intention in columns[2:]:
        print(f"Intention: {intention} -- {df[intention].value_counts()[True]} \n")
    print("================== Missing Values =======================")
    print(df.isnull().sum())  # Count of missing values in each column
    print("================== Numerical Columns Distribution =======================")
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    for column in numeric_columns:
        plt.figure()
        df[column].plot(kind="hist")
        plt.title(column)
        plt.show()
    print("================== Categorical Columns Distribution =======================")
    categorical_columns = df.select_dtypes(exclude=[np.number]).columns
    for column in categorical_columns:
        plt.figure()
        df[column].value_counts().plot(kind="bar")
        plt.title(column)
        plt.show()
    print("================== Cross-tabulation =======================")
    for col1 in columns[2:]:
        for col2 in columns[2:]:
            if col1 != col2:
                cross_tab = pd.crosstab(df[col1], df[col2])
                print(f"Cross-tabulation: {col1} vs {col2}")
                print(cross_tab)
                print("\n")
    print("================== Random Samples =======================")
    print(df.sample(5).to_string(max_rows=None))
    logging.info("Finished analysing data")


if __name__ == "__main__":
    log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    logging = logging.getLogger(__name__)

    parser = argparse.ArgumentParser(description="Data Processing Script")
    parser.add_argument("--csv-path", type=str, default="../../data/processed/data.csv",
                        help="Path to raw data folder")
    args = parser.parse_args()

    main(Path(args.csv_path))
