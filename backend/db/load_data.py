import os
import pandas as pd
import psycopg2
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)

cur = conn.cursor()

def load_csv_to_table(file_path, table_name, columns):
    df = pd.read_csv(file_path)
    df = df[columns]  # ensure order
    for _, row in df.iterrows():
        placeholders = ','.join(['%s'] * len(row))
        query = f"INSERT INTO {table_name} ({','.join(columns)}) VALUES ({placeholders})"
        cur.execute(query, tuple(row))
    conn.commit()
    print(f"Inserted into {table_name}")


# Load distribution_centers
load_csv_to_table('data/distribution_centers.csv', 'distribution_centers',
    ['name', 'latitude', 'longitude'])

# Load users
load_csv_to_table('data/users.csv', 'users', [
    'first_name', 'last_name', 'email', 'age', 'gender', 'state',
    'street_address', 'postal_code', 'city', 'country', 'latitude',
    'longitude', 'traffic_source', 'created_at'
])

# Load products
load_csv_to_table('data/products.csv', 'products', [
    'cost', 'category', 'name', 'brand', 'retail_price', 'department',
    'sku', 'distribution_center_id'
])

# Load inventory_items
load_csv_to_table('data/inventory_items.csv', 'inventory_items', [
    'product_id', 'created_at', 'sold_at', 'cost', 'product_category',
    'product_name', 'product_brand', 'product_retail_price',
    'product_department', 'product_sku', 'product_distribution_center_id'
])

# Load orders
load_csv_to_table('data/orders.csv', 'orders', [
    'user_id', 'status', 'gender', 'created_at', 'returned_at',
    'shipped_at', 'delivered_at', 'num_of_item'
])

# Load order_items
load_csv_to_table('data/order_items.csv', 'order_items', [
    'order_id', 'user_id', 'product_id', 'inventory_item_id',
    'status', 'created_at', 'shipped_at', 'delivered_at', 'returned_at'
])

cur.close()
conn.close()
