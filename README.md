# Dema.ai Mini Datalake

This project provides a Dockerized setup for data ingestion and SQL-like aggregation on AWS Glue with Spark. The setup reads CSV files ([orders.csv](orders.csv) and [inventory.csv](inventory.csv)), stores them as partitioned Parquet files, and performs aggregation using both PySpark DataFrame API and SQL-like queries.

## Project Structure

[ingest.py](ingest.py): Ingests data from CSV files, partitions inventory by category and orders by date, and saves them as Parquet files.
aggregate.py: Performs aggregation using PySpark DataFrame API.
aggregate_sql.py: Performs aggregation using Spark SQL for a SQL-like experience.
Makefile: Contains commands for building and running the Docker container with various tasks.
Prerequisites
Docker: Ensure Docker is installed on your machine.
Setup Instructions
Clone the Repository: bash git clone <repository-url> cd <repository-directory>

Add Data Files: Place your orders.csv and inventory.csv files in the project root directory.

Makefile Commands
Build the Docker Image
To build the Docker image:

go
Copy code
make build
Run Data Ingestion
To ingest the data and save it as partitioned Parquet files:

go
Copy code
make ingest
Run Aggregation with PySpark DataFrame API
To run aggregation using PySpark DataFrame API:

go
Copy code
make aggregate
Run Aggregation with Spark SQL
To run aggregation using Spark SQL:

go
Copy code
make aggregate_sql
Open an Interactive Shell in the Container
To open an interactive shell in the container:

go
Copy code
make shell
Clean Up Docker Image
To remove the Docker image:

go
Copy code
make clean
Build and Run Ingestion in a Single Step
To build the Docker image and run the ingestion step in one command:

css
Copy code
make all
Aggregation Outputs
aggregate.py:

Aggregates orders by date, showing total amount and quantity.
Aggregates inventory by category, showing total inventory quantity.
aggregate_sql.py:

Runs SQL queries for similar aggregations.
License
This project is open source and available under the MIT License.
