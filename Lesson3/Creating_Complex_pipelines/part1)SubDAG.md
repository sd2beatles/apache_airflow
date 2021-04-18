![image](https://user-images.githubusercontent.com/53164959/110245299-e4ce7880-7fa5-11eb-8a01-d4969484d8d8.png)

## 1. Introduction 

Just imagine that you have data pipelines that consist of three major tasks; downloading, checking files, and processing files with the dependencies. 

 ![image](https://user-images.githubusercontent.com/53164959/110196897-fff89580-7e8a-11eb-9548-1516ddfa65b9.png)

But our question here is "is there any feasible way to group tasks according to thier functionality and roles?"  For example, Because all the first tasks colored red is dealing with downloading files, we can put them into a single task. The sampling procedure goes for the rest. 
This is what subdag is available for. Briefly speaking, subdag allows you to create a Dag inside another dag to group your tasks. 

![image](https://user-images.githubusercontent.com/53164959/110197095-74800400-7e8c-11eb-82c1-2c27e8b70ec3.png)

## 2. Configuration 


Visit the file **_airlfow.cfg_** and find the variable called  **_load_examples_**. Change the default setting to False. 
Here, we will use the parallel_dag.py from the previous lecure as a basis. We will add some features to implement subdag. 

Firs,create a new folder named subfolders under dags and a file **_subdag_parallel_dag.py_**. In the file, we will define a function to make
a subdag. In this function, we create a new DAG by instantiating a DAG objection with  parent and child id with the default arguments equal to those already specified in the 'main' DAG.

```python
## sudag_parallel_dag.py
from airflow import DAG
from airflow.operators.bash import BashOperator

def subdag_parallel_dag(parent_dag_id,child_dag_id,default_args):
    with DAG(dag_id='{}.{}'.format(parent_dag_id,child_dag_id),default_args=default_args) as dag:
        task_2=BashOperator(
            task_id="task_2",
            bash_command="sleep 3"
        )
        
        task_3=BashOperator(
            task_id="task_3",
            bash_command="sleep 3"
        )
        
        return dag
```

Import the function we have defined to the parallel_dag.py. There is an important task to take; 

   - put 'main' DAG id to praent_id
   - put the task id of SubDagOperator to child_id

```python
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.subdag import SubDagOperator
from datetime import datetime
from subdags.subdag_parallel_dag import subdag_parallel_dag

default_args={
    'start_date':datetime(2021,3,6)
}

with DAG("parallel_dag",schedule_interval="@daily",default_args=default_args,catchup=False) as dag:
    task_1=BashOperator(
        task_id='task_1',
        bash_command='sleep 3'
    )
    
    processing=SubDagOperator(
        task_id="processing_tasks",
        subdag=subdag_parallel_dag('parallel_dag','processing_tasks',default_args)
    )
  

    task_4=BashOperator(
        task_id="task_4",
        bash_command="sleep 3"
    )

    task_1 >> processing >> task_4
    
```

### 4. Tips to Remember

In practical settings, sub-dags are not recommended at all because you will face a variety of issues related to this simple function. 


First of all,  there is a high chance of your whole system being into deadlocks to prevent all the rest tasks from running successfully. 

Secondly, it adds some complexity to the data pipelines. From the previous example, we have defined a new function and inside it created a new DAG with the same sharing arguments as the parent DAG.

Last but not least, sub-DAG has its executor independent from the 'main' DAG. Even if the configuration of airflow we set up is a local executor, the sub DAG is still abiding by sequential executor by default.







