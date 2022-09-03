# Save the program before compiling it

# In this program using the pandas library we will read the "," seprated text files
# We will extract valuesof the longitude and latitude from  the text file seprately .....
# USing the for loop we will import the volcanoes in the file

import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")

# Getting the list of the Columns
# W eprefer to work on the list because working on the list is faster

lat = list(data["LAT"])
lon = list(data["LON"])


map = folium.Map(location = [38.58,-99.09], zoom_start=6, tiles="Stamen Terrain")

# Adding the Children to the Map
# Creating the feature group & in the feature group we can add the marker and the polygon
fg = folium.FeatureGroup(name="My Map")
for lt, ln in zip(lat, lon):   # Tese are the list elements mention in the for loop
    map.add_child(folium.Marker(location = [lt, ln], popup = "Hi I am a Marker", icon = folium.Icon(color='green')))


map.save("Volcanoes.html")
