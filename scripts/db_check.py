import sqlite3
import pandas as pd

conn = sqlite3.connect("../ecommerce.db")

df = pd.read_sql("SELECT * FROM orders_data LIMIT 5;", conn)

print(df)