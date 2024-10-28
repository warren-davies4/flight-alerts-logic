# from transforms.api import Pipeline
from pyspark.sql import SparkSession

import datasets

from datasets.clean import flight_alerts_clean
from datasets.preprocessed import flight_alerts_preprocessed
from datasets.processed import flight_alerts_processed

# my_pipeline = Pipeline()
# my_pipeline.add_transforms(my_compute_function)
# my_pipeline.discover_transforms(datasets)

spark = (SparkSession
    .builder
    .appName("test")
    .getOrCreate()
)

df_raw = spark.read.csv("data_in/test_data.csv", header=True)

df_raw.show()

df_aggregated = (df_raw
    .transform(flight_alerts_clean.compute)
    .transform(flight_alerts_preprocessed.compute)
    .transform(flight_alerts_processed.compute)
)

df_aggregated.show()