![image](https://user-images.githubusercontent.com/53164959/99251405-a3785880-2850-11eb-8343-9739679ce315.png)

# 1.A quick Reminder
## 1.1 Quick Review

Apache airflow readily works in a distributed environment. Each task is scheduled according to dependencies defined into DAG and the workers pick up and run thier jobs with thier load balanced for performance optimization. We have another machine called metadata database where all information is stored and is updated regularly.  

![image](https://user-images.githubusercontent.com/53164959/101675835-a9eba000-3a9d-11eb-99b1-7becd100f4d2.png)

## 1.2 SQLite 

- SQLite is a default executor in apache airflow and is known a s a relation databse

- SQLite is ACID-compliant(Atomicity,Consistency,Ioslation,Durability)   
  - Atomicity : 
    Atomicity implies that we only possibly get all trasactions succeed or none of it succeed. What it means that obtainig part of it suceeding and of it not is impossible.
  
  - Consistency:
   All data is valid as long as trascations follow the specified rules applied on the database
   
   - Isolation:
   Isolation ensures that all transaction is running in isolation,which indicates no trascation possibly gain data from another that has not yet completed
   
   - Durability:
   Once a transaction is commiteed, it will remain in the system even if a system crash follows the transaction. Any changes from the trasncation mustbe stored permanently. 
   
- SQLite requires no configuration to run. 

- It supports an unlimited number of simulataneous readers, but only one writer at any instant in time

- Limited in size up to 140TB and the entire database is stored into a single disk file. 


## 1.3 Concurrency VS Parallelism

It is believed that Concurrency and parallelism are the terminologies that are used interchangeably. However, the mechanism behind each structure type is quite different.

Concurrency is when one or more tasks start and run, and complete in the overlapping time period. Let's assume that we have two tasks in a single machine. It begins with task1 and spends some time completing part of it and switch to the other, performing it, and back to task1 again. This process will repeat over and over until the tasks are complete. 

On the other hand, Parallelism is when tasks literally run at the same time.
Two task are being performed on two different machies. 

![image](https://user-images.githubusercontent.com/53164959/101834063-2e612000-3b7d-11eb-9b0b-e637c2ff3122.png)


# 2. Introduction of Executor

## 2.1 Definition

An Executor is fundamentally a mssage queque process which determines the worker process that executes each scheduled task.
The major types of executors are as follows:
 - Sequential Executor
 - Local Executor
 
## 2.2  Sequential Executor 

- Sequetial Executor is said to be the most fundamental executor to use. 
- The most distinct feaure is to allow only one task at a time,which is useful for debugging
- It is only excutor that can compatible with SQLite, which as previously mentioned does not support multiple writers.
- It is the default executor that you run Apcahe airflow for the first time.
- There is no paralelism and/or concurrency 


## 2.2 Local Executor 

- Local Executor runs task by spwaning processess in a controlled in different modes
- Setting the parallelism parameters to be zero(self.parallelism=0), the number of processes that the local executor spawn is unlimited 
- When the parallelismparametes to be one(ie self.parallelism=1), it beahves exacthly the same as the sequal executor does




# 3. Configuration Files

![image](https://user-images.githubusercontent.com/53164959/101833187-f0afc780-3b7b-11eb-9529-2f6b569aed96.png)


![image](https://user-images.githubusercontent.com/53164959/101834160-52246600-3b7d-11eb-98fb-9668adcb10fc.png)





