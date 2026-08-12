from urllib.parse import urlparse

#TRACKING_URI = "file:./mlruns"
TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI")
EXPERIMENT_NAME = "HousePriceExperiment"
MODEL_NAME = "Best Randomforest Model"
