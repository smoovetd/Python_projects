import folium
import webbrowser
import pandas

def get_color_by_elevation(elevation: float) -> str:
    ''' get_color_by_elevation() - takes elevation as parameter and provides color as string depending on the elevation'''
    result = '';

    if elevation < 2000:
        result = 'green'
    elif elevation < 3000:
        result = 'orange'
    else:
        result = 'red'

    return result

def get_elements_pandas(file_path: str, delimiter:str = ',' ) -> list:
    ''' Open file csv file containing  Volcanoes information using pandas. Create list of dictionary items for every Volcanoe and return it'''
    all_elements = pandas.read_csv(file_path ,delimiter)
    #LOCATION,STATUS,ELEV,TYPE,TIMEFRAME,LAT,LON
    #print(type(all_elements))
    #print(all_elements['NAME'])
    result = []
    id = 0
    for name, location, height, lat, lon in zip(all_elements['NAME'],all_elements['LOCATION'], all_elements['ELEV'], all_elements['LAT'], all_elements['LON']):
        result.append({
            'id': id,
            'name': name,
            'location': location,
            'height': float(height),
            'latitude': float(lat) ,
            'lontitude': float(lon)
        })
        id +=1

    return result

def get_elements(file_path:str ) -> list:
    '''Open file csv file containing  Volcanoes information using "with open()...". Create list of dictionary items for every Volcanoe and return it'''
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

fg = folium.FeatureGroup(name = 'Volcanoes')
all_volcanoes = get_elements_pandas('files/Volcanoes.txt')
html_popuptext = """<h4>Volcanoe Information:<h4>
name: %s<br>location: %s<br>height: %s m
"""
for volcanoe in all_volcanoes:
    lat = volcanoe['latitude']
    lon = volcanoe['lontitude']
    iframe = folium.IFrame(html = html_popuptext % (volcanoe['name'], volcanoe['location'], volcanoe['height']), width=250, height=100)

#    crnt_marker = folium.Marker(location=[lat, lon ],
#                                    radius = 10,
#                                     tooltip = volcanoe['name'],
#                                     popup =  folium.Popup(iframe),
#                                     icon=folium.Icon(color=get_color_by_elevation(volcanoe['height'])
#                                     ))
    crnt_color = get_color_by_elevation(volcanoe['height'])
    crnt_marker = folium.CircleMarker(location=[lat, lon ],
                                        radius = 10,
                                         tooltip = volcanoe['name'],
                                         popup =  folium.Popup(iframe),
                                         color = crnt_color,
                                         fill = True,
                                         fill_color = crnt_color,
                                         opacity = 0.5,
                                         fill_opacity = 0.5
                                         )
    fg.add_child(crnt_marker)

crnt_map.add_child(fg)
crnt_map.save(file_name)
print('New map is saved: %s' % (file_name))

if input('Do you want to open the map as new browser tab? Y for Yes, anything for no: ') == 'Y':
    webbrowser.open(file_name)

print('Goodbye')

get_elements_pandas('files/Volcanoes.txt')
