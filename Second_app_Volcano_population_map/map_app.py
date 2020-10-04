import folium
import webbrowser
import pandas

def get_elements(file_path:str ) -> list:
    content = pandas.read_csv(file_path)
    #print(content)
    #print(type(content))\
    content.set_index('NAME', inplace = True)
    for row in content.items():
        print(row)
        print(type(row))
        #print('Number: %s - %s (lat:%s ; lon: %s) ' % (row[1], row[2], row[6], row[7]))
    #print(type(row))

    return []

startup_coordinates = [42.67,23.37]
def_zoom = 14
file_name = 'files/map1.html'

crnt_map = folium.Map(location=startup_coordinates, zoom_start = def_zoom, tiles='Stamen Terrain')


home_point = folium.CircleMarker(location=[44.6839, 21.33069],
                                 popup = 'Test',
                                 tooltip = 'Test position',
                                 radius = 2
                                 )
crnt_map.add_child(home_point)
crnt_map.save(file_name)
print('new map is saved')

if input('Do you want to open the map? Y for Yes, anything for no: ') == 'Y':
    webbrowser.open(file_name)

print('Goodbye')

get_elements('files/Volcanoes.txt')
