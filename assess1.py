import psycopg2

def get_db_connection():
    connection = psycopg2.connect(
            user="postgres",
            password="5731",
            host="localhost",
            port="5432",
            database="assessmentdb")
    return connection

