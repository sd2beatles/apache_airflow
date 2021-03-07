## 1. Introduction 

If you want to go down a certain path depending on the arbitrary condition which is typically associated with some past events in an upstream task. One way to realize this is by using BrachPythonOperator.


For example,  from the first task, we compute the level of accuracy based on some function. If the computed value is greater than  5 as a threshold, go to the task node called 'accuracy'. Otherwise, the next node it will flow to is  'inaccuracy'. Execution of code is highly related to the value from the preceding node. 




## 2. Code

### :pushpin: Task 
If any of the training models return accuracy greater than your arbitrary threshold, it flows to the **_accurate_** path or the **_inaccurate_**  if not.


First, let's make two dummay operators,one for accurate and the other for inaccurate. Remind you that DummyOperat is as the name implies an
operator used in running your own experimenets withouth storing data in the database.

```python


    accurate=DummyOperator(
        task_id="accurate"
    )

    inaccurate=DummyOperator(
        task_id="inaccurate"
    )

       


```

modify the 'choose_model' variable by changing its operator to BranchPythonOperator. 

```python
 choose_model =BranchPythonOperator(
        task_id='task_4',
        python_callable=_choose_best_model
    )

```
Go back to the function our operator will call and
make iteration over the accuracies of xcom.pulls and if the condition is met, return "accurate". Otherwise, return "inaccurate". You may wonder why we should return the id this time.
According to documenation, it states as follows 

**_The BranchPythonOperator is much like the PythonOperator except that it expects a python_callable that returns a task_id (or list of task_ids). The task_id returned is followed, and all of the other paths are skipped. 
The task_id returned by the Python function has to be referencing a task directly downstream from the BranchPythonOperator task._**


```python
def _choose_best_model(ti):
    print("chosing the best model")
    accuracies=ti.xcom_pull(key="model_accuracy",task_ids=[
        "processing_tasks.training_model_a",
        "processing_tasks.training_model_b",
        "processing_tasks.training_model_c"
    ])
    for accuracy in accuracies:
        if accuracy>5:
            return 'accurate'
    return 'inaccurate'
```

Lastly, we will make another taks called "storing". 

```python
   
   storing=DummyOperator(
        task_id="storing"
    )
```


The overall code for encompassing all the modificaitons in the previous stpes is shown below


```python



```

