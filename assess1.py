import psycopg2
#3.3
def get_db_connection():
    connection = psycopg2.connect(
            user="postgres",
            password="5731",
            host="localhost",
            port="5432",
            database="assessmentdb")
    return connection

#3.4
def view_contacts():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM public.view_contacts")
    view = cursor.fetchall()
    cursor.close()
    connection.close()
    print(view)
print("Welcome! What would you like to do?")
while True:
    user_input = input("\nLIST \t See an overview of the contacts\n"
    "INSERT \t Add a new contact\nDELETE \t Remove a contact\nQUIT \t Exit the program\n"
    ":").upper()
    if user_input == 'LIST':
        view_contacts()
    elif user_input == 'INSERT':
        print()
    elif user_input == 'DELETE':
        print()
    elif user_input == 'QUIT':
        exit()
    else:
        print("Invalid input!")