import data_base_for_notes
import datetime
import menu
from uuid import uuid4
from itertools import count

counter = count(1)

def user_choose_menu(command:int):

    # New note
    if command == 1:

        Title_of_note = input("Title: ")
        dev_id = next(counter)
        Body_of_note = input('Text: ')
        date_time = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S.%f')
        data_base_for_notes.insert_new_note_in_table(dev_id, Title_of_note, Body_of_note, date_time)
        print("Ok")

    # All notes
    if command == 2:
        data_base_for_notes.read_all_notes()
        print("Ok")

    # Change note
    if command == 3:
        data_base_for_notes.read_title_of_notes()
        print()
        command_for_update = menu.menu_for_update()
        if command_for_update == 1:
            asking_id = input("Input ID: ")
            new_title_of_note = input("New note title: ")
            data_base_for_notes.change_note_title(new_title_of_note, asking_id)

        if command_for_update == 2:
            asking_id=input("Input ID: ")
            new_body_of_note = input("New note text: ")
            data_base_for_notes.change_note_text(new_body_of_note, asking_id)

        if command_for_update == 3:
            menu.notes_menu()
        print("Ok")

    # Choose note
    if command == 4:
        data_base_for_notes.read_title_of_notes()
        dev_id = input("Input ID note for choose it:")
        data_base_for_notes.choose_note(dev_id)


    # Delete note
    if command == 5:
        data_base_for_notes.read_title_of_notes()
        print()
        dev_id = input("Input ID note for delete:")
        data_base_for_notes.delete_note_title(dev_id)

    # Exit
    if command == 6:
        data_base_for_notes.program_exitt()

    # Del all
    if command == 7:
        data_base_for_notes.delete_all()







