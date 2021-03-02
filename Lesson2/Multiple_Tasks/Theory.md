### 1. Objectives 

:point_right: Here is a list of questions we should answer after the lecture. 

- How to configure Airflow for executing multiple tasks?

- What are the important prameters to know?

- What are the different executors for scaling Airflow?


### 2. Default Mode 


![image](https://user-images.githubusercontent.com/53164959/109650883-312e4880-7ba1-11eb-8452-5aa0795313a1.png)

Let's briefly talk about how the airflow configuration runs by default. If you look at the diagram of the flow chart, it is not hard to see that the first task will be executed foremost. The real issue here is what is the next task the apache airflow performs? Since task 2 and task 3 are on the same level, it looks reasonable to say that two tasks are to be performed in parallel.  This is not true under the default configuration of airflow. 

"The default configuration only allows for sequential mode, which means that tasks will be performed one after another."

Therfore, we need to change the current mode by wirting a code below. 

```linux
airflow config 

```


