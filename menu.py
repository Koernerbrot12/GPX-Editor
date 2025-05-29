import gpxpy

from print_file import print_gpx
from commands import cls


def GPX_Menu(gpx_file):
    print("Choose a editor function!")
    print("1. show GPX File")
    print("2. Create Point")
    print("3. Delete Point")
    print("4. Update Point")
    print("5. Create Track")
    print("6. Create Route")
    print("7. Exit")


    while True:
        choice = input("Please select an option (1-7): ")
        if choice == '1':
            print("You want to show the GPX file.")
            print_gpx(gpx_file)
            
        elif choice == '2':
            print("You wanne delete a point.")
        elif choice == '3':
            print("You wanne delete a point.")
        elif choice == '4':
            print("You wanne update a point.")
        elif choice == '5':
            print("You wanne create a track.")
        elif choice == '6':
            print("You wanne create a route.")
        elif choice == '7':

            while True:
            # Ask the user if they are sure they want to exit
                cls()
                print("Exiting the menu are you sure? (all data will be lost!)")
                print("")
                print("1. Yes")
                print("2. No")

                exit_choice = input("Please select an option (1-2): ")

                if exit_choice == '1':
                    print("Exiting the menu.")
                    return
                elif exit_choice == '2':
                    print("canceled")
                    break
                else:
                    print("Invalid selection, please try again.")
                    continue
        else:
            print("Invalid selection, please try again.")
