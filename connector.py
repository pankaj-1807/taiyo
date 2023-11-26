# connector.py

import boto3
from pyspark.sql import SparkSession

def read_from_s3(spark, bucket, key):
    s3 = boto3.client("s3")
    obj = s3.get_object(Bucket=bucket, Key=key)
    return spark.read.csv(obj['Body'], header=True, inferSchema=True)

def write_to_s3(data_frame, bucket, key, format):
    data_frame.write.format(format).save(f"s3://{bucket}/{key}")
