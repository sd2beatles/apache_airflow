![image](https://user-images.githubusercontent.com/53164959/99251405-a3785880-2850-11eb-8343-9739679ce315.png)


# Section 2. Operator 

### 2.1 Definition 

While DAGs describes how to run a workflow, operators determine what actually gets doen.


An operator describes a single task in a workflow. Operators are usually (but not always) atomic, meaning they can stand on their own and don’t need to share resources with any other operators. The DAG will make sure that operators run in the correct order; other than those dependencies, operators generally run independently. In fact, they may run on two completely different machines.

This is a subtle but very important point: in general, if two operators need to share information, like a filename or small amount of data, you should consider combining them into a single operator. If it absolutely can’t be avoided, Airflow does have a feature for operator cross-communication called XCom that is described in the section XComs

                                                                                                    

### 2.2 Key Things to Remember

The key features of operators we should be familiar with are 

- The Operatior are regarded as the definition of a __single__ task.
- The operator should be impotent,which explains regardless of how many times it is run, the operator should produce the same result.
- Any assigned task can be repeatedly __retried__ in the time of failure.
- A task is created by __instantiating__ an Operator class.
- An operator defines the nature of a task and how it should be executed.
- When an operator is instantiated, the assigend task now becomes a node in your DAG.


### 2.3 Types of Operators

- Therea are three major types of opertors we often see 
  - __Action Operators__ is closely related to performing an action. 
  
  - __Transfer Operators__ 
     - is playing a key role to moving data from one systemt to another
     - Data will be pulled out from the source,staged on the machine where the executor is running and then trasferred to the target system
     - Do not use this operator unless your can not accomodate a large amount of data
     
  - __Sensor Operators__ waits for data to arrive a a defined location. 
    - They are useful for monitoring external process like waiting for files to uploaded in HDFS or a partition appering in Hive
    - They are basically long running task
    - The Sensor operators have a poke method called repeatedly until it return true
  
   eg) the example code for sensor operator
    
```python
    from airflow import DAG
    from airflow.contrib.operators.file_sensor import FileSensor
    with DAG(dag_id="twitter_dag",schedule_interval="@daily") as dag:
       """
       Parameters :
  
       fs_conn_id:id of connection where the path of the file will be stored
  
       filepath:a file name related to the base path set
 
      task ID: an unique identifier for a given task
 
      poke_interval : defines the interval at which the folder of the file will be
                      checked. In our code, the task will check every five second
      """
      waiting_for_tweets=FileSensor(task_id="waiting_for_tweets",fs_conn_id="fs_tweet",\n
                                    filepath="data.csv",poke_interval=5)


```
Right after writing the code and saving it, we should revist the airflow web browser. Fill out the sections in order to run the code.

![image](https://user-images.githubusercontent.com/53164959/100551884-ef061a00-32c6-11eb-9675-8b1c1b469260.png)

  
