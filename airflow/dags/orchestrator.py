import sys
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime, timedelta

sys.path.append("/opt/airflow/app_code")

def safe_main_callable():
    from insert_records import main
    return main() 

default_args = {
    'description': 'Airflow DAG to orchestrate data',
    'start_date': datetime(2025, 11, 23),
    'catchup':'False' 
}

dag = DAG(
    dag_id='Weather-API-Orchestrator',
    default_args=default_args,
    schedule=timedelta(minutes=5)
)

with dag:
    task1 = PythonOperator(
        task_id='ingest_task_data',
        python_callable=safe_main_callable
    )