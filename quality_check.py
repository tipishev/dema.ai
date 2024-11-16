from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize Spark session
spark = SparkSession.builder.appName("Data Quality Checks").getOrCreate()

# Paths to partitioned Parquet files
orders_parquet_path = "/home/glue_user/workspace/data/orders"
inventory_parquet_path = "/home/glue_user/workspace/data/inventory"

# Load data
orders_df = spark.read.parquet(orders_parquet_path)
inventory_df = spark.read.parquet(inventory_parquet_path)


# Function to print data quality check results
def check_data_quality(df, description):
    if df.count() > 0:
        print(f"Data Quality Issue: {description}")
        df.show()
    else:
        print(f"No issues found for: {description}")


# 1. Non-null Checks
check_data_quality(
    orders_df.filter(col("orderId").isNull()), "orders: Null values in orderId"
)
check_data_quality(
    inventory_df.filter(col("productId").isNull()),
    "inventory: Null values in productId",
)

# 2. Unique Constraints
check_data_quality(
    orders_df.groupBy("orderId").count().filter(col("count") > 1),
    "orders: Duplicate orderId",
)
check_data_quality(
    inventory_df.groupBy("productId").count().filter(col("count") > 1),
    "inventory: Duplicate productId",
)

# 3. Value Range Checks
check_data_quality(orders_df.filter(col("quantity") <= 0), "orders: quantity <= 0")
check_data_quality(
    inventory_df.filter(col("quantity") <= 0), "inventory: quantity <= 0"
)

# Stop the Spark session
spark.stop()
