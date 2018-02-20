import googlemaps
from datetime import datetime
import json

plotlykey="dLABb2R1baaRKtKYS5oG"
gmaps = googlemaps.Client(key='AIzaSyB84VySbMwOjfLY5SYDdi07vmNeMuq7Zug')

# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()

print (geocode_result[0].keys())


# print (type(directions_result))