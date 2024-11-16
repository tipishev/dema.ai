# Define variables
IMAGE_NAME = glue-spark-demo
CONTAINER_NAME = glue_spark_submit
DOCKER_RUN_OPTS = -it -v $(PWD):/home/glue_user/workspace/ -e DISABLE_SSL=true --rm -p 4040:4040 -p 18080:18080 --name $(CONTAINER_NAME)

# Build the Docker image
build:
	docker build -t $(IMAGE_NAME) .

# Run the ingestion script in the Docker container
ingest:
	docker run $(DOCKER_RUN_OPTS) $(IMAGE_NAME) spark-submit /home/glue_user/workspace/ingest.py

# Run the data quality check script in the Docker container
quality_check:
	docker run $(DOCKER_RUN_OPTS) $(IMAGE_NAME) spark-submit /home/glue_user/workspace/quality_check.py

# Run the aggregation script in the Docker container
aggregate:
	docker run $(DOCKER_RUN_OPTS) $(IMAGE_NAME) spark-submit /home/glue_user/workspace/aggregate.py

# Run the aggregation script in the Docker container
aggregate_sql:
	docker run $(DOCKER_RUN_OPTS) $(IMAGE_NAME) spark-submit /home/glue_user/workspace/aggregate_sql.py

# Open an interactive shell in the container
shell:
	docker run $(DOCKER_RUN_OPTS) $(IMAGE_NAME)

# Clean up any dangling images
clean:
	docker rmi $(IMAGE_NAME)

# Combine build and ingestion run in a single command
all: build ingest
