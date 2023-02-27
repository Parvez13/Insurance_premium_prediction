import pymongo
import pandas as pd
import json
from insurance.config import mongo_client

DATA_FILE_PATH = "insurance.csv"
DATABASE_NAME = "insurance_database"
COLLECTION_NAME = "insurance_collection"

if __name__ == '__main__':
    df = pd.read_csv(DATA_FILE_PATH)
    df.reset_index(drop=True, inplace=True)
    json_records = list(json.loads(df.T.to_json()).values())
    mongo_client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_records)
    print("Insertion into Database done.")