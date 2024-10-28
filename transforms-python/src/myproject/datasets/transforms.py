import os
import glob
from pathlib import Path
from pyspark.sql import SparkSession

def transform_df(output, input):
    def _(original_compute):
        def decorated_compute(*args, **kwargs):
            spark = SparkSession.getActiveSession()
            df_input = spark.read.csv(input, header=True)
            df_processed = original_compute(df_input)
            save_spark_dataframe_as_csv(df_processed, output)
            return df_processed
        return decorated_compute
    return _


def save_spark_dataframe_as_csv(
    df_input, 
    output_folder : str
) -> None:
    """
    Function to save a spark dataframe as a csv to a new folder in the data_out folder

    Parameters
    ----------
        df_input : pyspark.DataFrame
            The spark dataframe that you want to save as csv
        output_folder : str
            The name for the folder in which the csv file will be saved
    """

    (df_input
        .write
        .mode('overwrite')
        .option("header", True)
        .csv(str(Path(output_folder)))
    )