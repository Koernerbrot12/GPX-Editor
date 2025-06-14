import gpxpy
from commands import cls

def tracks_menu(gpx):
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
    cls()
    if gpx.tracks:
        for track in gpx.tracks:
            print(f"Name: {track.name}, Number of Segments: {len(track.segments)}")
            for segment_idx, segment in enumerate(track.segments):
                print(f"  Segment {segment_idx + 1}, Number of Points: {len(segment.points)}")
                for point in segment.points:
                    print(f"  - {point.name if point.name else 'Unnamed'} (Latitude: {point.latitude}, Longitude: {point.longitude}, Elevation: {point.elevation})")
    else:
        print("No tracks found in the GPX file.")
    
    input("Press Enter to return to the tracks menu...")

def add_track(gpx):
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

    if not gpx.waypoints:
        print("No waypoints available to add to the track.")
        input("Press Enter to return to the tracks menu...")
        return

    print("Available Waypoints:")
    for waypoint in gpx.waypoints:
        print(f"- {waypoint.name} (Latitude: {waypoint.latitude}, Longitude: {waypoint.longitude}, Elevation: {waypoint.elevation})")

    while True:
        track_point_name = input("Enter a waypoint name to add to the track (or type 'done' when finished): ")
        if track_point_name.lower() == 'done':
            break

        found = False
        for waypoint in gpx.waypoints:
            if waypoint.name == track_point_name:
                point = gpxpy.gpx.GPXTrackPoint(
                    latitude=waypoint.latitude,
                    longitude=waypoint.longitude,
                    elevation=waypoint.elevation,
                    name=waypoint.name
                )
                segment.points.append(point)
                print(f"Waypoint '{track_point_name}' added to Track '{track_name}' successfully.")
                found = True
                break
        if not found:
            print(f"Waypoint '{track_point_name}' not found.")

    track.segments.append(segment)
    gpx.tracks.append(track)
    print(f"Track '{track_name}' added successfully.")
    input("Press Enter to return to the tracks menu...")

def delete_track(gpx):
    cls()
    if not gpx.tracks:
        print("No tracks available to delete.")
        input("Press Enter to return to the tracks menu...")
        return

    print("Available Tracks:")
    for track in gpx.tracks:
        print(f"- {track.name}")
    
    track_name = input("Enter the track name to delete (or type 'cancel' to cancel): ")
    if track_name.lower() == 'cancel':
        print("Deletion cancelled.")
        input("Press Enter to return to the tracks menu...")
        return

    for track in gpx.tracks:
        if track.name == track_name:
            gpx.tracks.remove(track)
            print(f"Track '{track_name}' deleted successfully.")
            input("Press Enter to return to the tracks menu...")
            return

    print(f"Track '{track_name}' not found.")
    input("Press Enter to return to the tracks menu...")

def update_track(gpx):
    cls()
    if not gpx.tracks:
        print("No tracks available to update.")
        input("Press Enter to return to the tracks menu...")
        return

    print("Available Tracks:")
    for track in gpx.tracks:
        print(f"- {track.name}")
    
    update_track_name = input("Enter the name of the track you want to update: ")
    
    selected_track = None
    for track in gpx.tracks:
        if track.name == update_track_name:
            selected_track = track
            break
    
    if selected_track is None:
        print(f"Track '{update_track_name}' not found.")
        input("Press Enter to return to the tracks menu...")
        return

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
    cls()
    if not track.segments or not track.segments[0].points:
        print("No points in this track to update.")
        input("Press Enter to return to the update menu...")
        return

    print("Current Track Points:")
    for segment_idx, segment in enumerate(track.segments):
        print(f"Segment {segment_idx + 1}:")
        for point in segment.points:
            print(f"- {point.name if point.name else 'Unnamed'} (Latitude: {point.latitude}, Longitude: {point.longitude}, Elevation: {point.elevation})")

    point_name = input("Enter the name of the point to update (or type 'cancel' to cancel): ")
    if point_name.lower() == 'cancel':
        print("Update cancelled.")
        input("Press Enter to return to the update menu...")
        return

    found = False
    for segment in track.segments:
        for point in segment.points:
            if point.name == point_name:
                found = True
                point.name = input("Enter new name (or press Enter to keep current name): ") or point.name
                point.latitude = float(input("Enter new latitude: ") or point.latitude) 
                point.longitude = float(input("Enter new longitude: ") or point.longitude)
                point.elevation = float(input("Enter new elevation: ") or point.elevation)
                print(f"Point '{point_name}' updated successfully.")
                break
        if found:
            break

    if not found:
        print(f"Point '{point_name}' not found in the track.")
    input("Press Enter to return to the update menu...")

def insert_track_point(gpx, track):
    cls()
    if not gpx.waypoints:
        print("No waypoints available to add to the track.")
        input("Press Enter to return to the update menu...")
        return

    print("Available Waypoints:")
    for waypoint in gpx.waypoints:
        print(f"- {waypoint.name} (Latitude: {waypoint.latitude}, Longitude: {waypoint.longitude}, Elevation: {waypoint.elevation})")

    waypoint_name = input("Enter the name of the waypoint to insert into the track (or type 'cancel' to cancel): ")
    if waypoint_name.lower() == 'cancel':
        print("Insertion cancelled.")
        input("Press Enter to return to the update menu...")
        return

    # Create new segment if track has none
    if not track.segments:
        track.segments.append(gpxpy.gpx.GPXTrackSegment())

    found = False
    for waypoint in gpx.waypoints:
        if waypoint.name == waypoint_name:
            found = True
            position = input("Enter the position to insert the point (start, end, or after a specific point name): ")
            new_point = gpxpy.gpx.GPXTrackPoint(
                latitude=waypoint.latitude,
                longitude=waypoint.longitude,
                elevation=waypoint.elevation,
                name=waypoint.name
            )

            if position.lower() == 'start':
                track.segments[0].points.insert(0, new_point)
                print(f"Point '{waypoint_name}' inserted at the start of the track.")
            elif position.lower() == 'end':
                track.segments[0].points.append(new_point)
                print(f"Point '{waypoint_name}' inserted at the end of the track.")
            else:
                for i, point in enumerate(track.segments[0].points):
                    if point.name == position:
                        track.segments[0].points.insert(i + 1, new_point)
                        print(f"Point '{waypoint_name}' inserted after '{position}'.")
                        break
                else:
                    print(f"Point '{position}' not found in the track. Insertion failed.")
            break

    if not found:
        print(f"Waypoint '{waypoint_name}' not found in the GPX file.")
    input("Press Enter to return to the update menu...")

def delete_track_point(gpx, track):
    cls()
    if not track.segments or not track.segments[0].points:
        print("No points in this track to delete.")
        input("Press Enter to return to the update menu...")
        return

    print("Current Track Points:")
    for segment_idx, segment in enumerate(track.segments):
        print(f"Segment {segment_idx + 1}:")
        for point in segment.points:
            print(f"- {point.name if point.name else 'Unnamed'} (Latitude: {point.latitude}, Longitude: {point.longitude}, Elevation: {point.elevation})")

    point_name = input("Enter the name of the point to delete (or type 'cancel' to cancel): ")
    if point_name.lower() == 'cancel':
        print("Deletion cancelled.")
        input("Press Enter to return to the update menu...")
        return

    found = False
    for segment in track.segments:
        for point in segment.points:
            if point.name == point_name:
                segment.points.remove(point)
                print(f"Point '{point_name}' deleted successfully.")
                found = True
                break
        if found:
            break

    if not found:
        print(f"Point '{point_name}' not found in the track.")
    input("Press Enter to return to the update menu...")