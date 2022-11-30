from datetime import datetime

from airflow import DAG
from airflow.decorators import task
from airflow.operators.trigger_dagrun import TriggerDagRunOperator

with DAG('calldag', description='BlogExampleFinTechExplained',
          schedule_interval='0 */2 * * *',
          start_date=datetime(2022, 11, 29), catchup=False) as dag:
    @task
    def start():
        print('start')


    trigger_pass_data = TriggerDagRunOperator(
        task_id="trigger_run",
        trigger_dag_id="passdata",
        dag=dag,
    )

    start() >> trigger_pass_data