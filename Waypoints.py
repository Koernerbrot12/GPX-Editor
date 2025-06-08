import gpxpy
from commands import cls

def waypoints_menu(gpx):
    
    """
    This function displays the waypoints menu and allows the user to interact with waypoints in a GPX file.
    
    :param gpx: The GPX data containing waypoints.
    """
    cls()
    print("Waypoints Menu")
    print("1. Show all waypoints")
    print("2. Add a waypoint")
    print("3. Delete a waypoint")
    print("4. Update a waypoint")
    print("5. Remove timestamp from waypoint")
    print("6. Return to main menu")

    while True:
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
            return
        else:
            print("Invalid selection, please try again.")

def print_points(gpx):

     cls()
# This function prints all waypoints in the GPX file.
     for waypoint in gpx.waypoints:
         print(f"Name: {waypoint.name}, Latitude: {waypoint.latitude}, Longitude: {waypoint.longitude}, Elevation: {waypoint.elevation}, Timestamp: {waypoint.time}")
     if not gpx.waypoints:
         print("No waypoints found in the GPX file.")
         input("Press Enter to return to the waypoints menu...")

     print("\nEnd of waypoints.")
     input("Press Enter to return to the waypoints menu...")

def add_waypoint(gpx):

     """
     This function allows the user to add a waypoint to the GPX file.
     
     :param gpx: The GPX data to which the waypoint will be added.
     """
     cls()
     name = input("Enter the name of the waypoint: ")
     latitude = float(input("Enter the latitude of the waypoint: "))
     longitude = float(input("Enter the longitude of the waypoint: "))
     elevation = float(input("Enter the elevation of the waypoint (optional, press Enter to skip): ") or 0)
     
     new_waypoint = gpxpy.gpx.GPXWaypoint(latitude, longitude, elevation=elevation, name=name)
     gpx.waypoints.append(new_waypoint)
     
     print(f"Waypoint '{name}' added successfully.")
     input("Press Enter to return to the waypoints menu...")

def delete_waypoint(gpx):
    
    """
    This function allows the user to delete a waypoint from the GPX file.
    
    :param gpx: The GPX data from which the waypoint will be deleted.
    """
    cls()
    print_points(gpx)
    
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
    
     """
     This function allows the user to update a waypoint in the GPX file.
     
     :param gpx: The GPX data containing waypoints.
     """
     cls()
     print_points(gpx)
     
     name = input("Enter the name of the waypoint to update: ")
     
     for waypoint in gpx.waypoints:
          if waypoint.name == name:
               new_name = input("Enter the new name (or press Enter to keep the same): ") or waypoint.name
               new_latitude = float(input(f"Enter the new latitude (current: {waypoint.latitude}): ") or waypoint.latitude)
               new_longitude = float(input(f"Enter the new longitude (current: {waypoint.longitude}): ") or waypoint.longitude)
               new_elevation = float(input(f"Enter the new elevation (current: {waypoint.elevation}): ") or waypoint.elevation)
               
               waypoint.name = new_name
               waypoint.latitude = new_latitude
               waypoint.longitude = new_longitude
               waypoint.elevation = new_elevation
               
               print(f"Waypoint '{name}' updated successfully.")
               break
     else:
          print(f"Waypoint '{name}' not found.")
     
     input("Press Enter to return to the waypoints menu...")

def remove_timestamp(gpx):
    
    cls()

    name = input("Enter the name of the waypoint to remove the timestamp from: ")
    for waypoint in gpx.waypoints:
        if waypoint.name == name:
            waypoint.time = None
            print(f"Timestamp removed from waypoint '{name}'.")
            break
    else:
        print(f"Waypoint '{name}' not found.")
