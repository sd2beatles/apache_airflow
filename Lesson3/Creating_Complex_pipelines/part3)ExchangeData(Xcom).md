
## 1. Introduction 


It is not hard to imagine that two tasks are directly communicating with each other for sharing information. For example, let's say airflow is to implement two tasks, one of each is to deal with listing filenames from an outside source and the other to download the corresponding files.  To perform the second task, there must be a direct link between two nodes.
But the question is how to make this sharing possible?


First, we depend on an external tool such as a database or AWS S3, which acts as a repository for storing information temporarily.  Information from the preceding node is pushed to the place and the following node pulls it in next.  This approach, as we expect, unintentionally adds complexity to our data-pipelines. 

Second, Airflow suggests a better mechanism to facilitate this sharing, which is now known as **_Xcoms_**.  The way to push and pull data acts similarly, but any incoming data is now identified with a unique key. Therefore, if one node pulling information requests a key, Xcoms responds to the request to return the corresponding value in return.  

![image](https://user-images.githubusercontent.com/53164959/110237850-98714180-7f81-11eb-8aaa-713c1bf72da3.png)


But the major obstacle that we must bear with when using "xcoms" is that **_cross-communication allows exchanging of a small amount of data. Not only for this, the allowed size of data varies on the types of database you use_**. 


Xcoms allows for 2 GB of data stroage for PostGreSQL ,1 GB for Xcom , 64 KB for MySQL. For this limitation, Xcoms is not usually accompanied with frameworks like Spark or Flink. 
