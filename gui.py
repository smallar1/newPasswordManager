import PySimpleGUI as sg
from database import *
from encryption import *


def login_window():
    layout = [[sg.Text("Enter your Username and Master Password")],
              [[sg.Text("Username")], [sg.InputText()]],
              [[sg.Text("Master Password")], [sg.InputText(do_not_clear=False)]],
              [sg.Button('Enter'), sg.Button('Back')]]

    login = sg.Window('Password Manager v1.0', layout)

    while True:
        event, values = login.read()

        if event == sg.WIN_CLOSED or event == 'Back':
            login.close()
            break
        elif event == 'Enter':
            if values[0] == '' or values[1] == '':
                sg.popup("Please enter a username and password")
            else:
                hashed_pass = str(hash_function(values[1]))

                for user in get_users():
                    if values[0] == user:
                        if hashed_pass == get_password(values[0]):
                            access = True
                            break
                        else:
                            access = False
                            break
                else:
                    access = None

                # Todo : FIX THESE ARE TEMPORARY
                if access:
                    sg.popup("Access Granted")
                    # TODO : Open the actual password manager here
                    login.close()
                elif access is None:
                    sg.popup("User not found")
                else:
                    sg.popup("Access Denied")
                    login.close()
                pass


def delete_window():
    layout = [[sg.Text("Enter your Username and Master Password")],
              [[sg.Text("Username")], [sg.InputText()]],
              [[sg.Text("Master Password")], [sg.InputText(do_not_clear=False)]],
              [sg.Button('Enter'), sg.Button('Back')]]

    delete = sg.Window('Password Manager v1.0', layout)

    while True:
        event, values = delete.read()

        if event == sg.WIN_CLOSED or event == 'Back':
            delete.close()
            break
        elif event == 'Enter':
            if values[0] == '' or values[1] == '':
                sg.popup("Please enter a username and password")
            else:
                hashed_pass = str(hash_function(values[1]))

                for user in get_users():
                    if values[0] == user:
                        if hashed_pass == get_password(values[0]):
                            access = True
                            break
                        else:
                            access = False
                            break
                else:
                    access = None

                if access:
                    pop_up = sg.popup_yes_no("Are you sure you want to delete this account?")
                    if pop_up == 'Yes':
                        user_id = get_userid(values[0])
                        delete_user(user_id)
                        sg.popup("User deleted")
                        delete.close()
                    else:
                        sg.popup("User Cancelled")
                        delete.close()
                elif access is None:
                    sg.popup("User not found")

                else:
                    sg.popup("Access Denied")
                    delete.close()
                pass




def register_window():
    # TODO: Will change when registration becomes possible -> Exactly like login rn
    layout = [[sg.Text("Enter a Username and Master Password")],
              [[sg.Text("Username")], [sg.InputText()]],
              [[sg.Text("Master Password")], [sg.InputText(do_not_clear=False)]],
              [sg.Button('Enter'),sg.Button('Back')]]

    register = sg.Window('Password Manager v1.0', layout)

    while True:
        event, values = register.read()

        if event == sg.WIN_CLOSED or event == 'Back':
            register.close()
            break
        elif event == 'Enter':
            if values[0] in get_users():
                sg.popup("Username already exists!")
                continue
            if values[0] == '' or values[1] == '':
                sg.popup("Fields cannot be left empty!")
                continue
            else:
                user_specific_key = generate_key()
                hashed_password = hash_function(values[1])
                try:
                    add_user(values[0], hashed_password, user_specific_key)
                    sg.popup(f"New User {values[0]} registered!")
                    register.close()
                except sqlite3.Error:
                    sg.popup("A database error occurred! User not registered.")
                    register.close()


def main_window():
    layout = [[sg.Text("Welcome to Password Manager v1.0")],
              [sg.Button('Login'),
               sg.Button('Register User'),
               sg.Button('Delete User'),
               sg.Button('Close')]]

    main = sg.Window('Password Manager v1.0', layout)

    while True:
        event, values = main.read()

        if event == sg.WIN_CLOSED or event == 'Close':
            print("Goodbye!")
            break

        # TODO: Insert 3 elif statements for all functions
        elif event == 'Login':
            login_window()

        elif event == 'Register User':
            register_window()

        elif event == 'Delete User':
            delete_window()

    main.close()


main_window()
