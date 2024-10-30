import PySimpleGUI as sg
from database import *
from encryption import *


def login_window():
    layout = [[sg.Text("Enter your Username and Master Password")],
              [[sg.Text("Username")], [sg.InputText()]],
              [[sg.Text("Master Password")], [sg.InputText(do_not_clear=False, password_char='*')]],
              [sg.Button('Enter', key='\r'), sg.Button('Back')]]

    login = sg.Window('Password Manager v1.0', layout, return_keyboard_events=True)

    while True:
        event, values = login.read()

        if event == sg.WIN_CLOSED or event == 'Back':
            login.close()
            main_window()
            break
        elif event == 'Enter' or event == '\r':
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
                    services_window(values[0])
                elif access is None:
                    sg.popup("User not found")
                else:
                    sg.popup("Access Denied")
                    login.close()
                pass


def services_window(username):
    layout = [[sg.Text('What would you like to do?')],
              [sg.Button('Add Service')], [sg.Button('Remove Service')], [sg.Button('View Services'),
                                                                          [sg.Button('Edit Services')]],
              [sg.Button('Logout')]]

    service = sg.Window('Password Manager v1.0', layout)

    while True:
        event, values = service.read()

        if event == sg.WIN_CLOSED or event == 'Logout':
            service.close()
            main_window()
            break
        elif event == 'Add Service':
            service.close()
            add_service_window(username)
            # TODO
            pass
        elif event == 'Remove Service':
            # TODO
            pass
        elif event == 'Edit Service':
            # TODO
            pass
        elif event == 'View Services':
            # TODO
            pass


def delete_window():
    layout = [[sg.Text("Enter your Username and Master Password")],
              [[sg.Text("Username")], [sg.InputText()]],
              [[sg.Text("Master Password")], [sg.InputText(do_not_clear=False, password_char='*')]],
              [sg.Button('Enter'), sg.Button('Back')]]

    delete = sg.Window('Password Manager v1.0', layout)

    while True:
        event, values = delete.read()

        if event == sg.WIN_CLOSED or event == 'Back':
            delete.close()
            main_window()
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
              [[sg.Text("Master Password")], [sg.InputText(do_not_clear=False, password_char='*')]],
              [sg.Button('Enter'), sg.Button('Back')]]

    register = sg.Window('Password Manager v1.0', layout)

    while True:
        event, values = register.read()

        if event == sg.WIN_CLOSED or event == 'Back':
            register.close()
            main_window()
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


def add_service_window(username):
    layout = [[sg.Text("Enter the service name, username, and password")],
              [[sg.Text("Service Name")], [sg.InputText()]],
              [[sg.Text("Username")], [sg.InputText()]],
              [[sg.Text("Password")], [sg.InputText(do_not_clear=False, password_char='*')]],
              [sg.Button('Enter'), sg.Button('Back')]]

    add_serv = sg.Window('Add Servie', layout)

    while True:
        event, values = add_serv.read()

        if event == sg.WIN_CLOSED or event == 'Back':
            add_serv.close()
            services_window(username)
        else:
            service_name = values[0]
            user = values[1]
            user_id = get_userid(username)
            print(f'This is user_id : {user_id}')
            encryption_key = get_encryption_key(user_id)[2:-1]
            print(f'This is encryption_key : {encryption_key}')
            # exit(1)
            passw = values[2]
            print(f"Services: {get_services(user_id)}")

            # if service_name in get_services(user_id) and user in get_services(user_id):

            # if check_if_service_exists(user_id, service_name) == 0:
            #     encrypted_pass = encrypt_password(encryption_key, passw)
            #     add_service(service_name, user, encrypted_pass, user_id)
            #     test = retrieve_user_pass_from_service(user_id, service_name)
            #     print(test[0] + ' ' + decrypt_password(encryption_key, test[1]))
            #     add_serv.close()

            if check_if_service_exists(user_id, service_name, user) > 0:

                # sg.popup("Service already exists! Would you like to replace the service?")
                if sg.popup_yes_no("Replace Service?") == 'Yes':
                    print('Yes')
                    # TODO : Use implemented replace service
                    sg.popup('Not Implemented')
                else:
                    print('No')
                    add_serv.close()
                    services_window(username)
            else:

                encrypted_pass = encrypt_password(encryption_key, passw)
                add_service(service_name, user, encrypted_pass, user_id)
                test = retrieve_user_pass_from_service(user_id, service_name)
                print(test[0] + ' ' + decrypt_password(encryption_key, test[1]))
                add_serv.close()

        pass

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
            main.close()
            exit(1)

        # TODO: Insert 3 elif statements for all functions
        elif event == 'Login':
            main.close()
            login_window()

        elif event == 'Register User':
            main.close()
            register_window()

        elif event == 'Delete User':
            main.close()
            delete_window()


if __name__ == "__main__":
    main_window()
