# from pyspark.sql import functions as F
from transforms.api import transform_df, Input, Output


@transform_df(
    Output(
        "/SOLEX-a8870f/[Notional] RAP Playground/Data Engineering Tutorials - Code Repositories/Datasource Project: Flight Alerts/datasets/clean/flight-alerts-clean"
    ),
    source_df=Input(
        "/SOLEX-a8870f/[Notional] RAP Playground/Data Engineering Tutorials - Code Repositories/Datasource Project: Flight Alerts/datasets/preprocessed/flight_alerts_preprocessed"
    ),
)
def compute(source_df):
    return source_df
