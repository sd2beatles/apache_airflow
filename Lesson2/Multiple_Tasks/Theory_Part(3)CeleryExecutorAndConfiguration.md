:warning: Stop all the airflow webserver and scheduler before setting configuraiton

### 1. Install apache-airflow Celery and Redis

Installration is pretty much simple and  you can simply follow the codes below

For installation of celery executors,

```linux
pip install 'apache-airflow[celery]'
```

For rebis,

```linux
sudo apt install redis-server
```
After installation finishes successfully, open a file named redis.config in your chosen editor. 

```linux
sudo vim /etc/redis/redis.conf
```
Now, if you land on the configuration file of redis, serach **_supervised no**_ and change it to **_supervised systemd_**
Exit the file and write two lines of codes in your terminal and you will see a message.

```linux
sudo systemctl restart redis.service
sudo systemctl status redis.service

````

![image](https://user-images.githubusercontent.com/53164959/109773615-c2a1c700-7c42-11eb-84b2-6560bee51201.png)


