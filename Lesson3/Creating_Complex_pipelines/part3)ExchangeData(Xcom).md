
## 1. Introduction 


It is not hard to imagine that two tasks are directly communicating with each other for sharing information. For example, let's say airflow is to implement two tasks, one of each is to deal with listing filenames from an outside source and the other to download the corresponding files.  To perform the second task, there must be a direct link between two nodes.
But the question is how to make this sharing possible?


First, we depend on an external tool such as a database or AWS S3, which acts as a repository for storing information temporarily.  Information from the preceding node is pushed to the place and the following node pulls it in next.  This approach, as we expect, unintentionally adds complexity to our data-pipelines. 

Second, Airflow suggests a better mechanism to facilitate this sharing, which is now known as **_Xcoms_**.  The way to push and pull data acts similarly, but any incoming data is now identified with a unique key. Therefore, if one node pulling information requests a key, Xcoms responds to the request to return the corresponding value in return.  

![image](https://user-images.githubusercontent.com/53164959/110237850-98714180-7f81-11eb-8aaa-713c1bf72da3.png)


But the major obstacle that we must bear with when using "xcoms" is that **_cross-communication allows exchanging of a small amount of data. Not only for this, the allowed size of data varies on the types of database you use_**. 


Xcoms allows for 2 GB of data stroage for PostGreSQL ,1 GB for Xcom , 64 KB for MySQL. For this limitation, Xcoms is not usually accompanied with frameworks like Spark or Flink. 


## 2 Case Study

:black_nib:
We are going to create a 'DAG' file that consists of three major tasks, download data, processing, and choosing the best model. Because this case study is only to understand the basic function of 'xcom',  we write a simple bash code for the first task , sleeping for 3 seconds.  On the second node, there are three training models, whose accuracy is determined by the random number in a range between 0 and 1.  Finally,  the last node is to choose the best model out of three. 


```python
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.task_group import TaskGroup
from datetime import datetime
from random import uniform
default_args={
    'start_date':datetime(2021,3,7)
}

def _training_model(ti):
    accuracy=uniform(0,10.0)
    print("model's accuracy: {}".format(accuracy))
    ti.xcom_push(key="model_accuracy",value=accuracy)


def _choose_best_model(ti):
    print("chosing the best model")
    accuracies=ti.xcom_pull(key="model_accuracy",task_ids=[
        "processing_tasks.training_model_a",
        "processing_tasks.training_model_b",
        "processing_tasks.training_model_c"
    ])
    print(accuracies)

with DAG("xcom_dag",schedule_interval="@daily",default_args=default_args,catchup=False) as dag:
    downloadingData=BashOperator(
        task_id="downloading_data",
        bash_command="sleep 3",
        do_xcom_push=False
    )

    with TaskGroup('processing_tasks') as processing_tasks:
            training_model_a = PythonOperator(
                task_id='training_model_a',
                python_callable=_training_model
            )

            training_model_b = PythonOperator(
                task_id='training_model_b',
                python_callable=_training_model
            )

            training_model_c = PythonOperator(
                task_id='training_model_c',
                python_callable=_training_model
            )

    choose_model = PythonOperator(
        task_id='task_4',
        python_callable=_choose_best_model
    )



    downloadingData >> processing_tasks >> choose_model
        
```



![image](https://user-images.githubusercontent.com/53164959/110242271-a1214200-7f98-11eb-8721-23aed34c62c9.png)





:pushpin: Considerations 

- Pay attention to type of opertors that will create xcom by default   

  Some operators will create x_com by default so you need to check out to set the arguements False if you do not want it to. 
  For more infomration on the list of operators creating xcom automatically, you should look into documentation issued by Apache Airflow. 

 
- xcom is not sutiable for big data tools incluing spark and flink. 
 
 



