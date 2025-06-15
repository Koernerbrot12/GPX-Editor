from fpdf import FPDF
import gpxpy
from commands import cls


def converter_function(file_or_gpx):
    # If a string is passed, treat it as a file path and parse it
    if isinstance(file_or_gpx, str):
        with open(file_or_gpx, 'r') as gpx_file:
            gpx = gpxpy.parse(gpx_file)
    else:
        gpx = file_or_gpx  # Assume it's already a GPX object

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="GPX Waypoints", ln=True, align='C')

    if gpx.waypoints:
        for wp in gpx.waypoints:
            pdf.cell(200, 10, txt=f"Name: {wp.name}, Lat: {wp.latitude}, Lon: {wp.longitude}", ln=True)
    else:
        pdf.cell(200, 10, txt="No waypoints found.", ln=True)

    pdf.output("output.pdf")

def print_gpx(gpx):
    # Print the contents of a GPX file to the console.
    cls()
    print("GPX File Contents:\n")

    print("Waypoints:")
    if gpx.waypoints:
        for waypoint in gpx.waypoints:
            print(f"Name: {waypoint.name}, Latitude: {waypoint.latitude}, Longitude: {waypoint.longitude}, Elevation: {waypoint.elevation}, Timestamp: {waypoint.time}")

    if not gpx.waypoints:
        # Check if there are no waypoints in the GPX file
        print("No waypoints found in the GPX file.")

    print("End of waypoints.\n")

    print("Tracks:")
    if gpx.tracks:
        for track in gpx.tracks:
            print(f"Name: {track.name}, Number of Segments: {len(track.segments)}")
            for segment_idx, segment in enumerate(track.segments):
                print(f"  Segment {segment_idx + 1}, Number of Points: {len(segment.points)}")
                for point in segment.points:
                    print(f"  - {point.name if point.name else 'Unnamed'} (Latitude: {point.latitude}, Longitude: {point.longitude}, Elevation: {point.elevation})")
    else:
        print("No tracks found in the GPX file.")

    print("End of tracks.\n")

    print("Routes:")
    if gpx.routes:
        for route in gpx.routes:
            print(f"Name: {route.name}, Number of Points: {len(route.points)}")
            for point in route.points:
                print(f"- {point.name} (Latitude: {point.latitude}, Longitude: {point.longitude}, Elevation: {point.elevation})")
    else:
        print("No routes found in the GPX file.")

    print("\nEnd of file.")

    input("Press Enter to return to the menu...")