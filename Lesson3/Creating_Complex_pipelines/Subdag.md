## 1. Introduction 

Just imagine that you have data pipelines that consist of three major tasks; downloading, checking f, and processing files with the dependencies. 

 ![image](https://user-images.githubusercontent.com/53164959/110196897-fff89580-7e8a-11eb-9548-1516ddfa65b9.png)

But our question here is "is there any feasible way to group tasks according to thier functionality and roles?"  For example, Because all the first tasks colored red is dealing with downloading files, we can put them into a single task. The sampling procedure goes for the rest. 
This is what subdag is available for. Briefly speaking, subdag allows you to create a Dag inside another dag to group your tasks. 

![image](https://user-images.githubusercontent.com/53164959/110197095-74800400-7e8c-11eb-82c1-2c27e8b70ec3.png)

## 2. Configuration 


Visit the file **_airlfow.cfg_** and find the variable called  **_load_examples_**. Change the default setting to False. 
Here, we will use the parallel.py from the previous lecure as a basis. We will add some features to implement subdag. 

```python




```
One noticeable difference from the last code is that we add SubDagOperator with tak_id set to "processing tasks".  We have to have one more task to do, creating a function to return the subdag. 

Firs,create a new folder named subfolders under dags and a file **_subdag_parallel_dag.py_**. In the file, we will define a function to make
a subdag. In this function, we create a new DAG by instantiating a DAG objection with  parent and child id with the default arguments equal to those already specified in the 'main' DAG.

```python





