# Save the program before compiling it
import folium
# Adding the Tiles means you are adding the POLITICAL MAP (Sattes bounf=draies to the map)
#map = folium.Map(location = [38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

# Physical Map
map = folium.Map(location = [38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

# Adding the Children to the Map
# Creating the feature group & in the feature group we can add the marker and the polygon
fg = folium.FeatureGroup(name="My Map")
map.add_child(fg)
# Adding markers (Adding the checkpoint on the map)
map.add_child(folium.Marker(location = [38.2, -99.1], popup = "Hi I am a Marker", icon = folium.Icon(color='green')))


map.save("Map1.html")
