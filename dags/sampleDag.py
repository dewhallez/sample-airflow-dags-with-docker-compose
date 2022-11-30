import os
from datetime import datetime
import requests
from airflow import DAG
from airflow.decorators import task
from airflow.operators.python import PythonOperator
import logging
with DAG('test', description='BlogExampleFinTechExplained',
          schedule_interval='0 */2 * * *',
          start_date=datetime(2022, 11, 29), catchup=False) as dag:
    @task
    def start():
        pass
    @task
    def do_first_task():
        pass
    @task
    def do_second_task():
        pass
    @task
    def do_third_task_with_second_task():
        pass
    @task
    def do_forth_task():
        pass
    @task
    def goodbye_link_to_all():
        pass
    start() >> do_first_task() >> [do_second_task(), do_third_task_with_second_task()]
    list(dag.tasks) >> goodbye_link_to_all()