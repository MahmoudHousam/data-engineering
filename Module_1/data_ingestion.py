import os
import argparse
import pandas as pd
from time import time
import pyarrow.parquet as pq
from urllib.parse import urlparse
from sqlalchemy import create_engine


def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url
    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")
    mimic_df = pd.read_csv("mimic3c.csv")
    print("Pulling data to DB...")
    start_time = time()
    mimic_df.to_sql(name=table_name, con=engine, if_exists="append")
    end_time = time()
    print(f"Data pulled to DB in: {end_time - start_time} seconds")
    # parsed_url = urlparse(url)
    # file_name = os.path.basename(parsed_url.path)
    # url2 = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet"
    # os.system(f"curl {url2} -o yellow_tripdata_2023-01.parquet")
    # parquet_file = pq.ParquetFile("yellow_tripdata_2023-01.parquet")
    # for batch in parquet_file.iter_batches(batch_size=100000):
    #     start_time = time()
    #     print("Fetching a new batch...")
    #     batch_df = batch.to_pandas(date_as_object=False)
    #     print("Fetched!")
    #     print("Appending batch to DB...")
    #     batch_df.to_sql(name=table_name, con=engine, if_exists="append")
    #     print("Appended!")
    #     end_time = time()
    #     print(f"Batch took: {end_time - start_time} seconds")
    
def parsing_args():
    parser = argparse.ArgumentParser(description="Ingest NY Taxi data to Postgres DB")
    parser.add_argument("--user", help="postgres username")
    parser.add_argument("--password", help="postgres password")
    parser.add_argument("--host", help="postgres host")
    parser.add_argument("--port", help="postgres port")
    parser.add_argument("--db", help="postgres DB name")
    parser.add_argument("--table_name", help="ingested table")
    parser.add_argument("--url", help="URL to ingest data from")
    return parser.parse_args()


if __name__ == "__main__":
    args = parsing_args()
    main(params=args)




