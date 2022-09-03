# Save the program before compiling it

# Adding the multiple Markers
# Two ways of adding the multiple markers
# By repeating the 1. -> map.add_child(folium.Marker(location = [38.2, -99.1], popup = "Hi I am a Marker", icon = folium.Icon(color='green')))
# Second Way -> By using the for loopp


import folium
# Adding the Tiles means you are adding the POLITICAL MAP (Sattes bounf=draies to the map)
#map = folium.Map(location = [38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

# Physical Map
map = folium.Map(location = [38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

# Adding the Children to the Map
# Creating the feature group & in the feature group we can add the marker and the polygon
fg = folium.FeatureGroup(name="My Map")
for coordinates in [[38.2, -99.1], [39.2, -97.1]]:   # Tese are the list elements mention in the for loop
    map.add_child(folium.Marker(location = coordinates, popup = "Hi I am a Marker", icon = folium.Icon(color='green')))



map.save("Map2.html")
