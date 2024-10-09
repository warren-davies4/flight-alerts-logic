from pyspark.sql import functions as F


def add_hello_col(df):
    df = (                  df
                            .withColumn(
                                         "hello", 
                    F.lit("Hello")
                )
    )
    return df
