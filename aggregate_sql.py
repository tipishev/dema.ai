from pyspark.sql import SparkSession

# Initialize a Spark session
spark = SparkSession.builder \
    .appName("SQL Aggregation Query") \
    .getOrCreate()

# Paths to the partitioned Parquet files
orders_parquet_path = "/home/glue_user/workspace/data/orders"
inventory_parquet_path = "/home/glue_user/workspace/data/inventory"

# Load the partitioned orders data and inventory data
orders_df = spark.read.parquet(orders_parquet_path)
inventory_df = spark.read.parquet(inventory_parquet_path)

# Register the DataFrames as temporary views to query with SQL
orders_df.createOrReplaceTempView("orders")
inventory_df.createOrReplaceTempView("inventory")

# SQL query: Total Order Amount and Quantity per Day
daily_orders_summary = spark.sql("""
    SELECT
        date,
        SUM(amount) AS total_amount,
        SUM(quantity) AS total_quantity
    FROM orders
    GROUP BY date
""")

print("Total Order Amount and Quantity per Day:")
daily_orders_summary.show()

# SQL query: Total Inventory Quantity per Category
category_inventory_summary = spark.sql("""
    SELECT
        category,
        SUM(quantity) AS total_inventory_quantity
    FROM inventory
    GROUP BY category
""")

print("Total Inventory Quantity per Category:")
category_inventory_summary.show()

# Stop the Spark session
spark.stop()
