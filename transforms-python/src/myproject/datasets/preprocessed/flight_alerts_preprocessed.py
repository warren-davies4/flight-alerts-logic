# from pyspark.sql import functions as F
# from transforms.api import transform_df, Input, Output
from datasets import cleaning_utils as clean
from datasets.transforms import transform_df

@transform_df(
    "data_out/preprocessed",
    "data_out/clean",
)
def compute(source_df):
    df_output = clean.add_preprocessed_col(source_df)
    return df_output
