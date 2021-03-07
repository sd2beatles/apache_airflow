## 1. Taskgrouop

In this short and simple lecture, we are going to introduce the use of **_task_grouop_** instead to perfectly substitute for the SubDAG.


## 2. Code

```python

from airflow.utils.task_group import TaskGroup

with TaskGroup("processing_tasks") as processing_tasks:
        task_2=BashOperator(
            task_id="task_2",
            bash_command="sleep 3"
        )    
        
        task_3=BashOperator(
            task_id="task_3",
            bash_command="sleep 3"
        )
    

    task_4=BashOperator(
        task_id="task_4",
        bash_command="sleep 3"
    )

```
As you can see from the above code,  you will soon realize thtat there is no burden to instantiate a new dag and define a function inside it by setting arguments equal to those in the main DAG. The deprecation of SUBDAG is belived to be upcoming soon. 

![image](https://user-images.githubusercontent.com/53164959/110235245-4ffe5780-7f72-11eb-887e-9eedbedf80e6.png)


## 3. Key point 

We are told that within DAG the same task_id may cause conflict to cease the whole program. What about if you grant the same id to  the one in the 
'main' DAG and in TaskGroup, respectively? Does it still give us a pause in running data-pipelines. The answer is "no". 

**_By default, any id defined under TaskGroup is prefixed with the group_id._** 
Hence, even if we set the task_id "task_3" in our code, the full name for the task_id Airflow will understand is "processing_tasks.task_3". 




