import builtins
import datetime
import uuid

import data_base_for_notes


def notes_menu():
    print(f"*****_Notes_*****\n"
          f"1. New note \n"
          f"2. All notes \n"
          f"3. Change note \n"
          f"4. Choose note \n"
          f"5. Delete note \n"
          f"6. Exit \n"
          f"7. Delete all\n")
    command = data_base_for_notes.check_input_command()
    return command

def menu_for_update():
    print(f"*****_Update_*****\n"
          f"1.Update Title of note \n"
          f"2.Update Text of note \n"
          f"3.Exit to the main menu \n")
    return int(input("Select a menu item:"))


