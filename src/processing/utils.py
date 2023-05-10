from db.utils import generic_query
import pandas as pd


def create_model(model_name: str, col: str, table: str, ):
    generic_query(f"CREATE MODEL {model_name} PREDICTING {col} FROM {table}")


def train_model(model: str, table: str):
    generic_query(f"TRAIN MODEL {model} FROM {table} AS trained_{model}")

def validate_model(model: str, dataset: str):
    generic_query(f"VALIDATE MODEL {model} From {dataset}")


def get_trained_models()-> pd.DataFrame:
    return generic_query("SELECT * FROM INFORMATION_SCHEMA.ML_TRAINED_MODELS")
    

def model_predict(model: str) -> pd.DataFrame:
    return generic_query(f"PREDICT( {model})")


