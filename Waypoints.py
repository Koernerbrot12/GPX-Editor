import gpxpy
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
            cls()
            print("Removing timestamp from all waypoints...")
            for waypoint in gpx.waypoints:
                waypoint.time = None
            print("All timestamps removed successfully.")
            input("Press Enter to return to the waypoints menu...")
        elif choice == '6':
            cls()
            print("Returning to the main menu...")
            gpx_menu.GPX_Menu(gpx)
        else:
            print("Invalid selection, please try again.")

def print_only_points(gpx):
    cls()
    for waypoint in gpx.waypoints:
        print(f"Name: {waypoint.name}, Latitude: {waypoint.latitude}, Longitude: {waypoint.longitude}, Elevation: {waypoint.elevation}, Timestamp: {waypoint.time}")
           
    
    if not gpx.waypoints:
        # Check if there are no waypoints in the GPX file
        print("No waypoints found in the GPX file.")
        input("Press Enter to return to the waypoints menu...")
        waypoints_menu(gpx)


def print_points(gpx):
    # This function prints all waypoints in the GPX file.
    cls()
    for waypoint in gpx.waypoints:
        print(f"Name: {waypoint.name}, Latitude: {waypoint.latitude}, Longitude: {waypoint.longitude}, Elevation: {waypoint.elevation}, Timestamp: {waypoint.time}")

    if not gpx.waypoints:
        # Check if there are no waypoints in the GPX file
        print("No waypoints found in the GPX file.")
        input("Press Enter to return to the waypoints menu...")
        return
    

    # Ask user if all information to a specific waypoint should be printed
    print("\nDo you want to see all information for a specific waypoint?")
    choice = input("Please select an option (y/n): ").lower()
    if choice == 'y':
        name = input("Enter the name of the waypoint: ")
        for waypoint in gpx.waypoints:
            if waypoint.name == name:
                # print all attributes of the waypoint
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
                break
        else:
            print("Waypoint not found.")
    elif choice == 'n':
        print("Returning to the waypoints menu...")
        return
    else:
        print("Invalid selection, please try again.")
        return

    input("Press Enter to return to the waypoints menu...")
     
def add_waypoint(gpx):

     # This function allows the user to add a new waypoint to the GPX file.
     cls()
     name = input("Enter the name of the waypoint: ")
     if name == "":
         print("Name cannot be empty. Please try again.")
         return
     if any(waypoint.name == name for waypoint in gpx.waypoints):
         print(f"A waypoint with the name '{name}' already exists. Please choose a different name.")
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
    
    # This function allows the user to delete a waypoint from the GPX file.
    cls()
    print_only_points(gpx)
    
    name = input("Enter the name of the waypoint to delete: ")
    
    for waypoint in gpx.waypoints:
        if waypoint.name == name:
            gpx.waypoints.remove(waypoint)
            print(f"Waypoint '{name}' deleted successfully.")
            break
    else:
        print(f"Waypoint '{name}' not found.")
    
    input("Press Enter to return to the waypoints menu...")

def update_waypoint(gpx):
    
     # This function allows the user to update a waypoint in the GPX file.
     cls()
     print_only_points(gpx)
     
     name = input("Enter the name of the waypoint to update: ")
     
     for waypoint in gpx.waypoints:
         if waypoint.name == name: # Check if the waypoint exists
             new_name = input("Enter the new name (or press Enter to keep the same): ") or waypoint.name
             while True:
                 try: # Ensure latitude is a float and within valid range
                     new_latitude = input("Enter the new latitude (or press Enter to keep the same): ")
                     if new_latitude == "": 
                         new_latitude = waypoint.latitude
                     else:
                         new_latitude = float(new_latitude)
                         if new_latitude < -90 or new_latitude > 90:
                             print("Invalid latitude. Please enter a value between -90 and 90.")
                             continue
                     break
                 except ValueError:
                     print("Invalid input. Please enter a valid latitude.")
             while True:
                 try: # Ensure longitude is a float and within valid range
                     new_longitude = input("Enter the new longitude (or press Enter to keep the same): ")
                     if new_longitude == "":
                         new_longitude = waypoint.longitude
                     else:
                         new_longitude = float(new_longitude)
                         if new_longitude < -180 or new_longitude > 180:
                             print("Invalid longitude. Please enter a value between -180 and 180.")
                             continue
                     break
                 except ValueError:
                     print("Invalid input. Please enter a valid longitude.")
             while True:
                 try: # Ensure elevation is a float, default to the current value if not provided
                     new_elevation = input("Enter the new elevation (or press Enter to keep the same): ")
                     if new_elevation == "":
                         new_elevation = waypoint.elevation
                     else:
                         new_elevation = float(new_elevation)
                     break
                 except ValueError:
                     print("Invalid input. Please enter a valid elevation.")
            # Update the waypoint attributes
             waypoint.name = new_name
             waypoint.latitude = new_latitude
             waypoint.longitude = new_longitude
             waypoint.elevation = new_elevation

             # Ask y/n to see further details to update
             print("Do you want to update additional details for this waypoint?")
             additional_details = input("Please select an option (y/n): ").lower()
             if additional_details == 'y':
                 print("1. Timestamp")
                 print("2. Magvar")
                 print("3. Geoid height")
                 print("4. Comment")
                 print("5. Description")
                 print("6. Source")
                 print("7. Link")
                 print("8. Symbol")
                 print("9. Type")
                 print("10. Fix")
                 print("11. Satellite")
                 print("12. hdop")
                 print("13. vdop")
                 print("14. pdop")
                 print("15. Age of GPS data")
                 print("16. dgpsid")

                 update_choice = input("Please select an option (1-17) or press Enter to skip: ")
                 if update_choice == '1':
                     new_time = input("Enter the new timestamp (YYYY-MM-DDTHH:MM:SSZ) or press Enter to keep the same: ")
                     if new_time:
                         waypoint.time = gpxpy.gpx.GPXTime(new_time)
                 elif update_choice == '2':
                     new_magvar = input("Enter the new magnetic variation (or press Enter to keep the same): ")
                     if new_magvar:
                         waypoint.magnetic_variation = float(new_magvar)
                 elif update_choice == '3':
                     new_geoid_height = input("Enter the new geoid height (or press Enter to keep the same): ")
                     if new_geoid_height:
                         waypoint.geoid_height = float(new_geoid_height)
                 elif update_choice == '4':
                     new_comment = input("Enter the new comment (or press Enter to keep the same): ")
                     if new_comment:
                         waypoint.comment = new_comment
                 elif update_choice == '5':
                     new_description = input("Enter the new description (or press Enter to keep the same): ")
                     if new_description:
                         waypoint.description = new_description
                 elif update_choice == '6':
                     new_source = input("Enter the new source (or press Enter to keep the same): ")
                     if new_source:
                         waypoint.source = new_source
                 elif update_choice == '7':
                     new_link = input("Enter the new link (or press Enter to keep the same): ")
                     if new_link:
                         waypoint.link = gpxpy.gpx.GPXLink(href=new_link)
                 elif update_choice == '8':
                     new_symbol = input("Enter the new symbol (or press Enter to keep the same): ")
                     if new_symbol:
                         waypoint.symbol = new_symbol
                 elif update_choice == '9':
                     new_type = input("Enter the new type (or press Enter to keep the same): ")
                     if new_type:
                         waypoint.type = new_type
                 elif update_choice == '10':
                     new_fix = input("Enter the new fix (or press Enter to keep the same): ")
                     if new_fix in ('none', '2d', '3d', 'dgps', 'pps', '3'):
                         waypoint.type_of_gpx_fix = new_fix
                 elif update_choice == '11':
                     new_satellite = input("Enter the new satellite (or press Enter to keep the same): ")
                     if new_satellite:
                         waypoint.satellites = int(new_satellite)
                 elif update_choice == '12': 
                     new_hdop = input("Enter the new hdop (or press Enter to keep the same): ")
                     if new_hdop:
                         waypoint.horizontal_dilution = float(new_hdop)
                 elif update_choice == '13': 
                     new_vdop = input("Enter the new vdop (or press Enter to keep the same): ")
                     if new_vdop:
                         waypoint.vertical_dilution = float(new_vdop)
                 elif update_choice == '14':     
                     new_pdop = input("Enter the new pdop (or press Enter to keep the same): ")
                     if new_pdop:
                         waypoint.position_dilution = float(new_pdop)
                 elif update_choice == '15':
                     new_age_of_gps_data = input("Enter the new age of GPS data (or press Enter to keep the same): ")
                     if new_age_of_gps_data:
                         waypoint.age_of_gps_data = float(new_age_of_gps_data)
                 elif update_choice == '16':
                     new_dgpsid = input("Enter the new dgpsid (or press Enter to keep the same): ")
                     if new_dgpsid:
                         waypoint.dgps_id = int(new_dgpsid)      
                 else:
                     print("No additional details updated or invalid type.")
             elif additional_details == 'n':
                 print("No additional details updated.")
                 
             else:
                 print("Invalid selection, please try again.")
                 return
            

             print(f"Waypoint '{name}' updated successfully.")
             break
     else:
         print(f"Waypoint '{name}' not found.")
     
     input("Press Enter to return to the waypoints menu...")

def remove_timestamp(gpx):
    
    # This function allows the user to remove timestamps from waypoints in the GPX file.
    cls()
    print("1. Remove timestamp from a specific waypoint")
    print("2. Remove timestamp from all waypoints")

    choice = input("Please select an option (1-2): ")

    if choice == '1':
        name = input("Enter the name of the waypoint to remove the timestamp from: ")
        for waypoint in gpx.waypoints:
            if waypoint.name == name:
                waypoint.time = None
                print(f"Timestamp removed from waypoint '{name}'.")
                break
        else:
            print(f"Waypoint '{name}' not found.")
    elif choice == '2':
        for waypoint in gpx.waypoints:
            waypoint.time = None
        print("All Timestamps removed from all waypoints.")
        print("press Enter to return to the waypoints menu...")
    else:
        print("Invalid selection, please try again.")
