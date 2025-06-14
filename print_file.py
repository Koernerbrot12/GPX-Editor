from fpdf import FPDF
import gpxpy


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

def print_gpx(gpx_to_print):
    # Print the contents of a GPX file to the console.
    print(gpx_to_print)
    print("\nEnd of file.")
    input("Press Enter to return to the menu...")