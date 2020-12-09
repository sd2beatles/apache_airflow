![image](https://user-images.githubusercontent.com/53164959/99251405-a3785880-2850-11eb-8343-9739679ce315.png)


# 1. Quick Review

Apache airflow readily works in a distributed environment. Each task is scheduled according to dependencies defined into DAG and the workers pick up and run thier jobs with thier load balanced for performance optimization. We have another machine called metadata database where all information is stored and is updated regularly.  

![image](https://user-images.githubusercontent.com/53164959/101675835-a9eba000-3a9d-11eb-99b1-7becd100f4d2.png)

# 2. SQLite 

- SQLite is a default executor in apache airflow and is known a s a relation databse

- SQLite is ACID-compliant(Atomicity,Consistency,Ioslation,Durability)   
  - Atomicity : 
    Atomicity implies that we only possibly get all trasactions succeed or none of it succeed. What it means that obtainig part of it suceeding and of it not is impossible.
  
  -Consistency:
   All data is valid as long as trascations follow the specified rules applied on the database
   
   -Isolation:
   Isolation ensures that all transaction is running in isolation,which indicates no trascation possibly gain data from another that has not yet completed
   
   -Durability:
   Once a transaction is commiteed, it will remain in the system even if a system crash follows the transaction. Any changes from the trasncation mustbe stored permanently. 
   
-SQLite requires no configuration to run. 

-It supports an unlimited number of simulataneous readers, but only one writer at any instant in time

-Limited in size up to 140TB and the entire database is stored into a single disk file. 



