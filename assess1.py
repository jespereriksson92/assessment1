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
    cursor.execute("SELECT first_name,last_name,title,organization FROM contacts")
    view = cursor.fetchall()
    cursor.close()
    connection.close()
    print(view)
#3.6
def insert_contact(first_name, last_name, title, organization):
    connection = get_db_connection()
    cursor = connection.cursor()
    insert_query = (f"INSERT INTO contacts (first_name, last_name, title, organization)VALUES ('{first_name}', '{last_name}', '{title}', '{organization}');")
    cursor.execute(insert_query)
    connection.commit()
    cursor.close()
    connection.close()
    print(f"{first_name} added!")

def insert_contact_type(contact_type):
    connection = get_db_connection()
    cursor = connection.cursor()
    insert_query = (f"INSERT INTO contact_types (contact_type) VALUES ('{contact_type}');")
    cursor.execute(insert_query)
    connection.commit()
    cursor.close()
    connection.close()
    print(f"{contact_type} added!")

def insert_contact_category(contact_category):
    connection = get_db_connection()
    cursor = connection.cursor()
    insert_query = (f"INSERT INTO contact_categories (contact_category) VALUES ('{contact_category}');")
    cursor.execute(insert_query)
    connection.commit()
    cursor.close()
    connection.close()
    print(f"{contact_category} added!")

def view_contacts_id():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT id, first_name FROM contacts")
    view = cursor.fetchall()
    cursor.close()
    connection.close()
    print(view)

def view_contact_types():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT id, contact_type FROM contact_types")
    view = cursor.fetchall()
    cursor.close()
    connection.close()
    print(view)

def view_contact_categories():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT id, contact_category FROM contact_categories")
    view = cursor.fetchall()
    cursor.close()
    connection.close()
    print(view)

def insert_items(contact,contact_id,contact_type_id,contact_category_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    insert_query = (f"INSERT INTO items (contact, contact_id, contact_type_id, contact_category_id) VALUES ('{contact}',{contact_id},{contact_type_id},{contact_category_id})")
    cursor.execute(insert_query)
    connection.commit()
    cursor.close()
    connection.close()
    print(f"Contact information added!")

#3.7
def delete_contact(first_name):
    connection = get_db_connection()
    cursor = connection.cursor()
    insert_query = (f"DELETE FROM contacts WHERE first_name = '{first_name}';")
    cursor.execute(insert_query)
    connection.commit()
    cursor.close()
    connection.close()
    print(f"{first_name} deleted! Hopefully you can be friends again someday.")

#3.5
print("Welcome! What would you like to do?")
while True:
    user_input = input("\nLIST \t See an overview of the contacts\n"
    "INSERT \t Add a new contact\nDELETE \t Remove a contact\nQUIT \t Exit the program\n"
    ":").upper()

    if user_input == 'LIST':
        print("First name, Last name, Title, Organization")
        view_contacts()
    
    elif user_input == 'INSERT':
        insert_user_input = input("Do you want to add a CONTACT, a CONTACT TYPE, CONTACT CATEGORY, or CONTACT INFORMATION?\n:")
        if insert_user_input == 'CONTACT':
            first_name_input = input("What is the first name of the person?\n: ")
            last_name_input = input("What is the last name of the person?\n: ")
            title_input = input("Give a title to this person, e.g. brother, mortal enemy?\n: ")
            organization_input = input("Does this person belong to a certain organization?\n: ")
            insert_contact(first_name_input,last_name_input,title_input,organization_input)

        elif insert_user_input == 'CONTACT TYPE':
            contact_type_input = input ("What kind of contact type do you wish to add?\n:")
            insert_contact_type(contact_type_input)

        elif insert_user_input == 'CONTACT CATEGORY':
            category_input = input("What kind of contact category do you want to add?\n:")
            insert_contact_category(category_input)

        elif insert_user_input == 'CONTACT INFORMATION':
            print("These persons exists in your contact list:")
            view_contacts_id()
            id_contact_insert = int(input("Type the ID of who you want to add contact information to.\n: "))
            contact_insert = input("Type the contact information, e.g. email, phonenumber.\n:")
            print("These are the contact types that exist:")
            view_contact_types()
            contact_type_insert = int(input("What kind of contact type is it you added? Type the ID."))
            print("These are the contact categories that exists:")
            view_contact_categories()
            contact_category_insert = int(input("To what kind of category does this belong to? Type the ID."))
            insert_items(contact_insert,id_contact_insert,contact_type_insert,contact_type_insert)

        else:
            print("Invalid input!")
    
    elif user_input == 'DELETE':
        deletion_input = input("What is the first name of the contact you wish to delete?\n"
        "Very convenient for me, your contact application, that you don't know anyone who shares the same name...\n:")
        delete_contact(deletion_input)

    elif user_input == 'QUIT':
        print("Bye!")
        exit()
        
    else:
        print("Invalid input!")