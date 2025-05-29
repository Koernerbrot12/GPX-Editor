import gpxpy

def parser():

    gpx_path = input("Enter the path to the GPX file: ")
    print(gpx_path)
    

    if gpx_path.endswith(".gpx") or gpx_path.endswith(".xml"):
        # Parse the GPX file
        with open(gpx_path, 'r') as gpx_file:
            gpx_parsed = gpxpy.parse(gpx_file)
        print("GPX file parsed successfully.")
        return gpx_parsed,gpx_path
    
    else:
        print("Invalid file format. Please provide a .gpx or .xml file.")
        SystemExit
        