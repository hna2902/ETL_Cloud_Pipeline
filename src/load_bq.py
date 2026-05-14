from google.cloud import bigquery
import time
import os

PROCESSED_DATA_PATH = "data/processed/ecommerce_cleaned.parquet"
# Thêm Project ID
PROJECT_ID = "ecommerce-etl-pipeline"
DATASET_ID = "ecommerce_dataset"
TABLE_NAME = "behavior_logs"
# Định dạng chuẩn của BigQuery: project.dataset.table
table_id = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_NAME}"

def run_load():
    print("Loading to BigQuery")
    start_time = time.time()
    client = bigquery.Client(project = PROJECT_ID)
    job_config = bigquery.LoadJobConfig(
        source_format = bigquery.SourceFormat.PARQUET,
        write_disposition = bigquery.WriteDisposition.WRITE_TRUNCATE,
    )
    print(f"Reading {PROCESSED_DATA_PATH} and upload to cloud")
    with open(PROCESSED_DATA_PATH, "rb") as source_file:
        load_job = client.load_table_from_file(
            source_file,
            table_id,
            job_config = job_config
        )
    load_job.result()
    end_time = time.time()

    destination_table = client.get_table(table_id)
    print("Succeed")
    print(f"Loading {destination_table.num_rows} into BigQuery")
    print(f"Time: {round(end_time - start_time, 2)} seconds")

if __name__ == "__main__":
    if not os.path.exists(PROCESSED_DATA_PATH):
        print(f"Cannot find the file {PROCESSED_DATA_PATH}")
    else:
        run_load()