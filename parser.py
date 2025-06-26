import gpxpy
import os


def parser():

    gpx_path = input("Enter the path to the GPX file: ")
    if gpx_path.startswith('"') and gpx_path.endswith('"'):
        gpx_path = gpx_path[1:-1]

    if gpx_path.endswith(".gpx") or gpx_path.endswith(".xml"):
        # Check if the file exists
        if not os.path.exists(gpx_path):
            print("File does not exist. Please check the path and try again.")
            return
        # Check if the file is empty
        if os.path.getsize(gpx_path) == 0:
            print("File is empty. creating a new GPX object.")
            gpx_parsed = gpxpy.gpx.GPX()
            return gpx_parsed
        # Parse the GPX file
        with open(gpx_path, 'r') as gpx_file:
            gpx_parsed = gpxpy.parse(gpx_file)
        print("GPX file parsed successfully.")
        return gpx_parsed
    
    else:
        print("Invalid file format. Please provide a .gpx or .xml file.")
        parser()

        