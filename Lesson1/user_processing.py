from airflow.models import DAG
from airflow.providers.sqlite.operators.sqlite import SqliteOperator
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from pandas import json_normalize
import json

defaultParams={'function':'OVERVIEW',
        'symbol':'IBM',
        'apikey':"OPF63VL4JTRN9IR8"}


def processing_companies(ti):
    company=ti.xcom_pull(task_ids=['extracting_company'])[0]
    if "Symbol" not in company:
        raise ValueError("Loaind is unsuccessful")
    proccessed_user=json_normalize({
        "symbol":company["Symbol"],
        "type":company[ "AssetType"],
        "name":company["Name"]
    })
    proccessed_user.to_csv("/tmp/companies.csv",index=None,header=False)


with DAG("user_processing",schedule_interval="@daily",start_date=datetime(2021,2,27),catchup=False) as dag:
    creating_table=SqliteOperator(
        task_id="creating_table",
        sqlite_conn_id="db_finance",
        sql='''
        CREATE TABLE IF NOT EXISTS overview(
            symbol TEXT NOT NULL PRIMARY KEY,
            assettype TEXT NOT NULL,
            name TEXT NOT NULL
        );
        '''
    )
    is_api_available=HttpSensor(
        task_id="is_api_available",
        http_conn_id="finance_api",
        request_params=defaultParams,
        endpoint='query?'
    )

    extracting_task=SimpleHttpOperator(
        task_id="extracting_company",
        http_conn_id="finance_api",
        endpoint="query?",
        data=defaultParams,
        method="GET",
        response_filter=lambda response:json.loads(response.text),
        log_response=True
    )

    processing_companies=PythonOperator(
        task_id="processing_user",
        python_callable=processing_companies
    )

    storing_user=BashOperator(
        task_id="storing_company",
        bash_command='echo -e ".separator ","\n.import /tmp/companies.csv overview" | sqlite3 /home/airflow/airflow/airflow.db'
        )



   creating_table >> is_api_available >> extracting_users >> processing_user >> storing_user




