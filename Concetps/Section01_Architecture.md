
# Apache_Airflow 



## Section 1. Theory

### 1. Architecure Overviews(Single Node)


![image](https://user-images.githubusercontent.com/53164959/99043269-70746180-25d1-11eb-8a44-1afcb64b3b12.png)

Airflow consists of five components in a single node mode, which are as follows:


- Web Server :
   The server is used for the user interface. 

- Scheduler :
    The component is responsible for triggering your task at the right time

- Executor:
   The part is commonly playing a role to define how tasks should be       	  	   	
    implemented. 

- Metadatabase:
This huge database is a place to store all the metadata related to your DAGs.

- Worker:
This component is simply defined as a subprocess to execute your task.

### 2. The Extension to Cluster Mode(Multi Nodes)

![image](https://user-images.githubusercontent.com/53164959/99045672-0e1d6000-25d5-11eb-9b14-6d657aa97a73.png)

An executor,no matter what type it is, always has a queue where the assigned tasks are moved into it to execute them. This queue
becomes external and should be managed independently by using a solution like RabbitMQ or Redis. The key to remember here is that 
all the executors carry a queuing system. 


Let's first extract the queue from the executor to show you what is going on during the running process of a DAG.
There are some of distinct features we may find curious and intereseting. 

First, as for a single node,it is a custom to keep the web server and the scheduler on the same node,therby preventing one metadatabase from lossing everything
if the node holoding it crashes. 

Second,there components which are shown to be aligned next to one anther in our diagram work togeher by excahing data through the metadatabse
       If we extend our range of the scope to the cluster mode, the major difference  is that you have
       a master node with a web server stting on the same node with a scheduler whereas the metadatabse is running on its own . On top of that, 
       your assigned taks are to be executed on multiple worker nodes since the workload is now distributed across the worker nodes, which
       allows you scale up Airflow to fit with your needs. 
       
    
Third, the queing system in the multiple nodes are somehow different because it is located on another node and totally independent. 
      
### 3. How Your Work Get Done?

First, the scheduler reads a DAG folder to see if there is any python file corresponding to a DAG. Once it checks out the presence of a DAG and 
trigger it immediately, a DAGRun object is now created based on the scheduling parameters. The DAGRun is nothing more than an instance of your
DAG with the state set to "running" if scheulder interval is exceeded. 

![image](https://user-images.githubusercontent.com/53164959/99047168-255d4d00-25d7-11eb-9893-becc6ddce927.png)


Second, right after the first stage is running smoothly, a task instance is instantiated for each task that needs executing and flagging to 
"scheduled".

![image](https://user-images.githubusercontent.com/53164959/99047354-71a88d00-25d7-11eb-9ea0-74d9664c8c8a.png)

Next, the scheduler picks taks instances according to its priority and sets the state of them to "queue", sending them to the executor to be triggered.

![image](https://user-images.githubusercontent.com/53164959/99047708-eda2d500-25d7-11eb-8bb4-dc209ce93e1f.png)

Now, the executor pulls the task from its queque and changes the state of the taskInstance from "Queued" to "Running". Once the status changes,
the subprocess starts to process the task instances. When the task finishes, the DAGRun is updated by the scheduler with stating either "sucess" or "failed".
Of Course, during this process, the web servers periodically fetches data frin the metadata base in order to update UI.

![image](https://user-images.githubusercontent.com/53164959/99047986-55592000-25d8-11eb-840f-8fd8935b33b5.png)


### 4. Sum Up

![image](https://user-images.githubusercontent.com/53164959/99048464-ee883680-25d8-11eb-8d56-af71a9bfda4f.png)

