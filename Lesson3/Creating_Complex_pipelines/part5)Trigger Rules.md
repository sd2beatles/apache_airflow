![image](https://user-images.githubusercontent.com/53164959/110245241-ac2e9f00-7fa5-11eb-9464-b3f47841a8fe.png)


## 1. Introduction 

The normal workflow behavior is to trigger the following task if all directly upstream tasks have succeeded. That is why our previous case study has skipped over the final task.  Thanks to the allowance of 9 trigger rules, we can trigger the following task depending on our disposal. 

The triggers rules are as follows 

![image](https://user-images.githubusercontent.com/53164959/110245234-a33dcd80-7fa5-11eb-8152-9c10a9973889.png)


## 2. Modifying the previous code 


 It is tiem to select a proper rule for **_trigger_rule_** arguement. As for our case, none of our parent tasks has failed but one of them has succeedAs for our case, none of our parent tasks has failed but one of them has succeeded, which is perfectly compatible with the rule, 'none_failed_or_skipped'. 
 
```python

    storing=DummyOperator(
        task_id="storing",
        trigger_rule="none_failed_or_skipped"

    )

```

Now, we can see that the problem has solved. 

![image](https://user-images.githubusercontent.com/53164959/110247123-f87ddd00-7fad-11eb-9a8a-fc0440d40309.png)




