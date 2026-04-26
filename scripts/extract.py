import pandas as pd

def extract():
    print("Extracting Data...")

    orders = pd.read_csv("../data/raw/olist_orders_dataset.csv")
    customers = pd.read_csv("../data/raw/olist_customers_dataset.csv")

    print("Data Extracted Successfully")

    return orders, customers