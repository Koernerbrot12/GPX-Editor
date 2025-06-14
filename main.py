from menu import GPX_Menu
from parser import parser
from commands import cls
import gpxpy

def main():
    print("Welcome to the GPX Editor 2.0!")

    while True:
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
            print("Exiting the program.")
            break

        else:
            print("Invalid selection, please try again.")
            cls()
            continue

main()