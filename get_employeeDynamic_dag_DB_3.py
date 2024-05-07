from airflow import DAG
from datetime import datetime
from airflow.providers.postgres.operators.postgres import PostgresOperator

with DAG("get_employees_Dynamic_dag_DB_3", start_date = datetime(2024,3,1), schedule_interval = "*/10 * * * *", catchup = False) as dag:
    run_sql_stmt = PostgresOperator(
        task_id="check_table",
        postgres_conn_id="connect_dest_database",  
        sql="select * from api;"
    )

    run_sql_stmt