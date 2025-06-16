import gpxpy
import os
from fpdf import FPDF
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
    pdf.ln(10)

    # Add GPX data to PDF
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, "Waypoints:", ln=True)
    if gpx.waypoints:
        for waypoint in gpx.waypoints:
            wp_text = f"Name: {waypoint.name}, Latitude: {waypoint.latitude}, Longitude: {waypoint.longitude}, Elevation: {waypoint.elevation}, Timestamp: {waypoint.time}"
            pdf.multi_cell(0, 10, wp_text)
    else:
        pdf.cell(0, 10, "No waypoints found in the GPX file.", ln=True)

    pdf.cell(0, 10, "End of waypoints.", ln=True)
    pdf.ln(5)

    pdf.cell(0, 10, "Tracks:", ln=True)
    if gpx.tracks:
        for track in gpx.tracks:
            track_text = f"Name: {track.name}, Number of Segments: {len(track.segments)}"
            pdf.multi_cell(0, 10, track_text)
            for segment_idx, segment in enumerate(track.segments):
                seg_text = f"  Segment {segment_idx + 1}, Number of Points: {len(segment.points)}"
                pdf.multi_cell(0, 10, seg_text)
                for point in segment.points:
                    pt_text = f"    - {point.name if point.name else 'Unnamed'} (Latitude: {point.latitude}, Longitude: {point.longitude}, Elevation: {point.elevation})"
                    pdf.multi_cell(0, 10, pt_text)
    else:
        pdf.cell(0, 10, "No tracks found in the GPX file.", ln=True)

    pdf.cell(0, 10, "End of tracks.", ln=True)
    pdf.ln(5)

    pdf.cell(0, 10, "Routes:", ln=True)
    if gpx.routes:
        for route in gpx.routes:
            route_text = f"Name: {route.name}, Number of Points: {len(route.points)}"
            pdf.multi_cell(0, 10, route_text)
            for point in route.points:
                pt_text = f"- {point.name} (Latitude: {point.latitude}, Longitude: {point.longitude}, Elevation: {point.elevation})"
                pdf.multi_cell(0, 10, pt_text)
    else:
        pdf.cell(0, 10, "No routes found in the GPX file.", ln=True)

    pdf.cell(0, 10, "End of routes.", ln=True)
    pdf.ln(5)

    pdf.cell(0, 10, "End of file.", ln=True)

    print("Where do you want to save the PDF file?")
    while True:
        cls()
        print("1. Save to default (Software folder) directory")
        print("2. Specify a different directory")
        print("3. Cancel save operation")

        save_choice = input("Please select an option (1-2-3): ")
        if save_choice == '1':
            pdf_file_path = 'output.pdf'
            pdf.output(pdf_file_path)
            print(f"PDF file saved successfully to {pdf_file_path}.")
            print("You can now close the program or continue editing.")
            input("Press Enter to return to the menu...")
            cls()
            return pdf_file_path
        elif save_choice == '2':
            dir_path = input("Enter the directory path where you want to save the PDF file: ")
            if not dir_path.endswith('/') and not dir_path.endswith('\\'):
                dir_path += '/'
            pdf_file_name = input("Enter the name of the PDF file (without extension): ")
            if not pdf_file_name.endswith('.pdf'):
                pdf_file_name += '.pdf'
            full_pdf_path = os.path.join(dir_path, pdf_file_name)
            try:
                pdf.output(full_pdf_path)
                print(f"PDF file saved successfully to {full_pdf_path}.")
                print("You can now close the program or continue editing.")
                input("Press Enter to return to the menu...")
                cls()
                return full_pdf_path
            except OSError as e:
                print(f"Error saving file: {e.strerror}. Please try again with a valid path.")
                continue
        elif save_choice == '3':
            print("Save operation canceled.")
            cls()
            break
        else:
            print("Invalid selection, please try again.")

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

    print("End of routes.\n")

    print("\nEnd of file.")

    input("Press Enter to return to the menu...")