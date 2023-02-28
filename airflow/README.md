# airflow

### pre task before start project
- create airflow user on xspector postgres
```
CREATE DATABASE airflow;
CREATE USER airflow WITH ENCRYPTED PASSWORD 'airflow';
GRANT ALL PRIVILEGES ON DATABASE airflow TO airflow;
```

### how to start project
1. run migrate airflow database `docker compose up airflow-init`
2. start airflow stack `docker compose up -d`
3. stack will generate dags, logs and plugins directories

### note
- if you got error permission denide directory dags, logs and plugins, you need to specify user to run airflow stack by command `echo -e "AIRFLOW_UID=$(id -u)" > .env`
