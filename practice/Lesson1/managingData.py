
from airflow import DAG
from airflow.contrib.sensors.file_sensor import FileSensor
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

import fetching_tweet
import cleaning_tweet

source_dir='replace me'
destination_dir="replace me"

default_args={
    "start_date":datetime(2020,1,1),
    "owner":"airflow"
}

with DAG(dag_id="twitter_dag",default_args=default_args,schedule_interval="@daily") as dag:
    waiting_for_tweet=FileSensor(taks_id="waiting_for_tweet",poke_interval=5,fs_conn_id="fs_tweet")
    fetching_tweet=PythonOperator(task_id="fetching_for_tweet",fs_conn_id="fs_tweet",python_callable=fetcing_tweet.main)
    cleaning_tweet=PythonOperator(task_id="cleaning_for_tweet",fs_conn_id="fs_tweet",python_callable=cleaning_tweet.main)
    storing_tweet=BashOperator(task_id="storing_for_tweet",bash_commnad=f"hadoop fs put -f {source_dir} {destination_dir}")


