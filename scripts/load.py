import os
from sqlalchemy import create_engine
from transform import transform


def load():
    try:
        print("Starting Load...")

        # 🔹 ensure database path (parent folder)
        db_path = "../ecommerce.db"

        # 🔹 run transform
        df = transform()

        # 🔹 create DB connection
        engine = create_engine(f"sqlite:///{db_path}")

        # 🔹 load data
        df.to_sql("orders_data", engine, if_exists="replace", index=False)

        print("Data Loaded Successfully ✅")

    except Exception as e:
        print("Error in Load:", e)


if __name__ == "__main__":
    load()