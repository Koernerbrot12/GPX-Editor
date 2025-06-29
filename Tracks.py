import gpxpy
from commands import cls

def tracks_menu(gpx):
    # This function displays the tracks menu and allows the user to manage tracks in the GPX file.
    # It provides options to show, add, delete, and update tracks.

    while True:
        cls()
        print("Tracks Menu")
        print("1. Show Tracks")
        print("2. Add Track")
        print("3. Delete Track")
        print("4. Update Track")
        print("5. Back to GPX Menu")

        choice = input("Please select an option (1-5): ")
        if choice == '1':
            print_tracks(gpx)
        elif choice == '2':
            add_track(gpx)
        elif choice == '3':
            delete_track(gpx)
        elif choice == '4':
            update_track(gpx)
        elif choice == '5':
            cls()
            print("Returning to the GPX menu...")
            return
        else:
            print("Invalid selection, please try again.")

def print_tracks(gpx):
    # This function prints the details of all tracks in the GPX file.
    # It displays the name of each track, the number of segments, and the points in each segment.
    cls()
    if gpx.tracks:
        for idx, track in enumerate(gpx.tracks, start=1):
            print(f"{idx}. Name: {track.name}, Number of Segments: {len(track.segments)}")
            for segment_idx, segment in enumerate(track.segments):
                print(f"  Segment {segment_idx + 1}, Number of Points: {len(segment.points)}")
                for point in segment.points:
                    print(f"  - {point.name if point.name else 'Unnamed'} (Latitude: {point.latitude}, Longitude: {point.longitude}, Elevation: {point.elevation})")
    else:
        print("No tracks found in the GPX file.")
    
    input("Press Enter to return to the tracks menu...")

def add_track(gpx):
    
    #Allows the user to add a track to the GPX file.
    
    cls()
    track_name = input("Enter the name of the track: ")
    if track_name == "":
        print("Name cannot be empty. Please try again.")
        return
    if any(track.name == track_name for track in gpx.tracks):
        print(f"A track with the name '{track_name}' already exists. Please choose a different name.")
        return

    track = gpxpy.gpx.GPXTrack(name=track_name)
    segment = gpxpy.gpx.GPXTrackSegment()

    # Print available waypoints with numbers
    if not gpx.waypoints:
        print("No waypoints available to add to the track.")
        input("Press Enter to return to the tracks menu...")
        return
    print("Available Waypoints:")
    for idx, waypoint in enumerate(gpx.waypoints, start=1):
        print(f"{idx}. {waypoint.name} (Latitude: {waypoint.latitude}, Longitude: {waypoint.longitude}, Elevation: {waypoint.elevation})")

    while True:
        selection = input("Enter the number of the waypoint to add to the track (or type 'done' when finished): ")
        if selection.lower() == 'done':
            break

        if not selection.isdigit() or not (1 <= int(selection) <= len(gpx.waypoints)):
            print("Invalid selection. Please enter a valid number.")
            continue

        idx = int(selection) - 1
        waypoint = gpx.waypoints[idx]

       
        segment.points.append(waypoint)
        print(f"Waypoint '{waypoint.name}' added to Track '{track_name}' successfully.")

    if not segment.points:
        print("No points added to the track. Track not created.")
        input("Press Enter to return to the tracks menu...")
        return

    track.segments.append(segment)
    gpx.tracks.append(track)
    print(f"Track '{track_name}' added successfully.")
    input("Press Enter to return to the tracks menu...")

        

def delete_track(gpx):
    # Allows the user to delete a track from the GPX file.
    # It lists all available tracks and prompts the user to select one for deletion by number.
    cls()
    if not gpx.tracks:
        print("No tracks available to delete.")
        input("Press Enter to return to the tracks menu...")
        return

    print("Available Tracks:")
    for idx, track in enumerate(gpx.tracks, start=1):
        print(f"{idx}. {track.name}")
    selection = input("Enter the number of the track to delete (or type 'cancel' to cancel): ")
    if selection.lower() == 'cancel':
        print("Deletion cancelled.")
        input("Press Enter to return to the tracks menu...")
        return
    if not selection.isdigit() or not (1 <= int(selection) <= len(gpx.tracks)):
        print("Invalid selection. Please enter a valid number.")
        input("Press Enter to return to the tracks menu...")
        return
    idx = int(selection) - 1
    track = gpx.tracks.pop(idx)
    print(f"Track '{track.name}' deleted successfully.")
    input("Press Enter to return to the tracks menu...")


def update_track(gpx):
    # Allows the user to update an existing track in the GPX file.
    # It provides options to change the track name, update points, insert new points, or delete points.

    cls()
    if not gpx.tracks:
        print("No tracks available to update.")
        input("Press Enter to return to the tracks menu...")
        return

    print("Available Tracks:")
    for idx, track in enumerate(gpx.tracks, start=1):
        print(f"{idx}. {track.name}")
    selection = input("Enter the number of the track you want to update (or type 'cancel' to cancel): ")
    if selection.lower() == 'cancel':
        print("Update cancelled.")
        input("Press Enter to return to the tracks menu...")
        return
    if not selection.isdigit() or not (1 <= int(selection) <= len(gpx.tracks)):
        print("Invalid selection. Please enter a valid number.")
        input("Press Enter to return to the tracks menu...")
        return
    idx = int(selection) - 1
    selected_track = gpx.tracks[idx]

    while True:
        cls()
        print(f"Updating Track: {selected_track.name}")
        print("Update Menu")
        print("1. Update Track Name")
        print("2. Update Track Points")
        print("3. Insert new Track point")
        print("4. Delete Track point")
        print("5. Back to Tracks Menu")

        choice = input("Please select an option (1-5): ")
        if choice == '1':
            change_track_name(gpx, selected_track)
        elif choice == '2':
            update_track_points(gpx, selected_track)
        elif choice == '3':
            insert_track_point(gpx, selected_track)
        elif choice == '4':
            delete_track_point(gpx, selected_track)
        elif choice == '5':
            cls()
            print("Returning to the Tracks menu...")
            return
        else:
            print("Invalid selection, please try again.")

def change_track_name(gpx, track):
    # Allows the user to change the name of a track.
    # It prompts for a new name and updates the track if valid.
    cls()
    print(f"Current track name: {track.name}")
    new_name = input("Enter the new name for the track (or type 'cancel' to cancel): ")
    
    if new_name.lower() == 'cancel':
        print("Update cancelled.")
    else:
        track.name = new_name
        print(f"Track name updated to '{new_name}' successfully.")
    
    input("Press Enter to return to the update menu...")

def update_track_points(gpx, track):
    #Allows the user to update the properties of a track point.
    
    cls()
    # Ensure the track has at least one segment and points
    if not track.segments or not track.segments[0].points:
        print("No points in this track to update.")
        input("Press Enter to return to the update menu...")
        return

    segment = track.segments[0]

    print("Current Track Points:")
    for idx, point in enumerate(segment.points, start=1):
        print(f"{idx}. Name: {point.name if point.name else 'Unnamed'}, Latitude: {point.latitude}, Longitude: {point.longitude}, Elevation: {point.elevation}")

    selection = input("Enter the number of the track point to update (or type 'cancel' to cancel): ")
    if selection.lower() == 'cancel':
        print("Update cancelled.")
        input("Press Enter to return to the update menu...")
        return

    if not selection.isdigit() or not (1 <= int(selection) <= len(segment.points)):
        print("Invalid selection. Please enter a valid number.")
        input("Press Enter to return to the update menu...")
        return

    idx = int(selection) - 1
    point = segment.points[idx]

    # Update the point's properties, or keep current values if the user presses Enter
    point.name = str(input("Enter new name for the track point (or press Enter to keep current name): ") or point.name)
    point.latitude = float(input("Enter new latitude: ") or point.latitude)
    point.longitude = float(input("Enter new longitude: ") or point.longitude)
    point.elevation = float(input("Enter new elevation: ") or point.elevation)
    print(f"Track point '{point.name}' updated successfully.")

    input("Press Enter to return to the update menu...")

def insert_track_point(gpx, track):
   
    #Allows the user to insert a waypoint into the track at a specified position.
    
    cls()
    # Check if there are waypoints to insert
    if not gpx.waypoints:
        print("No waypoints available to add to the track.")
        input("Press Enter to return to the update menu...")
        return

    print("Available Waypoints:")
    for idx, waypoint in enumerate(gpx.waypoints, start=1):
        print(f"{idx}. {waypoint.name} (Latitude: {waypoint.latitude}, Longitude: {waypoint.longitude}, Elevation: {waypoint.elevation})")

    selection = input("Enter the number of the waypoint to insert into the track (or type 'cancel' to cancel): ")
    if selection.lower() == 'cancel':
        print("Insertion cancelled.")
        input("Press Enter to return to the update menu...")
        return

    if not selection.isdigit() or not (1 <= int(selection) <= len(gpx.waypoints)):
        print("Invalid selection. Please enter a valid number.")
        input("Press Enter to return to the update menu...")
        return

    waypoint = gpx.waypoints[int(selection) - 1]

    # For tracks, we assume a single segment for simplicity
    if not track.segments:
        track.segments.append(gpxpy.gpx.GPXTrackSegment())

    segment = track.segments[0]

    print("Current Track Points:")
    # If the segment has no points, we can directly add the waypoint
    if not segment.points:
        print("Track is currently empty. The waypoint will be added as the first point.")
        segment.points.append(waypoint)
        print(f"Waypoint '{waypoint.name}' inserted as the first point in the track.")
        input("Press Enter to return to the update menu...")
        return

    for idx, point in enumerate(segment.points, start=1):
        print(f"{idx}. {point.name} (Latitude: {point.latitude}, Longitude: {point.longitude}, Elevation: {point.elevation})")

    pos_input = input("Enter the position number to insert before (1 for start, or one past the last number for end): ")
    if not pos_input.isdigit() or not (1 <= int(pos_input) <= len(segment.points) + 1):
        print("Invalid position. Insertion failed.")
        input("Press Enter to return to the update menu...")
        return

    insert_idx = int(pos_input) - 1
    segment.points.insert(insert_idx, waypoint)
    print(f"Waypoint '{waypoint.name}' inserted at position {insert_idx + 1} in the track.")

    input("Press Enter to return to the update menu...")


def delete_track_point(gpx, track):
    
    #Allows the user to delete a point from the first segment of the track.
    
    cls()
    # Ensure the track has at least one segment
    if not track.segments or not track.segments[0].points:
        print("No points in this track to delete.")
        input("Press Enter to return to the update menu...")
        return

    segment = track.segments[0]

    print("Current Track Points:")
    for idx, point in enumerate(segment.points, start=1):
        print(f"{idx}. {point.name if point.name else 'Unnamed'} (Latitude: {point.latitude}, Longitude: {point.longitude}, Elevation: {point.elevation})")

    selection = input("Enter the number of the point to delete (or type 'cancel' to cancel): ")
    if selection.lower() == 'cancel':
        print("Deletion cancelled.")
        input("Press Enter to return to the update menu...")
        return

    if not selection.isdigit() or not (1 <= int(selection) <= len(segment.points)):
        print("Invalid selection. Please enter a valid number.")
        input("Press Enter to return to the update menu...")
        return

    idx = int(selection) - 1
    deleted_point = segment.points.pop(idx)
    print(f"Point '{deleted_point.name if deleted_point.name else 'Unnamed'}' deleted successfully.")

    input("Press Enter to return to the update menu...")

