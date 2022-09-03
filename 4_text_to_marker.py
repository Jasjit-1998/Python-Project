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
elev = list(data["ELEV"])    # Loading the elevation data to the python List

map = folium.Map(location = [38.58,-99.09], zoom_start=6, tiles="Stamen Terrain")

# Adding the Children to the Map
# Creating the feature group & in the feature group we can add the marker and the polygon
fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, elev):  # Tese are the list elements mention in the for loop
# add the things in the tupil otherwise it will not work
    fg.add_child(folium.Marker(location = [lt, ln], popup = str(el) +" m", icon = folium.Icon(color='green')))


map.add_child(fg)
map.save("Volcanoes.html")
