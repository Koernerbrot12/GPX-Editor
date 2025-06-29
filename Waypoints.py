import gpxpy
import datetime
from commands import cls
import menu as gpx_menu

# With the help of the library gpxpy, the waypoints are easy to find and manage.
def waypoints_menu(gpx):

    # This function displays the waypoints menu and allows the user to manage waypoints in the GPX file.
    while True:
        # If returning to the waypoints menu, display the menu again
        cls()
        print("Waypoints Menu")
        print("1. Show all waypoints")
        print("2. Add a waypoint")
        print("3. Delete a waypoint")
        print("4. Update a waypoint")
        print("5. Remove timestamp from waypoint")
        print("6. Return to main menu")
        choice = input("Please select an option (1-6): ")
        if choice == '1':
            print_points(gpx)
        elif choice == '2':
            add_waypoint(gpx)
        elif choice == '3':
            delete_waypoint(gpx)
        elif choice == '4':
            update_waypoint(gpx)
        elif choice == '5':
            remove_timestamp(gpx)
        elif choice == '6':
            cls()
            print("Returning to the main menu...")
            gpx_menu.GPX_Menu(gpx)
        else:
            print("Invalid selection, please try again.")

def print_only_points(gpx):
    cls()
    if not gpx.waypoints:
        print("No waypoints found in the GPX file.")
        input("Press Enter to return to the waypoints menu...")
        return

    print("Waypoints:")
    for idx, waypoint in enumerate(gpx.waypoints, start=1):
        print(f"{idx}. {waypoint.name if waypoint.name else 'Unnamed'} (Latitude: {waypoint.latitude}, Longitude: {waypoint.longitude}, Elevation: {waypoint.elevation}, Timestamp: {waypoint.time})")

    

def print_points(gpx):
    # This function prints all waypoints in the GPX file, numbers them, and lets the user select by number.
    cls()
    if not gpx.waypoints:
        print("No waypoints found in the GPX file.")
        input("Press Enter to return to the waypoints menu...")
        return

    print("Waypoints:")
    for idx, waypoint in enumerate(gpx.waypoints, start=1):
        print(f"{idx}. {waypoint.name if waypoint.name else 'Unnamed'} (Latitude: {waypoint.latitude}, Longitude: {waypoint.longitude}, Elevation: {waypoint.elevation}, Timestamp: {waypoint.time})")

    print("\nDo you want to see all information for a specific waypoint?")
    choice = input("Please select an option (y/n): ").lower()
    if choice == 'y':
        selection = input("Enter the number of the waypoint: ")
        if not selection.isdigit() or not (1 <= int(selection) <= len(gpx.waypoints)):
            print("Invalid selection. Please enter a valid number.")
            input("Press Enter to return to the waypoints menu...")
            return
        idx = int(selection) - 1
        waypoint = gpx.waypoints[idx]
        print(f"{'Name:':20} {waypoint.name if waypoint.name else 'None'}")
        print(f"{'Latitude:':20} {waypoint.latitude if waypoint.latitude is not None else 'None'}")
        print(f"{'Longitude:':20} {waypoint.longitude if waypoint.longitude is not None else 'None'}")
        print(f"{'Elevation:':20} {waypoint.elevation if waypoint.elevation is not None else 'None'}")
        print(f"{'Timestamp:':20} {waypoint.time if waypoint.time else 'None'}")
        print(f"{'Magvar:':20} {waypoint.magnetic_variation if waypoint.magnetic_variation is not None else 'None'}")
        print(f"{'Geoid Height:':20} {waypoint.geoid_height if waypoint.geoid_height is not None else 'None'}")
        print(f"{'Comment:':20} {waypoint.comment if waypoint.comment else 'None'}")
        print(f"{'Description:':20} {waypoint.description if waypoint.description else 'None'}")
        print(f"{'Source:':20} {waypoint.source if waypoint.source else 'None'}")
        print(f"{'Link:':20} {waypoint.link if waypoint.link else 'None'}")
        print(f"{'Symbol:':20} {waypoint.symbol if waypoint.symbol else 'None'}")
        print(f"{'Type:':20} {waypoint.type if waypoint.type else 'None'}")
        print(f"{'Fix:':20} {waypoint.type_of_gpx_fix if waypoint.type_of_gpx_fix else 'None'}")
        print(f"{'Satellite:':20} {waypoint.satellites if waypoint.satellites is not None else 'None'}")
        print(f"{'Hdop:':20} {waypoint.horizontal_dilution if waypoint.horizontal_dilution is not None else 'None'}")
        print(f"{'Vdop:':20} {waypoint.vertical_dilution if waypoint.vertical_dilution is not None else 'None'}")
        print(f"{'Pdop:':20} {waypoint.position_dilution if waypoint.position_dilution is not None else 'None'}")
        print(f"{'Age of GPS Data:':20} {waypoint.age_of_dgps_data if waypoint.age_of_dgps_data is not None else 'None'}")
        print(f"{'Dgpsid:':20} {waypoint.dgps_id if waypoint.dgps_id is not None else 'None'}")
    elif choice == 'n':
        print("Returning to the waypoints menu...")
        return
    else:
        print("Invalid selection, please try again.")
        input("Press Enter to return to the waypoints menu...")
        return

    input("Press Enter to return to the waypoints menu...")



def add_waypoint(gpx):

     # This function allows the user to add a new waypoint to the GPX file.
     cls()
     name = input("Enter the name of the waypoint (optional, press Enter to skip): ")
     if name == "":
         name = None
     # Only check for duplicate names if a name is provided
     if name is not None and any(waypoint.name == name for waypoint in gpx.waypoints):
         input(f"A waypoint with the name '{name}' already exists. Please choose a different name. Press enter to return.")
         return
     while True:
         try:
             latitude = float(input("Enter the latitude of the waypoint: "))
             if latitude < -90 or latitude > 90:
                 print("Invalid latitude. Please enter a value between -90 and 90.")
                 continue
             break
         except ValueError:
             print("Invalid input. Please enter a valid latitude.")
         # Ensure longitude is a float and within valid range
     while True:
        try:
            longitude = float(input("Enter the longitude of the waypoint: "))
            if longitude < -180 or longitude > 180:
                print("Invalid longitude. Please enter a value between -180 and 180.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid longitude.")
        # Ensure elevation is a float, default to 0 if not provided
     while True:
        try:
            elevation_input = input("Enter the elevation of the waypoint (optional, press Enter to skip): ")
            if elevation_input == "":
                elevation = 0.0  # Default value if no input is provided
            else:
                elevation = float(elevation_input)
            break
        except ValueError:
            print("Invalid input. Please enter a valid elevation.")
     
     new_waypoint = gpxpy.gpx.GPXWaypoint(latitude, longitude, elevation=elevation, name=name)
     gpx.waypoints.append(new_waypoint)

     
     print(f"Waypoint '{name}' added successfully.")
     input("Press Enter to return to the waypoints menu...")

def delete_waypoint(gpx):
    # This function allows the user to delete a waypoint from the GPX file using numbers instead of names.
    cls()
    print_only_points(gpx)
  

    selection = input("Enter the number of the waypoint to delete (or type 'cancel' to return): ")
    if selection.lower() == 'cancel':
        print("Deletion cancelled.")
        input("Press Enter to return to the waypoints menu...")
        return

    if not selection.isdigit() or not (1 <= int(selection) <= len(gpx.waypoints)):
        print("Invalid selection. Please enter a valid number.")
        input("Press Enter to return to the waypoints menu...")
        return

    idx = int(selection) - 1
    deleted_waypoint = gpx.waypoints.pop(idx)
    print(f"Waypoint '{deleted_waypoint.name if deleted_waypoint.name else 'Unnamed'}' deleted successfully.")

    input("Press Enter to return to the waypoints menu...")

def update_waypoint(gpx):
    # This function allows the user to update a waypoint in the GPX file using numbers instead of names.
    cls()
    print_only_points(gpx)

    selection = input("Enter the number of the waypoint to update (or type 'cancel' to return): ")
    if selection.lower() == 'cancel':
        print("Update cancelled.")
        input("Press Enter to return to the waypoints menu...")
        return

    if not selection.isdigit() or not (1 <= int(selection) <= len(gpx.waypoints)):
        print("Invalid selection. Please enter a valid number.")
        input("Press Enter to return to the waypoints menu...")
        return

    idx = int(selection) - 1
    waypoint = gpx.waypoints[idx]

    while True:
        cls()
        print(f"Updating waypoint: {waypoint.name if waypoint.name else 'Unnamed'} (Lat: {waypoint.latitude}, Lon: {waypoint.longitude}, Ele: {waypoint.elevation}, Time: {waypoint.time})")
        print("1. Name")
        print("2. Latitude")
        print("3. Longitude")
        print("4. Elevation")
        print("5. Timestamp")
        print("6. Magvar")
        print("7. Geoid height")
        print("8. Comment")
        print("9. Description")
        print("10. Source")
        print("11. Link")
        print("12. Symbol")
        print("13. Type")
        print("14. Fix")
        print("15. Satellite")
        print("16. hdop")
        print("17. vdop")
        print("18. pdop")
        print("19. Age of GPS data")
        print("20. dgpsid")
        print("0. (or press enter) Finish updating")

        update_choice = input("Please select an option (1-20, 0 to finish): ")

        if update_choice == '0' or update_choice == '':
            break
        elif update_choice == '1':
            new_name = input("Enter the new name (or press Enter to keep the same): ")
            if new_name:
                waypoint.name = new_name
        elif update_choice == '2':
            while True:
                new_latitude = input("Enter the new latitude (or press Enter to keep the same): ")
                if new_latitude == "":
                    break  # Keep the same
                try:
                    new_latitude = float(new_latitude)
                    if new_latitude < -90 or new_latitude > 90:
                        print("Invalid latitude. Please enter a value between -90 and 90.")
                        continue
                    waypoint.latitude = new_latitude
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid latitude.")
        elif update_choice == '3':
            while True:
                new_longitude = input("Enter the new longitude (or press Enter to keep the same): ")
                if new_longitude == "":
                    break  # Keep the same
                try:
                    new_longitude = float(new_longitude)
                    if new_longitude < -180 or new_longitude > 180:
                        print("Invalid longitude. Please enter a value between -180 and 180.")
                        continue
                    waypoint.longitude = new_longitude
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid longitude.")
        elif update_choice == '4':
            while True:
                new_elevation = input("Enter the new elevation (or press Enter to keep the same): ")
                if new_elevation == "":
                    break  # Keep the same
                try:
                    waypoint.elevation = float(new_elevation)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid elevation.")
        elif update_choice == '5':
            print("Enter the new timestamp for the waypoint.")
            print("Accepted formats:")
            print("  1. YYYY-MM-DDTHH:MM:SSZ (e.g., 2024-06-25T14:30:00Z)")
            print("  2. YYYY-MM-DD HH:MM:SS (e.g., 2024-06-25 14:30:00)")
            print("  3. YYYY-MM-DD (date only, time will be set to 00:00:00)")
            while True:
                newtimestamp = input("Enter the new timestamp or press Enter to keep the same: ")
                if not newtimestamp:
                    break  # Keep the same
                try:
                    if newtimestamp.endswith("Z"):
                        waypoint.time = datetime.datetime.strptime(newtimestamp, "%Y-%m-%dT%H:%M:%SZ")
                    elif "T" in newtimestamp:
                        waypoint.time = datetime.datetime.strptime(newtimestamp, "%Y-%m-%dT%H:%M:%S")
                    elif " " in newtimestamp:
                        waypoint.time = datetime.datetime.strptime(newtimestamp, "%Y-%m-%d %H:%M:%S")
                    else:
                        waypoint.time = datetime.datetime.strptime(newtimestamp, "%Y-%m-%d")
                    print("Timestamp updated successfully.")
                    break
                except ValueError:
                    print("Invalid timestamp format. Please use one of the accepted formats above.")
        elif update_choice == '6':
            while True:
                new_magvar = input("Enter the new magnetic variation (or press Enter to keep the same): ")
                if new_magvar == "":
                    break
                try:
                    waypoint.magnetic_variation = float(new_magvar)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
        elif update_choice == '7':
            while True:
                new_geoid_height = input("Enter the new geoid height (or press Enter to keep the same): ")
                if new_geoid_height == "":
                    break
                try:
                    waypoint.geoid_height = float(new_geoid_height)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
        elif update_choice == '8':
            new_comment = input("Enter the new comment (or press Enter to keep the same): ")
            if new_comment:
                waypoint.comment = new_comment
        elif update_choice == '9':
            new_description = input("Enter the new description (or press Enter to keep the same): ")
            if new_description:
                waypoint.description = new_description
        elif update_choice == '10':
            new_source = input("Enter the new source (or press Enter to keep the same): ")
            if new_source:
                waypoint.source = new_source
        elif update_choice == '11':
            while True:
                new_link = input("Enter the new link (or press Enter to keep the same): ")
                if not new_link:
                    break  # Keep the same
                if not (new_link.startswith("http://") or new_link.startswith("https://")):
                    print("Invalid link format. Please enter a valid URL starting with http:// or https://.")
                    continue
                waypoint.link = [new_link]
                break
        elif update_choice == '12':
            new_symbol = input("Enter the new symbol (or press Enter to keep the same): ")
            if new_symbol:
                waypoint.symbol = new_symbol
        elif update_choice == '13':
            new_type = input("Enter the new type (or press Enter to keep the same): ")
            if new_type:
                waypoint.type = new_type
        elif update_choice == '14':
            valid_fixes = ('none', '2d', '3d', 'dgps', 'pps', '3')
            while True:
                new_fix = input("Enter the new fix (either 'none', '2d', '3d', 'dgps', 'pps', '3') or press Enter to keep the same: ")
                if new_fix == "":
                    break  # Keep the same
                if new_fix in valid_fixes:
                    waypoint.type_of_gpx_fix = new_fix
                    break
                else:
                    print("Invalid fix type. Please enter one of the following: 'none', '2d', '3d', 'dgps', 'pps', '3'.")
        elif update_choice == '15':
            while True:
                new_satellite = input("Enter the new satellite (or press Enter to keep the same): ")
                if new_satellite == "":
                    break
                try:
                    waypoint.satellites = int(new_satellite)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")
        elif update_choice == '16':
            while True:
                new_hdop = input("Enter the new hdop (or press Enter to keep the same): ")
                if new_hdop == "":
                    break
                try:
                    waypoint.horizontal_dilution = float(new_hdop)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
        elif update_choice == '17':
            while True:
                new_vdop = input("Enter the new vdop (or press Enter to keep the same): ")
                if new_vdop == "":
                    break
                try:
                    waypoint.vertical_dilution = float(new_vdop)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
        elif update_choice == '18':
            while True:
                new_pdop = input("Enter the new pdop (or press Enter to keep the same): ")
                if new_pdop == "":
                    break
                try:
                    waypoint.position_dilution = float(new_pdop)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
        elif update_choice == '19':
            while True:
                new_age_of_gps_data = input("Enter the new age of GPS data (or press Enter to keep the same): ")
                if new_age_of_gps_data == "":
                    break
                try:
                    waypoint.age_of_dgps_data = float(new_age_of_gps_data)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
        elif update_choice == '20':
            while True:
                new_dgpsid = input("Enter the new dgpsid (or press Enter to keep the same): ")
                if new_dgpsid == "":
                    break
                try:
                    waypoint.dgps_id = int(new_dgpsid)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")
        else:
            print("No additional details updated or invalid type.")
    print(f"Waypoint '{waypoint.name}' updated successfully.")
    input("Press Enter to return to the waypoints menu...")


def remove_timestamp(gpx):
    # This function allows the user to remove timestamps from waypoints in the GPX file using numbers.
    cls()
    print("1. Remove timestamp from a specific waypoint")
    print("2. Remove timestamp from all waypoints")

    choice = input("Please select an option (1-2): ")

    if choice == '1':
        print_only_points(gpx)

        selection = input("Enter the number of the waypoint to remove the timestamp from (or type 'cancel' to return): ")
        if selection.lower() == 'cancel':
            print("Operation cancelled.")
            input("Press Enter to return to the waypoints menu...")
            return

        if not selection.isdigit() or not (1 <= int(selection) <= len(gpx.waypoints)):
            print("Invalid selection. Please enter a valid number.")
            input("Press Enter to return to the waypoints menu...")
            return

        idx = int(selection) - 1
        gpx.waypoints[idx].time = None
        print(f"Timestamp removed from waypoint '{gpx.waypoints[idx].name if gpx.waypoints[idx].name else 'Unnamed'}'.")

    elif choice == '2':
        choice2=input("This will remove timestamps from all waypoints. Are you sure? (y/n): ").lower()
        if choice2 == 'y':
            for waypoint in gpx.waypoints:
                waypoint.time = None
            print("Timestamps removed from all waypoints.")
            input("Press Enter to return to the waypoints menu...")
            return
        elif choice2 == 'n':
            print("Operation cancelled.")
            input("Press Enter to return to the waypoints menu...")
            return
        
    else:
        print("Invalid selection, please try again.")

    input("Press Enter to return to the waypoints menu...")