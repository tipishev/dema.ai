# Define variables
IMAGE_NAME = glue-spark-demo
CONTAINER_NAME = glue_spark_demo

# Build the Docker image
build:
	docker build -t $(IMAGE_NAME) .

# Run the Docker container with necessary ports and environment variables
run:
	docker run -it \
		-v $(PWD):/home/glue_user/workspace/ \
		-e DISABLE_SSL=true \
		--rm \
		-p 4040:4040 \
		-p 18080:18080 \
		--name $(CONTAINER_NAME) \
		$(IMAGE_NAME)

# Doesn't work
# Open an interactive shell in the container
#shell:
#    docker run -it \
#        -v $(PWD):/home/glue_user/workspace/ \
#        -e DISABLE_SSL=true \
#        --rm \
#        -p 4040:4040 \
#        -p 18080:18080 \
#        --name $(CONTAINER_NAME) \
#        $(IMAGE_NAME) /bin/bash

# Clean up any dangling images
clean:
	docker rmi $(IMAGE_NAME)

# Combine build and run in a single command
all: build run

