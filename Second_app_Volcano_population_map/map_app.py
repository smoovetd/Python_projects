import folium
import webbrowser
import pandas

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

startup_coordinates = [44.67,23.37]
def_zoom = 14
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

for volcanoe in all_volcanoes:
    lat = volcanoe['latitude']
    lon = volcanoe['lontitude']
    crnt_marker = folium.Marker(location=[lat, lon ],
                                     tooltip = volcanoe['name'],
                                     popup = 'name: %s\nlocation: %s\nheight: %s' % (volcanoe['name'], volcanoe['location'], int(volcanoe['height'])),
                                     icon=folium.Icon(color='red')
                                     )
    fg.add_child(crnt_marker)

crnt_map.add_child(fg)
crnt_map.save(file_name)
print('New map is saved: %s' % (file_name))

if input('Do you want to open the map? Y for Yes, anything for no: ') == 'Y':
    webbrowser.open(file_name)

print('Goodbye')

#get_elements('files/Volcanoes.txt')
