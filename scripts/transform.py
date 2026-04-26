import pandas as pd
import os
from extract import extract

def transform():
    print("Starting Transform...")

    # 🔹 extract data
    orders, customers = extract()

    # 🔹 cleaning
    orders = orders.dropna()
    customers = customers.dropna()

    # 🔹 merge datasets
    merged = orders.merge(customers, on="customer_id")

    # 🔹 ensure processed folder exists
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    processed_path = os.path.join(base_dir, "data", "processed")
    os.makedirs(processed_path, exist_ok=True)

    # 🔹 save cleaned data
    file_path = os.path.join(processed_path, "cleaned_data.csv")
    merged.to_csv(file_path, index=False)

    print("Transform Successfully")

    return merged


if __name__ == "__main__":
    transform()