from menu import GPX_Menu
from parser import parser
from commands import cls
import gpxpy


def main():

    # This is the start of our programm
    
    cls()
    print("Welcome to the GPX Editor 2.0!")
    input("Press Enter to start...")

    while True:

        # Simple menu to select the sorce of the GPX file or start with a new GPX file

        cls()
        print("1 - Import GPX file")
        print("2 - Create new GPX file")
        print("0 - Exit")
        choice = input("Please select an option (1-2-0): ")
        if choice == '1':
            parsed_file = parser()
            GPX_Menu(parsed_file)
        elif choice == '2':
            new_file=gpxpy.gpx.GPX()
            print("New GPX file created.")
            GPX_Menu(new_file)
        elif choice == '0':
            import sys
            print("Exiting the program.")
            sys.exit()

        else:
            print("Invalid selection, please try again.")
            cls()
            continue

main()