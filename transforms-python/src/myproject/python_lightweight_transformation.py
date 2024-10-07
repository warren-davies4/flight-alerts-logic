from transforms.api import Input, Output, transform, lightweight


@lightweight(cpu_cores=1, memory_gb=8)
@transform(
    output_dataset=Output("/SOLEX-a8870f/[Notional] RAP Playground/Data Engineering Tutorials - Code Repositories/Datasource Project: Flight Alerts/myproject/python_lightweight_transformation"),
    input_dataset=Input("SOURCE_DATASET_PATH"),
)
def polars_lightweight_transform(output_dataset, input_dataset):
    polars_df = input_dataset.polars()
    output_dataset.write_table(polars_df.limit(10))


@lightweight
@transform(
    output_dataset=Output("/SOLEX-a8870f/[Notional] RAP Playground/Data Engineering Tutorials - Code Repositories/Datasource Project: Flight Alerts/myproject/python_lightweight_transformation"),
    input_dataset=Input("SOURCE_DATASET_PATH"),
)
def pandas_lightweight_transform(output_dataset, input_dataset):
    pandas_df = input_dataset.pandas()
    output_dataset.write_table(pandas_df.head(10))
