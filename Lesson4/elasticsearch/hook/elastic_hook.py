from airflow.hooks.base import BaseHook
from elasticsearch import Elasticsearch

class ElasticHook(BaseHook):
    def __init__(self,conn_id='elasticsearch_default',*args,**kwargs):
        super().__init__(*args,**kwargs)
        conn=self.get_connection(conn_id)

        conn_config={}
        hosts={}

        if conn.host:
            hosts=conn.host.split(',')

        if conn.port:
            conn_config['port']=int(conn.port)

        if conn.login:
            conn_config['http_auth']=(conn.login,conn.password)

        self.es=Elasticsearch(hosts,**conn_config)
        self.index=conn.schema
    
    def info(self):
        return self.es.info()

    def set_index(self,index):
        self.index=index
    
    def add_doc(self,index,doc_type,body):
        self.set_index(index)
        result=self.es.index(index=index,doc_type=doc_type,body=body)
        return result 

