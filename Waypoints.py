import gpxpy
from commands import cls

def print_points(gpx):

     cls()
# This function prints all waypoints in the GPX file.
     for waypoint in gpx.waypoints:
         print(f"Name: {waypoint.name}, Latitude: {waypoint.latitude}, Longitude: {waypoint.longitude}, Elevation: {waypoint.elevation}")


     print("\nEnd of waypoints.")


    