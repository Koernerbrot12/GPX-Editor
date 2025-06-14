import gpxpy
from commands import cls

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
            return
        else:
            print("Invalid selection, please try again.")

def print_points(gpx):
     
     # This function prints all waypoints in the GPX file.
     cls()
     for waypoint in gpx.waypoints:
         print(f"Name: {waypoint.name}, Latitude: {waypoint.latitude}, Longitude: {waypoint.longitude}, Elevation: {waypoint.elevation}, Timestamp: {waypoint.time}")
            
        
     if not gpx.waypoints:
         # Check if there are no waypoints in the GPX file
         print("No waypoints found in the GPX file.")
         
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
     latitude = float(input("Enter the latitude of the waypoint: "))
     longitude = float(input("Enter the longitude of the waypoint: "))
     elevation = float(input("Enter the elevation of the waypoint (optional, press Enter to skip): ") or 0)
     
     new_waypoint = gpxpy.gpx.GPXWaypoint(latitude, longitude, elevation=elevation, name=name)
     gpx.waypoints.append(new_waypoint)
     
     print(f"Waypoint '{name}' added successfully.")
     input("Press Enter to return to the waypoints menu...")

def delete_waypoint(gpx):
    
    # This function allows the user to delete a waypoint from the GPX file.
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
    
     # This function allows the user to update a waypoint in the GPX file.
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
