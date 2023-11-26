# main.py

from pyspark.sql import SparkSession
from transformation_functions import group_by_measure, join_data
import boto3

def main():
    # Initialize Spark session
    spark = SparkSession.builder.appName("DataPipeline").getOrCreate()

    # Read data from a source (e.g., CSV file)
    source_data = spark.read.csv("s3://your-s3-bucket/data.csv", header=True, inferSchema=True)

    # Transformation: Group By some Measure
    grouped_data = group_by_measure(source_data, "category")

    # Transformation: Join with another Data Pipeline or static datasets
    static_data = spark.read.json("s3://your-s3-bucket/static_data.json")
    joined_data = join_data(grouped_data, static_data, "category")

    # Write data to different formats and locations
    joined_data.write.parquet("s3://your-s3-bucket/output/parquet_data")
    joined_data.write.json("s3://your-s3-bucket/output/json_data")
    joined_data.write.option("compression", "gzip").csv("s3://your-s3-bucket/output/csv_data")

    # Stop Spark session
    spark.stop()

if __name__ == "__main__":
    main()
