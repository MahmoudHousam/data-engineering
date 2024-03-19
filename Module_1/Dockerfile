FROM python:3.9

RUN apt-get update && apt-get install wget curl -y
RUN pip install pyarrow pandas numpy sqlalchemy psycopg2

# ENV DATA_URL=https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet
# RUN curl $DATA_URL -o yellow_tripdata_2023-01.parquet

WORKDIR /data-engineering/Module_1

COPY data_ingestion.py data_ingestion.py

# data files should be mounted. This is a bad practice to follow that will be changed later.
# COPY yellow_tripdata_2023-01.parquet yellow_tripdata_2023-01.parquet

ENTRYPOINT ["python", "data_ingestion.py"]