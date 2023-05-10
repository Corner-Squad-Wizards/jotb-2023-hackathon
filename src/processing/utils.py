from db.utils import generic_query
import pandas as pd


def create_model(model_name: str, col: str, table: str, ):
    generic_query(f"CREATE MODEL {model_name} PREDICTING {col} FROM {table}")


def train_model(model: str, table: str):
    generic_query(f"TRAIN MODEL {model} FROM {table} AS trained_{model}")

def validate_model(model: str = "", val_name: str = "") -> pd.DataFrame:
    # generic_query(f"VALIDATE MODEL {model} From {dataset}")
    return generic_query(f"VALIDATE MODEL AcceptLoanReal2 AS {val_name} USE test3 from hk.loan_data_few")

def get_validation_metrics(val: str):
    return generic_query(f"select * from information_schema.ml_validation_metrics WHERE VALIDATION_RUN_NAME = '{val}'")


def get_trained_models(val: str)-> pd.DataFrame:
    return generic_query("SELECT * FROM INFORMATION_SCHEMA.ML_TRAINED_MODELS")
    
# model_predict('test1', 'hk.loan_data_some')
def model_predict(model: str, validation_set: str) -> pd.DataFrame:
    return generic_query(f"""
    SELECT 
      PREDICT(AcceptLoan use {model}) as prediction, 
      PROBABILITY(AcceptLoan use {model} ) as probability_accepted,
      * 
    FROM 
      {validation_set}
    """)


