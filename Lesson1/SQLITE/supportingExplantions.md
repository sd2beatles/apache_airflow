### 0. Importing all the relevant libraries 


```python
from airflow.models import DAG
from datetime import datetime
from airflow.providers.sqlite.operators.sqlite import SqliteOperator
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator
from pandas import json_normalize
import json

```




###  1. Creating DAG ID


```python 


with DAG("user_processing",schedule_interval="@daily",start_date=datetime(2021,3,1),catchup=False) as dag:
    creatingTable=SqliteOperator(
        task_id='creatingTable',
        sqlite_conn_id='db_sqlite',
        sql='''
        CREATE TABLE IF NOT EXISTS users (
            firstname TEXT NOT NULL,
            lastname TEXT NOT NULL,
            country TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            email TEXT NOT NULL PRIMARY KEY 
        );
        '''
        )


````




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

```python
    is_api_available=HttpSensor(
        task_id="is_api_available",
        http_conn_id="user_api",
        endpoint='api/'
    )



```


Before proceeding to the further stage, we need to better check out the existence of API from which we can download data. The steps are much similar to what we did in the section 2 excepts that infomration you enter is different.  

![image](https://user-images.githubusercontent.com/53164959/109629573-4a2a0000-7b87-11eb-9443-a19d5e33e5ec.png)

Again, to perform the given task, we need to implement a line of code below. 

```linux
airflow tasks test dag_id task_id starte_date
eg) airflow tasks test user_processing is_api_available 2021-03-01
```


### 5. Extracting Data 

In this step,there is nothing special. Right after writing a python code, implement a code below again

```python

   extracting_user=SimpleHttpOperator(
        task_id="extracting_user",
        http_conn_id="user_api",
        endpoint="api/",
        method="GET",
        response_filter=lambda response:json.loads(response.text),
        log_response=True
    )


```


```linux

airflow tasks test dag_id task_id starte_date
eg)airflo taskts test user_processing extracting_user 2020-03-01
```


### 6. Saving Data to Directory Folder 


```python

def _processing_user(ti):
    users=ti.xcom_pull(task_ids=["extracting_user"])

    if not len(users) or 'results' not in users[0]:
        raise ValueError("User is empy")

    user=users[0]['results'][0]
    processed_user=json_normalize({
        'firstname':user['name']['first'],
        'lastname':user['name']['last'],
        'country':user['location']['country'],
        'username':user['login']['username'],
        'password':user['login']['password'],
        'email':user['email']
        })
    processed_user.to_csv("/tmp/processed_user.csv",index=None,header=False)
    
    processing_user=PythonOperator(
        task_id="processing_user",
        python_callable=_processing_user
    )


 ```
 
 
 ```linux
 airflow tasks test dag_id task_id 
 eg) airflow tasks test user_processing processing_user
 ```

Here is the point where x.com_pull kicks in. All the loaded data must be saved to a file under your pre-assigned folder. Our code will make use of xcom to make it possible. 

:arrow_forward:   What is xcom?  

For simplicity, think of xcom as a way of sharing data among tasks in airflow. For example, in our code, "extracting user" will create x.com and  the data we extract through the task will be stored as x.com in the main database of airflow. The key and value will be given automatically where key is a unique value identifying the data and value is data we obtain. When you want to fatch it from the master of airflow , you simply call the function,xcom.pull,with the right task id. 


### 7. File to SQLite3

For simple code explanation, we specified the separator of our values in the file. And then we will execute the "import" to bring the values 
from the storage of data to the table under SQLite3 database. 


```python
 storing_user=BashOperator(
        task_id="storing_user",
        bash_command='echo -e ".separtor ","\n.import /tmp/processed_user.csv users" | sqlite3 /home/airflow/airflow/airflow.db'
    )
```

```linux
 airflow tasks test dag_id task_id 
 eg) airflow tasks test user_processing storing_users
```

![image](https://user-images.githubusercontent.com/53164959/109639469-8f9ffa80-7b92-11eb-83e0-aceed5c26c7c.png)

If you want to check that data has been sent to the pre-assigned table, run the code below in your terminal.

```linux
sqlite3 airflow.db

sqlite> SELECT * FROM users;

```













