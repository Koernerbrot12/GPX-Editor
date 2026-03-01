import gpxpy
from commands import cls

def routes_menu(gpx):


    while True:
        # This function displays the routes menu and allows the user to manage routes in the GPX file.
        # It provides options to show, add, delete, and update routes.


        cls()
        print("Routes Menu")
        print("1. Show Routes")
        print("2. Add Route")
        print("3. Delete Route")
        print("4. Update Route")
        print("5. Back to GPX Menu")

        choice = input("Please select an option (1-5): ")
        if choice == '1':
            print_routes(gpx)
        elif choice == '2':
            add_route(gpx)
        elif choice == '3':
            delete_route(gpx)
        elif choice == '4':
            update_route(gpx)
        elif choice == '5':
            cls()
            print("Returning to the GPX menu...")
            return
        else:
            print("Invalid selection, please try again.")


def print_routes(gpx):
    cls()
    # This function prints all routes in the GPX file, numbered.
    if gpx.routes:
        for idx, route in enumerate(gpx.routes, start=1):
            print(f"{idx}. Name: {route.name}, Number of Points: {len(route.points)}")
            for point in route.points:
                print(f"- {point.name} (Latitude: {point.latitude}, Longitude: {point.longitude}, Elevation: {point.elevation})")
    else:
        print("No routes found in the GPX file.")
    input("Press Enter to return to the routes menu...")


def add_route(gpx):
    
    #This function allows the user to add a route to the GPX file using existing waypoints.
    
    cls()
    route_name = input("Enter the name of the route: ")
    if route_name == "":
        print("Name cannot be empty. Please try again.")
        return
    if any(route.name == route_name for route in gpx.routes):
        print(f"A route with the name '{route_name}' already exists. Please choose a different name.")
        return
    route = gpxpy.gpx.GPXRoute(name=route_name)
    
    # Print available waypoints with numbers
    if not gpx.waypoints:
        print("No waypoints available to add to the route.")
        input("Press Enter to return to the routes menu...")
        return
    print("Available Waypoints:")
    for idx, waypoint in enumerate(gpx.waypoints, start=1):
        print(f"{idx}. {waypoint.name} (Latitude: {waypoint.latitude}, Longitude: {waypoint.longitude}, Elevation: {waypoint.elevation})")

    while True:
        selection = input("Enter the number of the waypoint to add to the route (or type 'done' when finished): ")
        if selection.lower() == 'done':
            break

        if not selection.isdigit() or not (1 <= int(selection) <= len(gpx.waypoints)):
            print("Invalid selection. Please enter a valid number.")
            continue

        idx = int(selection) - 1
        waypoint = gpx.waypoints[idx]
        route.points.append(waypoint)
        print(f"Waypoint '{waypoint.name}' added to Route '{route_name}' successfully.")

    gpx.routes.append(route)
    print(f"Route '{route_name}' added successfully.")
    input("Press Enter to return to the routes menu...")

def delete_route(gpx):
    
    #This function allows the user to delete a route from the GPX file.
    
    cls()
    if not gpx.routes:
        print("No routes available to delete.")
        input("Press Enter to return to the routes menu...")
        return

    print("Available Routes:")
    for idx, route in enumerate(gpx.routes, start=1):
        print(f"{idx}. {route.name}")
    selection = input("Enter the number of the route to delete (or type 'cancel' to cancel): ")
    if selection.lower() == 'cancel':
        print("Deletion cancelled.")
        input("Press Enter to return to the routes menu...")
        return
    if not selection.isdigit() or not (1 <= int(selection) <= len(gpx.routes)):
        print("Invalid selection. Please enter a valid number.")
        input("Press Enter to return to the routes menu...")
        return
    idx = int(selection) - 1
    route = gpx.routes.pop(idx)
    print(f"Route '{route.name}' deleted successfully.")
    input("Press Enter to return to the routes menu...")


def update_route(gpx):
    cls()
    if not gpx.routes:
        print("No routes available to update.")
        input("Press Enter to return to the routes menu...")
        return

    print("Available Routes:")
    for idx, route in enumerate(gpx.routes, start=1):
        print(f"{idx}. {route.name}")
    selection = input("Enter the number of the route you want to update (or type 'cancel' to cancel): ")
    if selection.lower() == 'cancel':
        print("Update cancelled.")
        input("Press Enter to return to the routes menu...")
        return
    if not selection.isdigit() or not (1 <= int(selection) <= len(gpx.routes)):
        print("Invalid selection. Please enter a valid number.")
        input("Press Enter to return to the routes menu...")
        return
    idx = int(selection) - 1
    selected_route = gpx.routes[idx]

    while True:
        cls()
        print(f"Updating Route: {selected_route.name}")
        print("Update Menu")
        print("1. Update Route Name")
        print("2. Update Route Points")
        print("3. Insert new Route point")
        print("4. Delete Route point")
        print("5. Back to Routes Menu")

        choice = input("Please select an option (1-6): ")
        if choice == '1':
            change_route_name(gpx, selected_route)
        elif choice == '2':
            update_route_points(gpx, selected_route)
        elif choice == '3':
            insert_route_point(gpx, selected_route)
        elif choice == '4':
            delete_route_point(gpx, selected_route)
        elif choice == '5':
            cls()
            print("Returning to the Routes menu...")
            return
        else:
            print("Invalid selection, please try again.")

def change_route_name(gpx, route):
    """
    This function updates the name of a selected route.
    """
    cls()
    print(f"Current route name: {route.name}")
    new_name = input("Enter the new name for the route (or type 'cancel' to cancel): ")
    
    if new_name.lower() == 'cancel':
        print("Update cancelled.")
    else:
        route.name = new_name
        print(f"Route name updated to '{new_name}' successfully.")
    
    input("Press Enter to return to the update menu...")


def update_route_points(gpx, route):
    
    #Allows the user to update the properties of a route point.
    
    cls()
    # Print the current points in the route with numbers
    if not route.points:
        print("No points in this route to update.")
        input("Press Enter to return to the update menu...")
        return
    print("Current Route Points:")
    for idx, point in enumerate(route.points, start=1):
        print(f"{idx}. Name: {point.name if point.name else 'Unnamed'}, Latitude: {point.latitude}, Longitude: {point.longitude}, Elevation: {point.elevation}")

    selection = input("Enter the number of the waypoint to update (or type 'cancel' to cancel): ")
    if selection.lower() == 'cancel':
        print("Update cancelled.")
        input("Press Enter to return to the update menu...")
        return

    if not selection.isdigit() or not (1 <= int(selection) <= len(route.points)):
        print("Invalid selection. Please enter a valid number.")
        input("Press Enter to return to the update menu...")
        return

    idx = int(selection) - 1
    point = route.points[idx]

    # Update the point's latitude, longitude, and elevation, or keep current values if the user presses Enter without inputting a new value
    point.name = str(input("Enter new name for the waypoint (or press Enter to keep current name): ") or point.name)
    point.latitude = float(input("Enter new latitude: ") or point.latitude)
    point.longitude = float(input("Enter new longitude: ") or point.longitude)
    point.elevation = float(input("Enter new elevation: ") or point.elevation)
    print(f"Waypoint '{point.name}' updated successfully.")

    input("Press Enter to return to the update menu...")

def insert_route_point(gpx, route):
    
    #Allows the user to insert a waypoint into the route at a specified position.
   
    cls()
    # Check if there are waypoints to insert
    if not gpx.waypoints:
        print("No waypoints available to add to the route.")
        input("Press Enter to return to the update menu...")
        return

    print("Available Waypoints:")
    for idx, waypoint in enumerate(gpx.waypoints, start=1):
        print(f"{idx}. {waypoint.name} (Latitude: {waypoint.latitude}, Longitude: {waypoint.longitude}, Elevation: {waypoint.elevation})")

    selection = input("Enter the number of the waypoint to insert into the route (or type 'cancel' to cancel): ")
    if selection.lower() == 'cancel':
        print("Insertion cancelled.")
        input("Press Enter to return to the update menu...")
        return

    if not selection.isdigit() or not (1 <= int(selection) <= len(gpx.waypoints)):
        print("Invalid selection. Please enter a valid number.")
        input("Press Enter to return to the update menu...")
        return

    waypoint = gpx.waypoints[int(selection) - 1]

    # Show current route points with numbers for position selection
    print("Current Route Points:")
    if not route.points:
        print("Route is currently empty. The waypoint will be added as the first point.")
        route.points.append(waypoint)
        print(f"Waypoint '{waypoint.name}' inserted as the first point in the route.")
        input("Press Enter to return to the update menu...")
        return

    for idx, point in enumerate(route.points, start=1):
        print(f"{idx}. {point.name} (Latitude: {point.latitude}, Longitude: {point.longitude}, Elevation: {point.elevation})")

    pos_input = input("Enter the position number to insert before (1 for start, or one past the last number for end): ")
    if not pos_input.isdigit() or not (1 <= int(pos_input) <= len(route.points) + 1):
        print("Invalid position. Insertion failed.")
        input("Press Enter to return to the update menu...")
        return

    insert_idx = int(pos_input) - 1
    route.points.insert(insert_idx, waypoint)
    print(f"Waypoint '{waypoint.name}' inserted at position {insert_idx + 1} in the route.")

    input("Press Enter to return to the update menu...")

def delete_route_point(gpx, route):
   
    #Allows the user to delete a point from the route.
    
    cls()
    # Check if there are points to delete
    if not route.points:
        print("No points in this route to delete.")
        input("Press Enter to return to the update menu...")
        return

    print("Current Route Points:")
    for idx, point in enumerate(route.points, start=1):
        print(f"{idx}. {point.name} (Latitude: {point.latitude}, Longitude: {point.longitude}, Elevation: {point.elevation})")
    
    selection = input("Enter the number of the point to delete (or type 'cancel' to cancel): ")
    if selection.lower() == 'cancel':
        print("Deletion cancelled.")
        input("Press Enter to return to the update menu...")
        return

    if not selection.isdigit() or not (1 <= int(selection) <= len(route.points)):
        print("Invalid selection. Please enter a valid number.")
        input("Press Enter to return to the update menu...")
        return

    idx = int(selection) - 1
    point = route.points.pop(idx)
    print(f"Point '{point.name}' deleted successfully.")

    input("Press Enter to return to the update menu...")

