# Dema.ai Mini Datalake

This project provides a Dockerized setup for data ingestion and SQL-like aggregation on AWS Glue with Spark. The setup reads CSV files ([orders.csv](orders.csv) and [inventory.csv](inventory.csv)), stores them as partitioned Parquet files, and performs aggregation using both PySpark DataFrame API and SQL-like queries.

## Project Structure

NOTE: this demo project is intentionally flat, I would create `src/` and `csv/` if there were more files. 

* [ingest.py](ingest.py): Ingests data from CSV files, partitions inventory by category and orders by date, and saves them as Parquet files.
* [quality_check.py](quality_check.py): Runs simple quality checks on the data. In real world I would look into [Great Expectations](https://greatexpectations.io/).
* [aggregate.py](aggregate.py): Performs aggregation using PySpark DataFrame API.
* [aggregate_sql.py](aggregate_sql.py): Performs aggregation using Spark SQL for a SQL-like experience, your analysts will love that!
* [Makefile](Makefile): Contains commands for building and running the Docker container with various tasks.

## Prerequisites

* Docker: Ensure Docker is installed on your machine.

## Setup Instructions

```bash
git clone git@github.com:tipishev/dema.ai.git
cd dema.ai
make build
make ingest

# run a quality check on the ingested data
make quality_check

# run PySpark aggregation example
make aggregate

# run SQL-like aggregation example
make aggregate_sql

# if you fancy the container internals for debugging
make shell
```

## License
This project is open source and available under the MIT License.
