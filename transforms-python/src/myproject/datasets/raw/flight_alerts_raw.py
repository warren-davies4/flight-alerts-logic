# from pyspark.sql import functions as F
from transforms.api import transform_df, Input, Output

@transform_df(
    Output("/SOLEX-a8870f/[Notional] RAP Playground/Data Engineering Tutorials - Code Repositories/Datasource Project: Flight Alerts/datasets/raw/flight_alerts_raw"),
    source_df=Input("/SOLEX-a8870f/[Notional] RAP Playground/Advanced incremental data processing with PySpark in Code Repositories (2024-10-04 16:01:09)/2_multi_inputs_outputs"),
)
def compute(source_df):
    return source_df
