### 1. Configuration of Connection 

Visit airflow UI and click connections under the section of Admin. 

Assuming that you have named "db_sqlite" for your connection id, following are a sreies of steps you need to prepare the SQLite table. 

- First,you need to put the exactly same name to "Conn Id" with "Conn Type" set to "Sqlite". 

- Write some memos that expalin what is about the connecitons.

- As for host, you need to specify the path in which "airflow.db" is stored followed by it.(eg  /home/airflow/ariflow/airflow.db)

Now, wee need to check if the conneciton has added to the list successufly. 

![image](https://user-images.githubusercontent.com/53164959/109615081-cec05280-7b76-11eb-8dc6-c5d4261aedb0.png)




