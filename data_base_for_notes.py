
import menu
import controller
import sqlite3
from sqlite3 import Error



# def sql_connection():
#     try:
#         sqlite3_connection = sqlite3.connect("Notes.db")
#         print("Connected with SQLite...")
#         return sqlite3_connection
#     except Error:
#         print(Error)

# def create_sql_table():
#     connect = sql_connection()
#     cursor = connect.cursor()
#     data = cursor.execute("select count(*) from sqlite_master where type='table' and name='All_notes'")
#     for row in data:
#         if [row] == 0:
#             cursor.execute("CREATE TABLE All_notes(id integer PRIMARY KEY, Title_of_note text, Body_of_note text, date_time datetime)")
#         else:
#             print("The table alredy exists!...")
#             connect.commit()


def insert_new_note_in_table(dev_id, Title_of_note, Body_of_note, date_time):
    try:
        connect = sqlite3.connect("Notes.db")
        cursor = connect.cursor()

        insert_with_param = "INSERT INTO All_notes(id, Title_of_note, Body_of_note, date_time) VALUES (?,?,?,?);"
        data_tuple = (dev_id, Title_of_note, Body_of_note, date_time)
        cursor.execute(insert_with_param,data_tuple)
        connect.commit()
        print("Data is successfully saved in table")

        cursor.close()
    except sqlite3.Error as error:
        print ("Error when working with the table!", error)
    finally:
        if connect:
            connect.close()
            # print ("Connection with BD is closed.")



def read_all_notes():
    try:
        connect = sqlite3.connect("Notes.db")
        cursor = connect.cursor()

        sqlite3_select_query = """SELECT * from All_notes"""
        cursor.execute(sqlite3_select_query)
        cursor = cursor.fetchall()
        for row in cursor:
            print("id:", row[0])
            print("Title of note:", row[1])
            print("Text of note:", row[2])
            print("Date:", row[3], end="\n\n")

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)

    finally:
        if connect:
            connect.close()
            # print("Соединение с SQLite закрыто")


def read_title_of_notes():
    try:
        connect = sqlite3.connect("Notes.db")
        cursor = connect.cursor()

        sqlite3_select_query = """SELECT * from All_notes"""
        cursor.execute(sqlite3_select_query)
        cursor = cursor.fetchall()
        for row in cursor:
            print("id:", row[0])
            print("Title of note:", row[1])

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)

    finally:
        if connect:
            connect.close()
            # print("Соединение с SQLite закрыто")

def change_note_text(new_text, dev_id):
    try:
        connect = sqlite3.connect("Notes.db")
        cursor = connect.cursor()

        sqlite3_select_query = """Update All_notes set body_of_note=? where id=?"""
        data = (new_text, dev_id)
        cursor.execute(sqlite3_select_query,data)
        connect.commit()
        print("Note is already update!!!")

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)

    finally:
        if connect:
            connect.close()
            # print("Соединение с SQLite закрыто")

def change_note_title(new_title, dev_id):
    try:
        connect = sqlite3.connect("Notes.db")
        cursor = connect.cursor()

        sqlite3_select_query = """Update All_notes set title_of_note=? where id=?"""
        data = (new_title, dev_id)
        cursor.execute(sqlite3_select_query,data)
        connect.commit()
        print("Note title is already update!!!")

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)

    finally:
        if connect:
            connect.close()
            # print("Соединение с SQLite закрыто")

def choose_note(dev_id):
    try:
        connect = sqlite3.connect("Notes.db")
        cursor = connect.cursor()

        sqlite3_choose_query = """Select * from All_notes where id=?"""
        cursor.execute(sqlite3_choose_query, dev_id)
        records = cursor.fetchall()
        for row in records:
            print("id:", row[0])
            print("Title of note:", row[1])
            print("Text of note:", row[2])

        print("Note is already choose!!")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)

    finally:
        if connect:
            connect.close()
            # print("Соединение с SQLite закрыто")


def delete_note_title(dev_id):
    try:
        connect = sqlite3.connect("Notes.db")
        cursor = connect.cursor()

        sqlite3_delete_query = """Delete from All_notes where id=?"""
        cursor.execute(sqlite3_delete_query, dev_id)
        connect.commit()
        print("Note is already delete!!")

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)

    finally:
        if connect:
            connect.close()
            # print("Соединение с SQLite закрыто")


def program_exitt():
    while True:
        ans = input("Are your sure your want to get up? Press Y/N: ")
        if ans == "Y":
            print("Come back to us again!")
            exit()
        elif ans == "N":
            controller.button_click()
        else:
            print('Press Y/N! ')

def delete_all():
    while True:
        are_you_shure = input("Are your shure that your want delete all tasks? Press Y/N: ")
        if are_you_shure == "Y":
            try:
                connect = sqlite3.connect("Notes.db")
                cursor = connect.cursor()

                sqlite3_delete_query = """Delete from All_notes"""
                cursor.execute(sqlite3_delete_query)
                connect.commit()
                print("All tasks is alredy deleted!")

                cursor.close()
                break

            except sqlite3.Error as error:
                print("Ошибка при работе с SQLite", error)

            finally:
                if connect:
                    connect.close()
                    # print("Соединение с SQLite закрыто")

        elif are_you_shure == "N":
            controller.button_click()

        else:
            print('Press Y/N! ')



def check_input_command():
    while True:
        try:
            command = int(input("Select a menu item: "))
            if command in range(1, 8):
                return command
                break
            else:
                print('Entered "COMMAND" must be type of the integer and from 1 to 7')
        except:
            print('Entered "COMMAND" must be type of the integer and from 1 to 7')



