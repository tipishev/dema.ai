from pyspark.sql import SparkSession
from pyspark.sql.functions import sum as spark_sum

# Initialize a Spark session
spark = SparkSession.builder.appName("Aggregation Query").getOrCreate()

# Updated paths to the partitioned Parquet files
orders_parquet_path = "/home/glue_user/workspace/data/orders"
inventory_parquet_path = "/home/glue_user/workspace/data/inventory"

# Load the partitioned orders data
orders_df = spark.read.parquet(orders_parquet_path)

# 1. Calculate total order amount and quantity per day
daily_orders_summary = orders_df.groupBy("date").agg(
    spark_sum("amount").alias("total_amount"),
    spark_sum("quantity").alias("total_quantity"),
)

print("Total Order Amount and Quantity per Day:")
daily_orders_summary.show()

# Load the partitioned inventory data
inventory_df = spark.read.parquet(inventory_parquet_path)

# 2. Calculate total inventory quantity per category
category_inventory_summary = inventory_df.groupBy("category").agg(
    spark_sum("quantity").alias("total_inventory_quantity")
)

print("Total Inventory Quantity per Category:")
category_inventory_summary.show()

# Stop the Spark session
spark.stop()
