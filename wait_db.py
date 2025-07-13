import time
import psycopg2
from psycopg2 import OperationalError
import os

def wait_for_db():
    db_host = os.environ.get("DB_HOST", "db")
    db_port = os.environ.get("DB_PORT", "5432")
    db_name = os.environ.get("DB_NAME", "meetwise")
    db_user = os.environ.get("DB_USER", "meetwise_user")
    db_password = os.environ.get("DB_PASSWORD", "meetwise_pass")

    while True:
        try:
            conn = psycopg2.connect(
                host=db_host,
                port=db_port,
                dbname=db_name,
                user=db_user,
                password=db_password,
            )
            conn.close()
            print("Database is up!")
            break
        except OperationalError:
            print("Database not ready, waiting 2 seconds...")
            time.sleep(2)

if __name__ == "__main__":
    wait_for_db()
