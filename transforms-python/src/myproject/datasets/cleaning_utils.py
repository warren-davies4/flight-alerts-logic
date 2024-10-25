from pyspark.sql import functions as F


def add_clean_col(df):
    df = df.withColumn("clean", F.lit("Clean"))
    return df


def add_preprocessed_col(df):
    df = df.withColumn("preprocessed", F.lit("Preprocessed"))
    return df


def add_processed_col(df):
    df = df.withColumn("processed", F.lit("Processed"))
    return df
