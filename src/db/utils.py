from sqlalchemy import text, create_engine, inspect
import pandas as pd
engine = create_engine("iris://SQLAdmin:joTB-2023@k8s-f444a1c6-a4058360-90ad00025c-d20a3c2e72757fae.elb.eu-central-1.amazonaws.com:1972/USER")

def inspect_schemas():
    inspector = inspect(engine)
    schemas = inspector.get_schema_names()
    for schema in schemas:
        print("schema:", schema)
        for table_name in inspector.get_table_names(schema=schema):
            print('\ttable:', table_name)
            for column in inspector.get_columns(table_name, schema=schema):
                print("\t\tcolumn:", column)

def query_table(cols: list, table: str) -> pd.DataFrame:
    sql_query = f"SELECT {', '.join(cols)} FROM {table}"
    with engine.connect() as connection:
        result = connection.execute(text(sql_query))
        return pd.DataFrame(result)
    
def generic_query(sql_text: str):
    with engine.connect() as connection:
        if result:= connection.execute(text(sql_text)):
            df = pd.DataFrame(result)
            print(df)
            return df
    
def load_table(df: pd.DataFrame, table_name: str, schema: str = 'hk', if_exists: str = 'replace'):
    with engine.begin() as connection:
        df.to_sql(table_name, connection, schema=schema, if_exists=if_exists)
