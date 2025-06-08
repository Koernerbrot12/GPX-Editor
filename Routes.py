import gpxpy
from commands import cls

def routes_menu(gpx):

 

  
    cls()
    print("Routes Menu")
    print("1. Show Routes")
    print("2. Add Route")
    print("3. Delete Route")
    print("4. Update Route")
    print("5. Back to GPX Menu")

    while True:
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
                print(f"  Point: Latitude: {point.latitude}, Longitude: {point.longitude}, Elevation: {point.elevation}")
    else:
        print("No routes found in the GPX file.")
    
    input("Press Enter to return to the routes menu...")

def add_route(gpx):
    """
    This function allows the user to add a route to the GPX file.
    """
    cls()
    route_name = input("Enter the name of the route: ")
    route = gpxpy.gpx.GPXRoute(name=route_name)
    

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