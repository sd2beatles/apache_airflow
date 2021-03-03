

### 1. Airflow At Scale

The higher number of tasks are executed, the greater burden our single machine has in the process. At some point, the single machine alone can not carry out all the tasks 
by itself and it seems to be inevitable to add more executors to our cluster for optimizing the prerformance level of handing tasks. 

In Airflow, we have many executors responsible for scaling out the number of workers,one of which is celery executor introduced in the lecture.


### 2. Introduction of The Celery Executor

Celery Executor is a distributed task system, whose major role is to spread out given tasks among multiple machines. In

To closely examine how the celery executor works, we first need to understand the flow of data to each worker.  In our chart below,  two fundamental systems, web server and scheduler, 
are currently running in node 1 with the metadatabase such as MySQL or PostgreSQL on node 2. Every task incoming into the system first is temporarily stored in the queue until airflow gets ready to execute it.  
Especially, you need to be alert that the queue is not located inside the executor but outside of it.  This is where Redis comes to our attention.  Now, we need to introduce the new terminology called Redis which is defined as an in-memory database to be used as a queue system.  While tasks are waiting in the Redist to be executed, it is workers or machines that pull out the task to execute them.  One last terminology we are familiar with is  worker_concurreny which tells us the maximum number of tasks allowed to be executed within each worker.For example, if you set worker_concurrency equal to 2 for every node and have two nodes, the total 4 tasks can be done in parallel.


With use of the flow chart, let's begin with the first task. It is fetched to node 3, waiting in the queue. Since all workers are free to use, it is now delivered and executed right away in node 4. With more tasks entering and stored in the queue, up to 4 tasks can be executed in a parallel since 
the number of co_current workers sets to be 2 and that of parallel is also 2. By providing the related celery settings, we can make more
tasks executed simultaneously. 



![image](https://user-images.githubusercontent.com/53164959/101950947-7fcee500-3c39-11eb-8cd2-4d0bb0f7de1d.png)

