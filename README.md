# Scalable Data Pipeline using PySpark

This repository contains a scalable data pipeline implemented in PySpark, designed to process and transform data, and store the results in various formats. The pipeline supports pluggable transformation functions, connectors for reading/writing data to different sources, and packaging for easy deployment.

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
- [Usage](#usage)
- [Data Pipeline Features](#data-pipeline-features)
  - [Plugable Transformation Functions](#plugable-transformation-functions)
  - [Connector-Based Design](#connector-based-design)
  - [Read/Write Data in Multiple Formats](#readwrite-data-in-multiple-formats)
- [Publishing as an Application](#publishing-as-an-application)
  - [Build and Deploy](#build-and-deploy)

## Introduction

This data pipeline is implemented in PySpark, providing a scalable solution for processing and transforming data. It includes pluggable transformation functions, connectors for reading/writing data from/to various sources, and supports multiple data formats.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following prerequisites installed:

- Python (3.x)
- Apache Spark
- Boto3 library (`pip install boto3`)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/pankaj-1807/taiyo.git

### Configuration
1. Set up AWS credentials:

     ```bash
    export AWS_ACCESS_KEY_ID=your_access_key_id
    export AWS_SECRET_ACCESS_KEY=your_secret_access_key

2. Configure S3 bucket and paths in main.py and connector.py.

### Usage

1. Run the data pipeline locally:

    ``` bash 
    python main.py
2. To simulate CI/CD, consider using a CI/CD tool (e.g., Jenkins, GitLab CI, GitHub Actions). Set up triggers, build configurations, and deployment scripts accordingly.

## Data Pipeline Features

### Plugable Transformation Functions

1. Group By some Measure:

The group_by_measure function in transformation_functions.py groups the data by a specified measure.

```bash
grouped_data = group_by_measure(source_data, "category")
```
2. Join some other Data Pipeline or static datasets:

The join_data function in transformation_functions.py joins two dataframes on a specified column.

``` bash 
joined_data = join_data(grouped_data, static_data, "category")
```

### Connector-Based Design

1. Read/Write from/to S3:

The connector.py file contains functions to read and write data to AWS S3.

``` bash 
# Read from S3
source_data = read_from_s3(spark, 'your-s3-bucket', 'path/to/data.csv')

# Write to S3
write_to_s3(joined_data, 'your-s3-bucket', 'output/parquet_data', 'parquet')
```
2. Read/Write from/to GCP, Files, Hadoop, SQL DB or file storage:

Extend the connector functions as needed for other data sources and sinks.

### Read/Write Data in Multiple Formats

- Read different formats:

``` bash 
source_data_json = spark.read.json("s3://your-s3-bucket/data.json")
source_data_parquet = spark.read.parquet("s3://your-s3-bucket/data.parquet")
```
- Write to different formats:

``` bash 
joined_data.write.json("s3://your-s3-bucket/output/json_data")
joined_data.write.parquet("s3://your-s3-bucket/output/parquet_data")
joined_data.write.option("compression", "gzip").csv("s3://your-s3-bucket/output/csv_data")
```

## Publishing as an Application

### Build and Deploy
1. Create a deployment package:

``` bash
python setup.py sdist
```
2. Deploy the package to your environment.

















