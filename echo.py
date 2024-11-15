from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Echo the input files") \
    .getOrCreate()

orders_path = "orders.csv"
inventory_path = "inventory.csv"

orders_df = spark.read.csv(orders_path, header=True, inferSchema=True)
inventory_df = spark.read.csv(inventory_path, header=True, inferSchema=True)

print("Orders Data (first 10 rows):")
orders_df.show(10)

print("Inventory Data (first 10 rows):")
inventory_df.show(10)

spark.stop()
