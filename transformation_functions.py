# transformation_functions.py

from pyspark.sql.functions import sum

def group_by_measure(data_frame, measure_column):
    return data_frame.groupBy(measure_column).agg(sum("value").alias("total_value"))

def join_data(data_frame1, data_frame2, join_column):
    return data_frame1.join(data_frame2, join_column)
