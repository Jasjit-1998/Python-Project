# In this program we will see -:
# The popullation of the country by the graduated color
# USsing the color kto see the popullaiton from low to high
# In this program colors of the lpolygon cganges to the yellow

import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")

# Getting the list of the Columns
# W eprefer to work on the list because working on the list is faster

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])    # Loading the elevation data to the python List

def color_producer(elevation):
    if elevation < 1000:
        return 'green'

    elif 1000<=elevation < 3000:
        return 'orange'

    else:
        return 'red'

map = folium.Map(location = [38.58,-99.09], zoom_start=6, tiles="Stamen Terrain")

# Adding the Children to the Map
# Creating the feature group & in the feature group we can add the marker and the polygon
fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, elev):  # Tese are the list elements mention in the for loop
# add the things in the tupil otherwise it will not work
    fg.add_child(folium.CircleMarker(location = [lt, ln], radius = 6, popup = str(el) +" m", fill_color=color_producer(el), color = 'grey', fill = True, fill_opacity=0.7))

 # Object to read the json file
 # Adding style function to show the popullation in the form of the color
# fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding = 'utf-8-sig')))    # Object to read the json file
fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding = 'utf-8-sig'),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']< 10000000
else 'orange' if 10000000 <= x['properties']['POP2005']< 20000000 else 'red'}))


map.add_child(fg)
map.save("7_2CountryPopulation.html")
