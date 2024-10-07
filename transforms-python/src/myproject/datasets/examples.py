# from pyspark.sql import DataFrame
# 
# # from pyspark.sql import functions as F
# from transforms.api import Input, Output, transform_df
# 
# from myproject.datasets import utils
# 
# 
# @transform_df(
#     Output("/SOLEX-a8870f/[Notional] RAP Playground/TARGET_DATASET_PATH"),
#     source_df=Input("/SOLEX-a8870f/[Notional] RAP Playground/SOURCE_DATASET_PATH"),
# )
# def compute(source_df: DataFrame):
#     return utils.identity(source_df)
