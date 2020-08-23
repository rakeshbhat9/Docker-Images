from airflow.models.dag import ScheduleInterval
from project_1.scripts.python_test_logic import get_data
from airflow.utils.dates import days_ago
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import  BashOperator

args = {
    'owner': 'Airflow',
    'start_date': days_ago(3),
    'ScheduleInterval': '0 * * * *'
    # 'email': ['rakeshbhat9@gmail.com'],
    # 'email_on_failure': True
}

dag = DAG(
    dag_id='python_test',
    default_args=args,
    tags=['example']
)

run_this = BashOperator(
    task_id='task_1',
    bash_command='echo About to run python operator..',
    dag=dag,
)

run_this_as_well = PythonOperator(
    task_id='task_2',
    python_callable=get_data,
    dag=dag,
)

run_this >> run_this_as_well