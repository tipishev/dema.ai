# Dockerfile

# Use the official AWS Glue version 4 image
FROM amazon/aws-glue-libs:glue_libs_4.0.0_image_01

# Set working directory inside the container
WORKDIR /home/glue_user/workspace

# Copy the PySpark script and data files into the workspace directory
COPY echo.py /home/glue_user/workspace/echo.py
COPY orders.csv /home/glue_user/workspace/orders.csv
COPY inventory.csv /home/glue_user/workspace/inventory.csv

# Set the DISABLE_SSL environment variable to true
ENV DISABLE_SSL=true

# Expose the Spark UI ports for monitoring
EXPOSE 4040 18080
