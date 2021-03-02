###  1. Creating DAG ID

This is a must to check if the DAG id we have previsouly specify is succssfully created with being free of errors. To check its status, just find the name of your Dag id in your list. Otherwise, you will be notifed what went wrong from the error message. From the below, we can find that the dag has been created without any error.

![image](https://user-images.githubusercontent.com/53164959/109617065-455e4f80-7b79-11eb-9908-b5ddaeaa84a1.png)


### 2. Configuration of Connection 

Visit airflow UI and click connections under the section of Admin. 

Assuming that you have named "db_sqlite" for your connection id, following are a sreies of steps you need to prepare the SQLite table. 

- First,you need to put the exactly same name to "Conn Id" with "Conn Type" set to "Sqlite". 

- Write some memos that expalin what is about the connecitons.

- As for host, you need to specify the path in which "airflow.db" is stored followed by it.(eg  /home/airflow/ariflow/airflow.db)

Now, wee need to check if the conneciton has added to the list successfully.

![image](https://user-images.githubusercontent.com/53164959/109615081-cec05280-7b76-11eb-8dc6-c5d4261aedb0.png)


### 3 Creating Table

Open your terminal and write a single line of code below. 

```linux
airflow tasks test  your_dag_id your_task_id start_date 
eg) airflow tasks test user_processing cretingTable 2021-03-01
```
If your python code does not contain gramatical erros, the table would be immediately set up and ready for use.
It should be helpful to check out the name of the newly created table by accessing the sqlite3 database.

```linux
sqlite3 airflow.db
sqlite> .tables 
```


### 4. Availabilty of API

Before proceeding to the further stage, we need to better check out the existence of API from which we can download data. The steps are much similar to what we did in the section 2 excepts that infomration you enter is different.  

![image](https://user-images.githubusercontent.com/53164959/109629573-4a2a0000-7b87-11eb-9443-a19d5e33e5ec.png)

Again, to perform the given task, we need to implement a line of code below. 

```linux
airflow tasks test dag_id task_id starte_date
eg) airflow tasks test user_processing is_api_available 2021-03-01
```




