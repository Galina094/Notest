import menu
import functions
import data_base_for_notes

def button_click():
    while True:
        # data_base_for_notes.create_sql_table()
        command = menu.notes_menu()
        functions.user_choose_menu(command)


