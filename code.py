import folium
import pandas 
#importing data from the file named image through pandas library
data = pandas.read_csv("points.txt")
lat = list(data["LAT"])              
lon = list(data["LON"])  #loaded the lat column and lon column from the data i.e points file
ele = list(data["ELEV"]) 

def color_maker(x):
    if x < 1000:
        return "black"
    elif 1000 <= x < 3000:
        return"red"
    else:
        return "purple"
        
        
map = folium.Map(location = (38.58,-99.09) , tiles = 'Stamen Terrain',zoom_start = 10)

fgv = folium.FeatureGroup(name = "VOLCANOES")   #layer1

#this for loop can do multiple iterations at one time
for lt,ln,el in zip(lat,lon,ele ):
    fgv.add_child(folium.Marker(location = (lt , ln) , popup = str(el) + "m", 
    icon = folium.Icon(color_maker(el))))

fgp = folium.FeatureGroup(name = "POPULATION")   #layer2

fgp.add_child(folium.GeoJson(data = open("polygons.txt" , 'r' , encoding = 'utf-8-sig').read(), 
style_function= lambda x: {"fillColor" : "yellow" if x['properties']['POP2005'] < 10000000 else 'orange'
                           if 10000000 < x['properties']['POP2005'] < 20000000 else 'red'}))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())


map.save("Map1.html")


