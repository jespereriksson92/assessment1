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
#3.6
def add_contact(first_name, last_name, title, organization):
    connection = get_db_connection()
    cursor = connection.cursor()
    insert_query = (f"INSERT INTO contacts (first_name, last_name, title, organization)VALUES ('{first_name}', '{last_name}', '{title}', '{organization}');")
    cursor.execute(insert_query)
    connection.commit()
    cursor.close()
    connection.close()
    print(f"{first_name} added!")

#3.5
print("Welcome! What would you like to do?")
while True:
    user_input = input("\nLIST \t See an overview of the contacts\n"
    "INSERT \t Add a new contact\nDELETE \t Remove a contact\nQUIT \t Exit the program\n"
    ":").upper()
    if user_input == 'LIST':
        view_contacts()
    elif user_input == 'INSERT':
        first_name_input = input("What is the first name of the person? ")
        last_name_input = input("What is the last name of the person? ")
        title_input = input("Give a title to this person, e.g. brother, mortal enemy? ")
        organization_input = input("Does this person belong to a certain organization? ")
        add_contact(first_name_input,last_name_input,title_input,organization_input)
    elif user_input == 'DELETE':
        print()
    elif user_input == 'QUIT':
        exit()
    else:
        print("Invalid input!")