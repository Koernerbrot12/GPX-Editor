import gpxpy
from commands import cls

def routes_menu(gpx):


    while True:

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
    # This function prints all routes in the GPX file.
    if gpx.routes:
        for route in gpx.routes:
            print(f"Name: {route.name}, Number of Points: {len(route.points)}")
            for point in route.points:
                print(f"- {point.name} (Latitude: {point.latitude}, Longitude: {point.longitude}, Elevation: {point.elevation})")
    else:
        print("No routes found in the GPX file.")
    
    input("Press Enter to return to the routes menu...")

def add_route(gpx):
    """
    This function allows the user to add a route to the GPX file.
    """
    cls()
    route_name = input("Enter the name of the route: ")
    if route_name == "":
        print("Name cannot be empty. Please try again.")
        return
    if any(route.name == route_name for route in gpx.routes):
        print(f"A route with the name '{route_name}' already exists. Please choose a different name.")
        return
    route = gpxpy.gpx.GPXRoute(name=route_name)
    
    # Print available waypoints
    if not gpx.waypoints:
        print("No waypoints available to add to the route.")
        input("Press Enter to return to the routes menu...")
        return
    print("Available Waypoints:")
    for waypoint in gpx.waypoints:
        print(f"- {waypoint.name} (Latitude: {waypoint.latitude}, Longitude: {waypoint.longitude}, Elevation: {waypoint.elevation})")

    while True:
        route_point_name = input("Enter a waypoint name to add to the route (or type 'done' when finished): ")
        if route_point_name.lower() == 'done':
            break

        found = False
        for waypoint in gpx.waypoints:
            if waypoint.name == route_point_name:
                route.points.append(waypoint)  # Append the waypoint object itself
                print(f"Waypoint '{route_point_name}' added to Route '{route_name}' successfully.")
                found = True
                break
        if not found:
            print(f"Waypoint '{route_point_name}' not found.")
        
    
    gpx.routes.append(route)
    print(f"Route '{route_name}' added successfully.")
    input("Press Enter to return to the routes menu...")

def delete_route(gpx):
    """
    This function allows the user to delete a route from the GPX file.
    """
    cls()
    if not gpx.routes:
        print("No routes available to delete.")
        input("Press Enter to return to the routes menu...")
        return

    print("Available Routes:")
    for route in gpx.routes:
        print(f"- {route.name}")
    print("Type the name of the route you want to delete (or type 'cancel' to cancel): ")
    route_name = input("Enter the route name: ")
    if route_name.lower() == 'cancel':
        print("Deletion cancelled.")
        input("Press Enter to return to the routes menu...")
        return
    for route in gpx.routes:
        if route.name == route_name:
            gpx.routes.remove(route)
            print(f"Route '{route_name}' deleted successfully.")
            input("Press Enter to return to the routes menu...")
            return
        
   

    input("Press Enter to return to the routes menu...")

def update_route(gpx):
    cls()
    if not gpx.routes:
        print("No routes available to update.")
        input("Press Enter to return to the routes menu...")
        return

    print("Available Routes:")
    for route in gpx.routes:
        print(f"- {route.name}")
    
    update_route_name = input("Enter the name of the route you want to update: ")
    
    # Find the selected route
    selected_route = None
    for route in gpx.routes:
        if route.name == update_route_name:
            selected_route = route
            break
    
    if selected_route is None:
        print(f"Route '{update_route_name}' not found.")
        input("Press Enter to return to the routes menu...")
        return

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

    cls()
    # print the current points in the route
    if not route.points:
        print("No points in this route to update.")
        input("Press Enter to return to the update menu...")
        return
    print("Current Route Points:")
    for point in route.points:
                print(f" Name: {point.name if point.name else 'Unnamed'}, Latitude: {point.latitude}, Longitude: {point.longitude}, Elevation: {point.elevation}")
                 

    # enter the name of the waypoint to update
    waypoint_name = input("Enter the name of the waypoint to update (or type 'cancel' to cancel): ")
    if waypoint_name.lower() == 'cancel':
        print("Update cancelled.")
        input("Press Enter to return to the update menu...")
        return
    found = False
    for point in route.points:
        if point.name == waypoint_name:
            found = True
            # update the point's latitude, longitude, and elevation, or keeo current values if the user presses Enter without inputting a new value
            point.name = str(input("Enter new name for the waypoint (or press Enter to keep current name): ") or point.name)
            waypoint_name = point.name  # Update the name variable to reflect the new name
            point.latitude = float(input("Enter new latitude: ") or point.latitude) 
            point.longitude = float(input("Enter new longitude: ") or point.longitude)
            point.elevation = float(input("Enter new elevation: ") or point.elevation)
            print(f"Waypoint '{waypoint_name}' updated successfully.")
            break
    if not found:
        print(f"Waypoint '{waypoint_name}' not found in the route.")
    input("Press Enter to return to the update menu...")


def insert_route_point(gpx, route):
    cls()
    # This function allows the user to insert a new waypoint into the route and let them choose where to insert it, the waypoint has to be added before, in the waypoints menu.
    #
    if not gpx.waypoints:
        print("No waypoints available to add to the route.")
        input("Press Enter to return to the update menu...")
        return
    print("Available Waypoints:")
    for waypoint in gpx.waypoints:
        print(f"- {waypoint.name} (Latitude: {waypoint.latitude}, Longitude: {waypoint.longitude}, Elevation: {waypoint.elevation})")
    waypoint_name = input("Enter the name of the waypoint to insert into the route (or type 'cancel' to cancel): ")
    if waypoint_name.lower() == 'cancel':
        print("Insertion cancelled.")
        input("Press Enter to return to the update menu...")
        return
    found = False
    # Now the routepoints are printed, the user can choose where to insert the new waypoint, "start" will insert it at the beginning, "end" will insert it at the end, and any other waypoint name will insert it after that position.
    for waypoint in gpx.waypoints:
        if waypoint.name == waypoint_name:
            found = True
            position = input("Enter the position to insert the waypoint (start, end, or after a specific waypoint name): ")
            if position.lower() == 'start':
                route.points.insert(0, waypoint)
                print(f"Waypoint '{waypoint_name}' inserted at the start of the route.")
            elif position.lower() == 'end':
                route.points.append(waypoint)
                print(f"Waypoint '{waypoint_name}' inserted at the end of the route.")
            else:
                for i, point in enumerate(route.points):
                    if point.name == position:
                        route.points.insert(i + 1, waypoint)
                        print(f"Waypoint '{waypoint_name}' inserted after '{position}'.")
                        break
                else:
                    print(f"Waypoint '{position}' not found in the route. Insertion failed.")
            break
    if not found:
        print(f"Waypoint '{waypoint_name}' not found in the GPX file. Insertion failed.")
    input("Press Enter to return to the update menu...")

    
def delete_route_point(gpx, route):
    cls()
    # This function allows the user to delete a point from the route.
    if not route.points:
        print("No points in this route to delete.")
        input("Press Enter to return to the update menu...")
        return

    print("Current Route Points:")
    for point in route.points:
        print(f"- {point.name} (Latitude: {point.latitude}, Longitude: {point.longitude}, Elevation: {point.elevation})")
    
    point_name = input("Enter the name of the point to delete (or type 'cancel' to cancel): ")
    if point_name.lower() == 'cancel':
        print("Deletion cancelled.")
        input("Press Enter to return to the update menu...")
        return
    
    for point in route.points:
        if point.name == point_name:
            route.points.remove(point)
            print(f"Point '{point_name}' deleted successfully.")
            break
    else:
        print(f"Point '{point_name}' not found in the route.")
    
    input("Press Enter to return to the update menu...")
