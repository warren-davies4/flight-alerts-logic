from transforms.api import Pipeline

from myproject import datasets

from myproject.datasets import clean


my_pipeline = Pipeline()
my_pipeline.discover_transforms(datasets.clean)
