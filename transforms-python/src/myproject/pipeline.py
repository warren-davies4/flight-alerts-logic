from transforms.api import Pipeline

from myproject import datasets

from myproject.datasets.clean import flight_alerts_clean
from myproject.datasets.preprocessed import flight_alerts_preprocessed
from myproject.datasets.processed import flight_alerts_processed

my_pipeline = Pipeline()

my_pipeline.add_transforms(my_compute_function)

my_pipeline.discover_transforms(datasets)
