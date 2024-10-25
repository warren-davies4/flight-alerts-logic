# from pyspark.sql import functions as F
from transforms.api import transform_df, Input, Output
from myproject.datasets import cleaning_utils as clean


@transform_df(
    Output(
        "/SOLEX-a8870f/[Notional] RAP Playground/Data Engineering Tutorials - Code Repositories/Datasource Project: Flight Alerts/datasets/processed/flight_alerts_processed"
    ),
    source_df=Input("/SOLEX-a8870f/[Notional] RAP Playground/Data Engineering Tutorials - Code Repositories/Datasource Project: Flight Alerts/datasets/preprocessed/flight_alerts_preprocessed"),
)
def compute(source_df):
    df_output = clean.add_processed_col(source_df)
    return df_output
