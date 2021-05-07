from plugins.elasticsearch_plugin.operators.postgres_to_elastic import PostgresToElasticOperator
from plugins.elasticsearch_plugin.hooks.elastic_hook import ElasticHook
from airflow.operators.python import PythonOperator
from datetime import datetime
from airflow import DAG

default_args={
    'start_date':datetime(2020,1,1)
}


def _print_es_info():
    hook=ElasticHook()
    print(hook.info())

with DAG('elasticserach_dag',schedule_interval='@daily',default_args=default_args,catchup=False) as dag:
    print_es_info=PythonOperator(
        task_id='print_es_info',
        python_callable=_print_es_info
    )

    connections_to_es=PostgresToElasticOperator(
        task_id='connections_to_es',
        sql='SELECT * FROM connection',
        index='connections'
    )

    print_es_info >> connections_to_es
