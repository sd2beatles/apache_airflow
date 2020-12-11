from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.mysql_operator import MySqlOperator
import datatime as dt

default_args={
    'start_date':dt.datetime(2020,1,1),
    'owner':'airflow',
    'retries':0
}
with DAG(dag_id="dynamic_dag",
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False
        ) as dag:
    opr_end=BashOperator(task_id="opr_end",bash_command='echo "Done"')
    #Dynamic definitions of your DAG
    for counter in range(1,4):
        task_id='opr_insert_'+str(counter)
        task_date=dt.datatime.now.strftime('%Y:%m:%d %H:%M:%S')
        opr_insert=MySqlOperator(task_id=task_id,
                                 sql="INSERT INTO tasks (id,timestamp) VALUES ('"+task_id+"_"+task_date+"','"+"task_date"+"');",
                                 mysql_conn_id='mysql',
                                 autocommit=True,
                                 database='airflow_mdb')
        opr_insert > opr_end
        
                                 
    
    
