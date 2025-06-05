from menu import GPX_Menu
from parser import parser

def main():

    print("Welcome to the GPX-editor!")
    print("1 - Import GPX file")
    print("0 - Exit")
    menu_return = False

    while True:
        if menu_return:
            print("1 - Import GPX file")
            print("0 - Exit")
        choice = input("Please select an option (1-0): ")
        if choice == '1':
            parsed_file = parser()
            menu_return = GPX_Menu(parsed_file)

        elif choice == '0':
            print("Exiting the program.")
            break

        else:
            print("Invalid selection, please try again.")

main()