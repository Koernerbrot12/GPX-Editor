import folium
from commands import cls
import gpxpy
import webbrowser
def grafic(gpx_file):
    while True:
        print("1. Show track on map")
        print("2. Show route on map")
        print("3. Exit to menu")
        choice = input("Please select an option (1-3): ")

        if choice == '1':
            track_show(gpx_file)
        elif choice == '2':
            route_show(gpx_file)
        elif choice == '3':
            print("Exiting to menu.")
            return
        else:  
            print("Invalid selection, please try again.")
        cls()
            
def track_show(gpx_file):
    if not gpx_file.tracks:
        print("No tracks available to display.")
        return
    
    track_names = [track.name for track in gpx_file.tracks]
    print("Available Tracks:")
    for i, name in enumerate(track_names, start=1):
        print(f"{i}. {name}")
    track_index = input("Select a track by number (or 'q' to quit): ")
    if track_index.lower() == 'q':
        print("Exiting track display.")
        return

    track = gpx_file.tracks[int(track_index) - 1]
    if not track.segments:
        print("Selected track has no segments.")
        return
    print(f"Displaying track: {track.name}")

    # Create a map centered around the first point of the track
    start_point = track.segments[0].points[0]
    m = folium.Map(location=[start_point.latitude, start_point.longitude], zoom_start=13)

    # Add the track to the map
    track_points = [(point.latitude, point.longitude) for segment in track.segments for point in segment.points]
    folium.PolyLine(
        locations=track_points,
        color='blue',
        weight=2.5,
        opacity=1
    ).add_to(m)

    # Save the map to an HTML file
    m.save('track_map.html')
    print("Track map saved as 'track_map.html'.")
    display_map = input("Do you want to open the map in your browser? (yes/no): ")
    if display_map.lower() == 'yes':
        webbrowser.open('track_map.html')
    else:
        print("Map not opened in browser.")
        return

def route_show(gpx_file):
    if not gpx_file.routes:
        print("No routes available to display.")
        return
    
    route_names = [route.name for route in gpx_file.routes]
    print("Available Routes:")
    for i, name in enumerate(route_names, start=1):
        print(f"{i}. {name}")
    route_index = input("Select a route by number (or 'q' to quit): ")
    if route_index.lower() == 'q':
        print("Exiting route display.")
        return

    route = gpx_file.routes[int(route_index) - 1]
    if not route.points:
        print("Selected route has no points.")
        return
    print(f"Displaying route: {route.name}")

    # Create a map centered around the first point of the route
    start_point = route.points[0]
    m = folium.Map(location=[start_point.latitude, start_point.longitude], zoom_start=13)

    # Add the route to the map
    folium.PolyLine(
        locations=[(point.latitude, point.longitude) for point in route.points],
        color='green',
        weight=2.5,
        opacity=1
    ).add_to(m)

    # Save the map to an HTML file
    m.save('route_map.html')
    print("Route map saved as 'route_map.html'.")
    display_map = input("Do you want to open the map in your browser? (yes/no): ")
    if display_map.lower() == 'yes':
        webbrowser.open('route_map.html')
    else:
        print("Map not opened in browser.")
        return
