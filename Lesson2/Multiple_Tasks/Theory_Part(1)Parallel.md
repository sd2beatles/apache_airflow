
![image](https://user-images.githubusercontent.com/53164959/110245267-cb2d3100-7fa5-11eb-9e26-ad14504dbdd7.png)


### 1. Objectives 

:point_right: Here is a list of questions we should answer after the lecture. 

- How to configure Airflow for executing multiple tasks?

- What are the important prameters to know?

- What are the different executors for scaling Airflow?


### 2. Default Mode 


![image](https://user-images.githubusercontent.com/53164959/109650883-312e4880-7ba1-11eb-8452-5aa0795313a1.png)

Let's briefly talk about how the airflow configuration runs by default. If you look at the diagram of the flow chart, it is not hard to see that the first task will be executed foremost. The real issue here is what is the next task the apache airflow performs? Since task B and task C are on the same level, it looks reasonable to say that two tasks are to be performed in parallel.  This is not true under the default configuration of airflow. 

"The default configuration only allows for sequential mode, which means that tasks will be performed one after another."

Before moving to the step of changing the setting, there are coule of things we should be aware of; 

- SQLite3 does not support parallel quries. If you want to make the quries work, you need to select another sql lanaguage apart from SQLite3. 

- By default, airflow database is automatically connected to the SQLite3. 
 ```linux
 airflow config get-value core sql_alchmey_conn
 airflow config get-value core executor 
 ```
![image](https://user-images.githubusercontent.com/53164959/109655015-27f3aa80-7ba6-11eb-9d19-edea611911ff.png)



### 3. Changing the default Settings

Open airflow.cfg file and find "sql_alchemy_conn". Here we will use postgre sql as a main sql database but the choice of databse system
depends on your preference. 

```linux
sql_alchemy_conn=postgresql+psycopg2://<user name>:<passsword>@<port>/<the name of database we willl use with airflow>              
eg)sql_alchemy_conn=postgresql+psycopg2://postgres:postgres@localhost/postgres

```
Now, we need one more thing to change. 

```linux
executor=LocalExecutor
```
If you have any airlfow servers or/and scheduler running in your virtual machine, you stop everthing and initialize postgres database.
In your terminal, write the code for initialization

```linux
airflow db init
```
![image](https://user-images.githubusercontent.com/53164959/109755175-d6403400-7c28-11eb-9788-d76311830b53.png)

Now,we need to create a new user under the new environmetal settings. The basic format is following below and fill every section to your preference. As for -r, you can choose one of the given options; Admin, Public, Viewer, User, Op.

```sql
airflow users create -u <username> -p <passowrd>  -r <role> -f <family name> -l <last name> -e <email>

eg)airflow users create -u admin -p admin -r Admin -f admin -l admin -e admin@airflow.com

```

Restart airflow webserver and scheduler. Vist your local webserver to log in with your new account.
By clicking "Gantt" in your webserver, We can double check whether our configuration are compatible and set up well for parallel programming. 

![image](https://user-images.githubusercontent.com/53164959/109756161-bb6ebf00-7c2a-11eb-9f02-02dab4cf9013.png)






 
 





