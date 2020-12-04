from airflow import DAG
from airflow.contrib.sensors.file_sensor import FileSensor
from datetime import datetime

default_args={
    "start_date":date_time(2020,1,1),
    "owner":"airflow"
}

with DAG(dag_id="twitter_dag",scheduler_interval="@daily",default_args=default_args) as dag:
    waiting_for_tweets=FileSensor(taks_id="waiting_for_tweets",fs_conn_id="fs_tweet",file_path="data.csv",poke_interval=5)


'''
#Try running the code below to check wether the specific file is avialbe

airflow test dag_id task_id starting_date

eg) airflow test twitter_dag waiting_for_tweets 2020-12-05 
'''


