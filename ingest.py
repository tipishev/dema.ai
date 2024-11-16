from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date

# Initialize a Spark session
spark = SparkSession.builder \
    .appName("Ingest Data and Partition") \
    .getOrCreate()

# Define input paths for CSV files
orders_path = "/home/glue_user/workspace/orders.csv"
inventory_path = "/home/glue_user/workspace/inventory.csv"

# Define output paths for partitioned Parquet files
orders_output_path = "/home/glue_user/workspace/data/orders"
inventory_output_path = "/home/glue_user/workspace/data/inventory"

# Load the Orders dataset and partition by date (extracted from dateTime)
orders_df = spark.read.csv(orders_path, header=True, inferSchema=True)
orders_df = orders_df.withColumn("date", to_date(col("dateTime")))  # Extract date from dateTime
orders_df.write.partitionBy("date").parquet(orders_output_path, mode="overwrite")

# Load the Inventory dataset and partition by category
inventory_df = spark.read.csv(inventory_path, header=True, inferSchema=True)
inventory_df.write.partitionBy("category").parquet(inventory_output_path, mode="overwrite")

# Stop the Spark session
spark.stop()
