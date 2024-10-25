# from pyspark.sql import functions as F
from transforms.api import transform_df, Input, Output
from myproject.datasets import cleaning_utils as clean


@transform_df(
    Output(
        "/SOLEX-a8870f/[Notional] RAP Playground/Data Engineering Tutorials - Code Repositories/Datasource Project: Flight Alerts/datasets/preprocessed/flight_alerts_preprocessed"
    ),
    source_df=Input("ri.foundry.main.dataset.9857288a-d355-40cb-ba4b-179d7a1cdeb1"),
)
def compute(source_df):
    df_output = clean.add_preprocessed_col(source_df)
    return df_output
