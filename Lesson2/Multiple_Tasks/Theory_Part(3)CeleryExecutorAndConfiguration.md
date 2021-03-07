
![image](https://user-images.githubusercontent.com/53164959/110245285-dc763d80-7fa5-11eb-94c5-40f62eb89fb9.png)

:warning: Stop all the airflow webserver and scheduler before setting configuraiton

### 1. Install apache-airflow Celery and Redis [terminal]

Installration is pretty much simple and  you can simply follow the codes below

For installation of celery executors,

```linux
pip install 'apache-airflow[celery]'
```

For rebis,

```linux
sudo apt install redis-server
```
After installation finishes successfully, open a file named redis.config in your chosen editor. 

```linux
sudo vim /etc/redis/redis.conf
```
Now, if you land on the configuration file of redis, serach **_supervised no_** and change it to **_supervised systemd_**
Exit the file and write two lines of codes in your terminal and you will see a message.

```linux
sudo systemctl restart redis.service
sudo systemctl status redis.service

````

![image](https://user-images.githubusercontent.com/53164959/109773615-c2a1c700-7c42-11eb-84b2-6560bee51201.png)

## 2. Airflow Config [airflow.conifg]

Now that we understand the role of CeleryExecutor from the lecture, it is time to change the executor class that airflow should use from 
**_LocalExecutor_** to **_CeleryExecutor_**. 

Open the file **_airflow.config_** and find the **_executor_** and set it to **_CeleryExecutor_** with leaving **_sql_alchemy_conn_** as it is. 
There are some specific parameters coressponding to Celery that we should modify,

   - broker_url: 
     - Url used by Celery to push tasks to Redis Message Broker
     - Specify the **_connection to broker_url_** as following below.
       ```linux 
       #redis://<host>:<port_number>/<the name of database>
       broker_url=redis://localhost:6379/0
       ```
   - result_backend: the database that stores results from excution of tasks in the context of Celery
     - define the exactly same code to **_result_backend_** as we did on the **_sql_alchemy_conn_**
       ```linux
       result_backend=db+postgresql://postgres:postgres@localhost/postgres
       ```
       
 ## 3. Interaction with Redis [Terminal]
 
As previously mentioned, Celery uses borker_ulr to interact with Redis. To make it work in airflow, we need to install an extra pacakge to support the system. 
In your terminal, 

```linux
pip install 'apache-airflow[redis]'
```

## 4. Flower [Terminal]

One of features associed with the Celery Executors is **_flower_**. Its major function is a user-interface allowing users to monitor workers or
executors in action. To make use of it, we need to open a new terminal and put a code below 

```linux
airflow celery flower
```
Here is the message notifying you that the connection by default is 5555. 

![image](https://user-images.githubusercontent.com/53164959/109780120-0a781c80-7c4a-11eb-9147-f604113b8f21.png)

Open your local web and type "localhost:5555"

![image](https://user-images.githubusercontent.com/53164959/109780473-680c6900-7c4a-11eb-8933-5d3203c36180.png)

Since we do not assign any executors to our system, no execution of tasks is allowed at this point.  

## 5. Kicking Off Workers [Terminal] 
We need to execute a code to allow workers or machine to enter the celery cluster 

```linux
airflow celery worker
```


