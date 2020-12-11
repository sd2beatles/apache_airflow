# Celery Executor with MySQL and RabbitMQ

### 1.What is RabbitMQ

RabbitMQ is an open source message borker software whose role is similar to a middleman accepting messages from producers and delivering them to consumers. 
Let's say we have a producer like a logging system producing a different level of logs such as bindings,warnings,and error in our case. 
Now,we specify three bindings,one for each bidning directed to the corresponding queue. Finally,each consumer is now waiting to receive the log messages coming from its queue.

![image](https://user-images.githubusercontent.com/53164959/101946422-4d6db980-3c32-11eb-9c55-422c6d4d31d6.png)

### 2. Celery Executor

CeleryExecutor is one of the ways you can scale out the number of workers. For this to work, you need to setup a Celery backend (RabbitMQ, Redis, …) and 
change your airflow.cfg to point the executor parameter to CeleryExecutor and provide the related Celery settings.


Now RabbitMQ as a celery backend is now running in the node 2 and waiting to receive a task as shown in the diagram below. workers are currently in node 4 and 5,respectively.
Let's begin with the first task. It is fetched to node 3 and RabbiMQ sends it to queue. Since all workers are fee to use, it is now delivered and executed right away in node 4.
Since the number of co_current workers is 2 and that of parallel is also 2, up to 4 tasks can be excuted in a parallel. By providing the related celery settings, we can make more
tasks executed simultaenously. 

![image](https://user-images.githubusercontent.com/53164959/101950947-7fcee500-3c39-11eb-8cd2-4d0bb0f7de1d.png)


### 3. Import Notes

- Dependencies installed on all workers 

Kowing that different tasks are executed on different machines, involved cores need dependencies required by the tasks they execute. For example, if a task relies on Spark and 
spark is not available on a given node and you will encounter a fauilre of execution. Therfore, the success of its system requires that all the dependencies be installed on al the nodes
of your cluster.

- DAG must be in sync.

If one of your node has a older version of DAG, you are more likely to get an inconsistency in your result or even an error. 

- Homogeneous configuration settins on all the worker nodes. 

### 4. Pros and Cons of The Celery Executor

- Third parties(Queue,Dependency managers) must be set up to make the executor run. This leads to the complexity of your architecures as well as the learning curve of your co-workers

- Workers must be in sync which implies that the same configuration settings and dependencies are required on all the nodes.

-Horizontal Scaliability. Scaling out the number of workers will incrase the nubmer of tasks to process. The time of task completion will decrease accordingly. 

- The celery executor is widely used in production and proven to be reliable. 









