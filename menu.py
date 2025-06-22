import os
import errno

from commands import cls
from Waypoints import waypoints_menu
from print_file import converter_function
from print_file import print_gpx
from Routes import routes_menu
from Tracks import tracks_menu
from grafic import grafic



def GPX_Menu(gpx_file):

    #Simple Menu with a if else loop to select the different functions of the GPX Editor
   
    while True:
        cls()
        print("Choose a editor function!")
        print("1. Show GPX File")
        print("2. Waypoints menu")
        print("3. Track menu")
        print("4. Route menu")
        print("5. Show track or route on a map")
        print("6. Save GPX File")
        print("7. Print GPX File to PDF")
        print("8. Exit")

        choice = input("Please select an option (1-8): ")
        if choice == '1':
            print("You want to show the GPX file.")
            print_gpx(gpx_file) 
        elif choice == '2':
            print("Waypoints menu selected.")
            waypoints_menu(gpx_file)
        elif choice == '3':
            print("Track menu selected.")
            tracks_menu(gpx_file)
        elif choice == '4':
            print("Route menu selected.")
            routes_menu(gpx_file)
        elif choice == '5':
            print("You want to show the track or route on a map.")
            grafic(gpx_file)
        elif choice == '6':
            print("You want to save the GPX file.")
            save_gpx(gpx_file)
        elif choice == '7':
            print("You want to print the GPX file to PDF.")
            converter_function(gpx_file)
        elif choice == '8':
                while True:

                    # Ask the user if they are sure they want to exit
                    
                    cls()
                    print("Exiting the menu are you sure? (all unsaved data will be lost!)")
                    print("")
                    print("1. Yes")
                    print("2. No")

                    exit_choice = input("Please select an option (1-2): ")

                    if exit_choice == '1':

                        # Needs to be imported here to avoid circular import issues

                        import main as main_menu

                        print("Exiting the menu.")
                        cls()
                        main_menu.main()
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

    # Save the GPX file to a specified path

    while True:
        cls()
        print("Are you sure you want to save the GPX file?")
        print("")
        print("1. Yes")
        print("2. No")

        save_choice = input("Please select an option (1-2): ")

        if save_choice == '1':
            while True:
                save_path = input("Enter the path where you want to save the GPX file (default is 'output.gpx'): ").strip().strip('"').strip("'")
                if not save_path:
                    save_path = 'output.gpx'

                # Case 1: User entered a full filename

                if save_path.endswith('.gpx') or save_path.endswith('.xml'):
                    gpx_file_str = file.to_xml()

                    # With try we ensure that the file can be saved without errors

                    try:
                        with open(save_path, 'w') as f:
                            f.write(gpx_file_str)
                        print(f"GPX file saved successfully to {save_path}.")
                        print("You can now close the program or continue editing.")
                        input("Press Enter to return to the menu...")
                        cls()
                        return save_path
                    except OSError as e:
                        print(f"Error saving file: {e.strerror}. Please try again with a valid path.")
                        continue
                    
                # Case 2: User entered a directory

                else:
                    dir_path = save_path
                    if not dir_path.endswith('/') and not dir_path.endswith('\\'):
                        dir_path += '/'
                    file_name = input("Enter the name of the GPX file (without extension): ").strip().strip('"').strip("'")
                    if not file_name.endswith('.gpx') and not file_name.endswith('.xml'):
                        file_name += '.gpx'
                    full_path = os.path.join(dir_path, file_name)
                    gpx_file_str = file.to_xml()

                    # With try we ensure that the file can be saved without errors

                    try:
                        with open(full_path, 'w') as f:
                            f.write(gpx_file_str)
                        print(f"GPX file saved successfully to {full_path}.")
                        print("You can now close the program or continue editing.")
                        input("Press Enter to return to the menu...")
                        cls()
                        return full_path
                    except OSError as e:
                        print(f"Error saving file: {e.strerror}. Please try again with a valid path.")
                        continue
        elif save_choice == '2':
            print("Save operation canceled.")
            cls()
            break
        else:
            print("Invalid selection, please try again.")
