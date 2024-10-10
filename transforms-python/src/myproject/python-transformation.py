# from pyspark.sql import functions as F
from transforms.api import transform_df, Input, Output


@transform_df(
    Output(
        "/SOLEX-a8870f/[Notional] RAP Playground/Data Engineering Tutorials - Code Repositories/Datasource Project: Flight Alerts/myproject/python-transformation"
    ),
    source_df=Input("SOURCE_DATASET_PATH"),
)
def compute(source_df):
    return source_df
