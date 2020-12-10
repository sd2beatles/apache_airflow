1. Run the code below
  
  ```
  vim airflow/airflow.cfg
  ```
  
2. Look for the executor parameter (ie the paramter determines the type of an excutor you want to use) and set the section like below

```
executor=LocalExecutor
```

3.Change the sql_alchemy_conn with the following format and save the fr

```
sql_alchemy_conn=mysql+mysqldb://login:password@localhost:host_number/schema_name

eg)
sql_alchemy_conn=mysql+mysqldb://airflow:airflow@localhost:3306/airflow_mdb
```

4.set parallelism and concurrency 

If you want allow for only one task instance at a time, then set dag_concurrency to 1. 
Otherwise, specify the number of task instances run by the scheduler concurrently. 


5. Stop airflow webserver and schduler and initialize the db by typing  'airflow initdb'.

6. Restart airflow webserver and scheduler 

7.Run the given python file(dynamic_dag.py) correspodinng to DAG
  
8. From the airflow url, we can click the section "Graph View" to see an overall structure. 

![image](https://user-images.githubusercontent.com/53164959/101836143-2eaeea80-3b80-11eb-94f4-18c9da213c08.png)

9. Admin -> Conncetions -> Create  and Fill out the necessary sections to run DAGs

![image](https://user-images.githubusercontent.com/53164959/101836266-6ae24b00-3b80-11eb-93b7-b9ceb53c7355.png)


10. All the DAG to run and now we can see how the executor has performed by clicking Gantt.

The image is showing that we have only one task instance possible at a time.

![image](https://user-images.githubusercontent.com/53164959/101836390-ab41c900-3b80-11eb-8bd4-2f25c4f6b9a6.png)

11.(option) Query the databases on the airflow interfaces by clikcing Data Profiling -> Ad Hoc Query 

![image](https://user-images.githubusercontent.com/53164959/101836586-05db2500-3b81-11eb-8e28-d18301eb86da.png)







