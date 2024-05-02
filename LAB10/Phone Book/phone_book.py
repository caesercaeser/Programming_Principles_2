import psycopg2
import csv
from prettytable import from_db_cursor

connection = None

try:
    #connect
    connection = psycopg2.connect(
        host = "127.0.0.1",
        user = "postgres",
        password = "123456",
        dbname = "postgres"
    )

    connection.autocommit = True

    #table creation
    with connection.cursor() as cursor:
        cursor.execute(
            '''CREATE TABLE IF NOT EXISTS phone_book(
                id serial PRIMARY KEY,
                name varchar(50) UNIQUE NOT NULL,
                phone_number varchar(50) NOT NULL
            );'''
        )

        print('[INFO] Now using created table!')

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         'DROP TABLE phone_book;'
    #     )

    #     print('[INFO] Successfully dropped')

    #getting input from user
    while True:
        checking = input('[INFO] For console input type "c", for CSV file input type "f", for update already existing data type "u", to show table type "s" and to quit type "q": ')
        
        if checking == 'q':
            break
        
        try:
            #if user input is redundant for our code
            if len(checking) != 1 or checking not in ['c', 'f', 'u', 's']:
                raise ValueError('[INFO] Enter exactly one letter ("c" , "f", "u" or "s"), or "q" to quit.')
            
            #update existing data method (record)
            elif checking == 'u':
                checu = input('[INFO] To update record type "r", to delete record type "d" or type "q" to quit: ')
                if checu == 'q':
                    break
                elif len(checking) != 1 or checking not in ['c', 'f', 'u', 's']:
                    raise ValueError('[INFO] Enter exactly one letter ("r" or "d"), or "q" to quit.')
                
                if checu == 'r':
                    while True:
                        name_to_update = input('[INFO] Enter a name of contact to update or "q" to quit: ')
                        if name_to_update == 'q': break

                        typeof = input('[INFO] Enter what field of contact to update (type "name" or "phone_number" to choose) or "q" to quit: ')
                        if typeof == 'q': break

                        elif typeof not in ['name', 'phone_number']:
                            print('[INFO] Invalid field request. Please, enter "name" or "phone_number".')
                            continue

                        new_value = input('Enter new value in place of past record: ')

                        try:
                            with connection.cursor() as cursor:
                                #checking if contact to update exists
                                cursor.execute(
                                    "SELECT name FROM phone_book WHERE name = %s",
                                    (name_to_update,)
                                )
                                exists_contact = cursor.fetchone()
                                if exists_contact is None:
                                    print(f"[INFO] There is no contact named {name_to_update}")
                                    break

                                #checking if new value for name of contact is already in the table (must be unique)
                                cursor.execute(
                                    "SELECT name FROM phone_book where name = %s",
                                    (new_value,)
                                )
                                exists_name = cursor.fetchone()
                                if exists_name:
                                    print("Pick another name. The name you have entered already exists.")
                                    break
                        
                                if typeof == 'name':
                                    cursor.execute(
                                        "UPDATE phone_book SET name = %s WHERE name = %s",
                                        (new_value, name_to_update)
                                    )
                                else:
                                    cursor.execute(
                                        "UPDATE phone_book SET phone_number = %s WHERE name = %s",
                                        (new_value, name_to_update)
                                    )
                                print(f"[INFO] Record for {name_to_update} updated successfully!")
                        except:
                            connection.rollback()
                            print('[INFO] Error occured when updating record.')
                
                else:
                    while True:
                        name_to_update = input('Enter a name of contact to delete or "q" to quit: ')
                        if name_to_update == 'q': break

                        with connection.cursor() as cursor:
                            cursor.execute("SELECT name FROM phone_book")
                            contacts = [row[0] for row in cursor.fetchall()]  
                            if name_to_update not in contacts:
                                print('[INFO] Contact not found.')
                                continue

                        try:
                            with connection.cursor() as cursor:
                                cursor.execute("DELETE FROM phone_book WHERE name = %s", (name_to_update,))

                            print(f'[INFO] Record for {name_to_update} deleted successfully!')
                        except:
                            connection.rollback()
                            print('[INFO] Error occured when deleting data.')
                        
                    
            #console method of inserting data (record)
            elif checking == 'c':
                print("Console input selected.")
                while True:
                    name = str(input('Enter name of a contact or "q" to quit: '))
                    if name == 'q': break
                    phone_number = str(input('Enter phone number of a contact or "q" to quit: '))
                    if phone_number == 'q': break
                        
                    with connection.cursor() as cursor:
                        try:
                            cursor.execute(
                                "INSERT INTO phone_book (name, phone_number) VALUES (%s, %s)",
                                (name, phone_number)
                            )
                            print('[INFO] Record inserted successfully.')
                        except:
                            connection.rollback()
                            print('[INFO] Error occured when inserting values.')

            #csv file method of inserting data (record)
            elif checking == 'f':
                print('[INFO] CSV file input selected.')
                inserted_records = []

                #getting all data from csv file as dictionary
                with open('C:\labs\code\LAB10\Phone Book\data.csv', 'r') as file:
                    for row in csv.DictReader(file):
                        name = row['name']
                        phone_number = row['phone_number']
                        try:
                            with connection.cursor() as cursor:
                                cursor.execute(
                                    "INSERT INTO phone_book (name, phone_number) VALUES (%s, %s)",
                                    (name, phone_number)
                                )
                                inserted_records.append((name, phone_number))
                                print(f'[INFO] Record inserted successfully: {name}, {phone_number}')
                        except:
                            connection.rollback()
                            print('[INFO] Error occured when inserting values.')
            
            #table query
            elif checking == 's':
                print('[INFO] Table viewing selected')

                checq = input('To show all data type "a", to show all contact names type "b", to show all contact numbers type "c", or type "q" to quit: ')
                if checq == 'q':
                    break
                elif len(checking) != 1 or checking not in ['a', 'b', 'c']:
                    print('Enter exactly one letter ("a", "b", "c"), or "q" to quit.')
                
                if checq == 'a':
                    with connection.cursor() as cursor:
                        cursor.execute("SELECT * FROM phone_book")
                        print(from_db_cursor(cursor))

                elif checq == 'b':
                    with connection.cursor() as cursor:
                        cursor.execute("SELECT name FROM phone_book")
                        print(from_db_cursor(cursor))

                elif checq == 'c':
                    with connection.cursor() as cursor:
                        cursor.execute("SELECT phone_number FROM phone_book")
                        print(from_db_cursor(cursor))
        except ValueError:
            print(ValueError)
        
        

except:
    print('[INFO] Error while working with PostgreSQL')

finally:
    if connection:
        connection.close()
        print('[INFO] PostgreSQL connection is ended')