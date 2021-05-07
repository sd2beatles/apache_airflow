from airflow.models import BaseOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from plugins.elasticsearch_plugin.hooks.elastic_hook import ElasticHook
from contextlib import closing
import json

class PostgresToElasticOperator(BaseOperator):
    def __init__(self,sql,index,postgres_conn_id='postgres_default',elastic_conn_id="elasticsearch_default",*args,**kwargs):
        super(PostgresToElasticOperator,self).__init__(*args,**kwargs)
        self.sql=sql
        self.index=index
        self.postgres_conn_id=postgres_conn_id
        self.elastic_conn_id=elastic_conn_id

    def execute(self,context):
        es=ElasticHook(conn_id=self.elastic_conn_id)
        pg=PostgresHook(postgres_conn_id=self.postgres_conn_id)
        with closing(pg.get_conn()) as conn:
            with closing(conn.cursor()) as cur:
                cur.itersize=1000
                cur.execute(self.sql)
                for row in cur:
                    doc=json.dumps(row,indent=2)
                    es.add_doc(index=self.index,doc_type='external',body=doc)
        
