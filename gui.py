import PySimpleGUI as sg


def login_window():
    layout = [[sg.Text("Enter your Username and Master Password")],
              [[sg.Text("Username")], [sg.InputText()]],
              [[sg.Text("Master Password")], [sg.InputText()]],
              [sg.Button('Back')]]

    login = sg.Window('Password Manager v1.0', layout)

    while True:
        event, values = login.read()

        if event == sg.WIN_CLOSED or event == 'Back':
            login.close()
            print("Going Back!")
            break


def delete_window():
    layout = [[sg.Text("Enter your Username and Master Password")],
              [[sg.Text("Username")], [sg.InputText()]],
              [[sg.Text("Master Password")], [sg.InputText()]],
              [sg.Button('Back')]]

    delete = sg.Window('Password Manager v1.0', layout)

    while True:
        event, values = delete.read()

        if event == sg.WIN_CLOSED or event == 'Back':
            delete.close()
            print("Going Back!")
            break


def register_window():
    # TODO: Will change when registration becomes possible -> Exactly like login rn
    layout = [[sg.Text("Enter a Username and Master Password")],
              [[sg.Text("Username")], [sg.InputText()]],
              [[sg.Text("Master Password")], [sg.InputText()]],
              [sg.Button('Back')]]

    register = sg.Window('Password Manager v1.0', layout)

    while True:
        event, values = register.read()

        if event == sg.WIN_CLOSED or event == 'Back':
            register.close()
            print("Going Back!")
            break


def main_window():
    layout = [[sg.Text("Welcome to Password Manager v1.0")],
              [sg.Button('Login'),
               sg.Button('Register User'),
               sg.Button('Delete User'),
               sg.Button('Cancel')]]

    main = sg.Window('Password Manager v1.0', layout)

    while True:
        event, values = main.read()

        if event == sg.WIN_CLOSED or event == 'Cancel':
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
