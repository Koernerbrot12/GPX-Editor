import os

from commands import cls
from Waypoints import waypoints_menu
from print_file import print_pdf
from print_file import print_gpx


def GPX_Menu(gpx_file):
   
    while True:
        cls()
        print("Choose a editor function!")
        print("1. Show GPX File")
        print("2. Waypoints menu")
        print("3. Track menu")
        print("4. Route menu")
        print("5. Save GPX File")
        print("6. Print GPX File to PDF")
        print("7. Exit")
        choice = input("Please select an option (1-7): ")
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
        elif choice == '5':
            print("You want to save the GPX file.")
            gpx_file = save_gpx(gpx_file)
        elif choice == '6':
            print("You want to print the GPX file to PDF.")
            # Print the GPX file to PDF
            print_pdf(gpx_file)
        elif choice == '7':
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

    #save the GPX file to a specified path
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
                    if save_path.endswith('.gpx') or save_path.endswith('.xml'):
                        gpx_file_str = file.to_xml()
                        with open(save_path, 'w') as f:
                            f.write(gpx_file_str)
                        print(f"GPX file saved successfully to {save_path}.")
                        print("You can now close the program or continue editing.")
                        input("Press Enter to return to the menu...")
                        cls()
                        return save_path
                    if not save_path.endswith('.gpx') and not save_path.endswith('.xml'):
                        dir_path = save_path
                        if not dir_path.endswith('/') and not dir_path.endswith('\\'):
                            dir_path += '/'
                        file_name = input("Enter the name of the GPX file (without extension): ")
                        if not file_name.endswith('.gpx') and not file_name.endswith('.xml'):
                            file_name += '.gpx'
                        full_path = os.path.join(dir_path, file_name)
                        gpx_file_str = file.to_xml()
                        with open(full_path, 'w') as f:
                            f.write(gpx_file_str)
                        print(f"GPX file saved successfully to {full_path}.")
                        print("You can now close the program or continue editing.")
                        input("Press Enter to return to the menu...")
                        cls()
                        return full_path
                elif save_choice == '2':
                    print("Save operation canceled.")
                    cls()
                    break
                else:
                    print("Invalid selection, please try again.")
