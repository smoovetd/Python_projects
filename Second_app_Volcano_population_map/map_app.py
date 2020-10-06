import folium
import webbrowser
import pandas

def get_color_by_elevation(elevation: float) -> str:
    result = '';

    if elevation < 2000:
        result = 'green'
    elif elevation < 3000:
        result = 'orange'
    else:
        result = 'red'

    return result

def get_elements_pandas(file_path: str) -> list:

    return []

def get_elements(file_path:str ) -> list:
    content = []
    result = []
    isheader = True
    with open(file_path, 'r') as file:
        for line in file:
            if isheader:
                isheader = False
            else:
                content.append(line)

    id = 0
    for item in content:
        result.append({
            'id': id,
            'name': item.split(',')[2],
            'location': item.split(',')[3],
            'height': float(item.split(',')[5]),
            'latitude': float(item.split(',')[8]),
            'lontitude': float(item.split(',')[9].replace('\n',''))
        })
        id +=1


    #print(result)
    return result

startup_coordinates = [48.67,-123.37]
def_zoom = 5
file_name = 'files/map1.html'

crnt_map = folium.Map(location=startup_coordinates, zoom_start = def_zoom, tiles='Stamen Terrain')


#home_point = folium.Marker(location=[44.6839, 21.33069],
#                                 popup = 'Test',
#                                 tooltip = 'Test position',
#                                 icon=folium.Icon(color='red')
#                                 )

fg = folium.FeatureGroup(name = 'Volcanoes')
#fg.add_child(home_point)
all_volcanoes = get_elements('files/Volcanoes.txt')
html_popuptext = """<h4>Volcanoe Information:<h4>
name: %s<br>location: %s<br>height: %s m
"""
for volcanoe in all_volcanoes:
    lat = volcanoe['latitude']
    lon = volcanoe['lontitude']
    iframe = folium.IFrame(html = html_popuptext % (volcanoe['name'], volcanoe['location'], volcanoe['height']), width=250, height=100)

    crnt_marker = folium.Marker(location=[lat, lon ],
                                     tooltip = volcanoe['name'],
                                     popup =  folium.Popup(iframe),
                                     icon=folium.Icon(color=get_color_by_elevation(volcanoe['height'])
                                     ))
    fg.add_child(crnt_marker)

crnt_map.add_child(fg)
crnt_map.save(file_name)
print('New map is saved: %s' % (file_name))

if input('Do you want to open the map? Y for Yes, anything for no: ') == 'Y':
    webbrowser.open(file_name)

print('Goodbye')

#get_elements('files/Volcanoes.txt')
