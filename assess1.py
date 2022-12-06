import psycopg2

def get_db_connection():
    connection = psycopg2.connect(
            user="postgres",
            password="5731",
            host="localhost",
            port="5432",
            database="assessmentdb")
    return connection

def list_db():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM public.view_contacts")
    complete_database = cursor.fetchall()
    cursor.close()
    connection.close()
    print(complete_database)

list_db()
