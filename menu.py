import gpxpy

from print_file import print_gpx
from commands import cls
from Waypoints import waypoints_menu
from Routes import routes_menu


def GPX_Menu(gpx_file):
    print("Choose a editor function!")
    print("1. Show GPX File")
    print("2. Waypoints menu")
    print("3. Track menu")
    print("4. Route menu")
    print("5. Save GPX File")
    print("6. Exit")


    while True:
        choice = input("Please select an option (1-6): ")
        if choice == '1':
            print("You want to show the GPX file.")
            print_gpx(gpx_file)
            
        elif choice == '2':
            print("Waypoints menu selected.")
            waypoints_menu(gpx_file)
        elif choice == '3':
            print("Track menu selected.")
        elif choice == '4':
            print("Route menu selected.")
            routes_menu(gpx_file)
        elif choice == '5':
            print("You want to save the GPX file.")
            save_gpx(gpx_file)
        elif choice == '6':
                while True:
                    # Ask the user if they are sure they want to exit
                    cls()
                    print("Exiting the menu are you sure? (all unsaved data will be lost!)")
                    print("")
                    print("1. Yes")
                    print("2. No")

                    exit_choice = input("Please select an option (1-2): ")

                    if exit_choice == '1':
                        print("Exiting the menu.")
                        cls()
                        return
                    elif exit_choice == '2':
                        print("canceled")
                        cls()
                        break
                    else:
                        print("Invalid selection, please try again.")
                        continue
        else:
            print("Invalid selection, please try again.")

def save_gpx(file):

    while True:
                cls()
                print("Are you sure you want to save the GPX file? (this will overwrite the existing file)")
                print("")
                print("1. Yes")
                print("2. No")

                save_choice = input("Please select an option (1-2): ")

                if save_choice == '1':
                    save_path = input("Enter the path where you want to save the GPX file (default is 'output.gpx'): ")
                    if not save_path:
                        save_path = 'output.gpx'

                    gpx_file_str = file.to_xml()
                    with open(save_path, 'w') as f:
                        f.write(gpx_file_str)
                    print("GPX file saved successfully to {save_path}.")
                    print("You can now close the program or continue editing.")
                    input("Press Enter to return to the menu...")
                    cls()
                    break
                elif save_choice == '2':
                    print("Save operation canceled.")
                    cls()
                    break
                else:
                    print("Invalid selection, please try again.")
