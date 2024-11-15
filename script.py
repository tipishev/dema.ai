# script.py

from pyspark.sql import SparkSession

# Initialize a Spark session
spark = SparkSession.builder \
    .appName("AWS Glue Minimal Setup") \
    .getOrCreate()

# Paths to the CSV files
orders_path = "orders.csv"
inventory_path = "inventory.csv"

# Load the datasets
orders_df = spark.read.csv(orders_path, header=True, inferSchema=True)
inventory_df = spark.read.csv(inventory_path, header=True, inferSchema=True)

# Show the first 10 rows of each file
print("Orders Data (first 10 rows):")
orders_df.show(10)

print("Inventory Data (first 10 rows):")
inventory_df.show(10)

# Stop the Spark session
spark.stop()
