import folium
from commands import cls
import gpxpy
import webbrowser
import os

def grafic(gpx_file):

    while True:

        # small menu to give the user the option to show a track or a route

        cls()
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

    # This function displays the available tracks in the GPX file and allows the user to select one to display on a map.

    #first checks if the GPX file has any tracks available to display

    if not gpx_file.tracks:                                                                                          
        print("No tracks available to display.")
        input("Press Enter to return to the menu...")                                            
        return
                                              
    # looks for the names of the tracks in the GPX file and printes them

    track_names = [track.name for track in gpx_file.tracks]                                                          
    print("Available Tracks:")

    # gives them a number to select them
                                             
    for i, name in enumerate(track_names, start=1):                                                                  
        print(f"{i}. {name}")

    # gives the user the option to exit the track display by typing 'q'
                                     
    track_index = input("Select a track by number (or 'q' to quit): ")                                          
    if track_index.lower() == 'q':                                                                                    
        print("Exiting track display.")                                         
        return
    
    # checks if the input is a number and if it is in the range of the available tracks
                                             
    if not track_index.isdigit() or int(track_index) < 1 or int(track_index) > len(gpx_file.tracks):
        print("Invalid track selection. Please enter a valid number.")
        return
    
    # saves the selcted track based on the user's input and checks if the selected track isnt empty

    track = gpx_file.tracks[int(track_index) - 1]                                                                     
    if not track.segments:                                                                                           
        print("Selected track has no segments.")
        return
    print(f"Displaying track: {track.name}")

    # Create a map centered around the first point of the track

    start_point = track.segments[0].points[0]                                                                        # reads in the first point of the track to center the map
    m = folium.Map(location=[start_point.latitude, start_point.longitude], zoom_start=13)                            # creates a map with folium, using the first point of the track as the center and a zoom level of 13

    # Add the track and his points in a segment to the map

    track_points = [(point.latitude, point.longitude) for segment in track.segments for point in segment.points]
    folium.PolyLine(
        locations=track_points,
        color='blue',
        weight=2.5,
        opacity=1
    ).add_to(m)

    # saving the map to an HTML file for later use or display

    while True:
        cls()
        print("Do you want to save the HTML file?")
        print("")
        print("1. Yes")
        print("2. No")

        save_choice = input("Please select an option (1-2): ")

        if save_choice == '1':
            save_path = input("Enter the path where you want to save the HTML file (default is 'track_map.html'): ")
            if not save_path:
                save_path = 'track_map.html'
            if save_path.endswith('.html') or save_path.endswith('.htm'):
                m.save(save_path)
                print(f"HTML file saved successfully to {save_path}.")
                print("You can now close the program or continue editing.")
                input("Press Enter to return to the menu...")
                cls()

                # asks the user if he wants to open the map in the browser

                display_map = input("Do you want to open the map in your browser? \n1. yes \n0. no \nPlease select an option (1-0): ")
                if display_map.lower() == '1':
                    webbrowser.open(save_path)
                elif display_map.lower() == '0':
                    print("Map not opened in browser.")
                else:
                    print("Invalid input, map not opened in browser.")
                input("Press Enter to return to the menu...")
                cls()
                return save_path
            else:
                dir_path = save_path
                if not dir_path.endswith('/') and not dir_path.endswith('\\'):
                    dir_path += '/'
                file_name = input("Enter the name of the HTML file (without extension): ")
                if not file_name.endswith('.html') and not file_name.endswith('.htm'):
                    file_name += '.html'
                full_path = os.path.join(dir_path, file_name)
                m.save(full_path)
                print(f"HTML file saved successfully to {full_path}.")

                # asks the user if he wants to open the map in the browser

                display_map = input("Do you want to open the map in your browser? \n1. yes \n0. no \nPlease select an option (1-0):")
                if display_map.lower() == '1':
                    webbrowser.open(full_path)
                elif display_map.lower() == '0':
                    print("Map not opened in browser.")
                else:
                    print("Invalid input, map not opened in browser.")
                input("Press Enter to return to the menu...")
                cls()
                return full_path
        elif save_choice == '2':
            print("Save operation canceled.")
            cls()
            break
        else:
            print("Invalid selection, please try again.")

def route_show(gpx_file):

    # This function operates similarly to the track_show function, but it displays routes instead of tracks.
    
    if not gpx_file.routes:
        print("No routes available to display.")
        input("Press Enter to return to the menu...")
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

    start_point = route.points[0]                                                               # reads in the first point of the route to center the map   
    m = folium.Map(location=[start_point.latitude, start_point.longitude], zoom_start=13)       # creates a map on the first point of the route

    # Add the route to the map

    folium.PolyLine(
        locations=[(point.latitude, point.longitude) for point in route.points],
        color='green',
        weight=2.5,
        opacity=1
    ).add_to(m)

    # saving the map to an HTML file for later use or display

    while True:
        cls()
        print("Do you want to save the HTML file?")
        print("")
        print("1. Yes")
        print("2. No")

        save_choice = input("Please select an option (1-2): ")

        if save_choice == '1':
            save_path = input("Enter the path where you want to save the HTML file (default is 'route_map.html'): ")
            if not save_path:
                save_path = 'route_map.html'
            if save_path.endswith('.html') or save_path.endswith('.htm'):
                m.save(save_path)
                print(f"HTML file saved successfully to {save_path}.")

                # asks the user if he wants to open the map in the browser

                display_map = input("Do you want to open the map in your browser? \n1. yes \n0. no \nPlease select an option (1-0): ")
                if display_map.lower() == '1':
                    webbrowser.open(save_path)
                elif display_map.lower() == '0':
                    print("Map not opened in browser.")
                else:
                    print("Invalid input, map not opened in browser.")

                input("Press Enter to return to the menu...")
                cls()
                return save_path
            else:
                dir_path = save_path
                if not dir_path.endswith('/') and not dir_path.endswith('\\'):
                    dir_path += '/'
                file_name = input("Enter the name of the HTML file (without extension): ")
                if not file_name.endswith('.html') and not file_name.endswith('.htm'):
                    file_name += '.html'
                full_path = os.path.join(dir_path, file_name)
                m.save(full_path)
                print(f"HTML file saved successfully to {full_path}.")

                # asks the user if he wants to open the map in the browser

                display_map = input("Do you want to open the map in your browser? \n1. yes \n0. no \nPlease select an option (1-0): ") 
                if display_map.lower() == '1':
                    webbrowser.open(full_path)
                elif display_map.lower() == '0':
                    print("Map not opened in browser.")

                input("Press Enter to return to the menu...")
                cls()
                return full_path
        elif save_choice == '2':
            print("Save operation canceled.")
            cls()
            break
        else:
            print("Invalid selection, please try again.")
            cls()