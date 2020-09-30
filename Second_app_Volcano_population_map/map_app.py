import folium
import webbrowser

startup_coordinates = [42.67,23.37]
def_zoom = 14
file_name = 'files/map1.html'

crnt_map = folium.Map(location=startup_coordinates, zoom_start = def_zoom)
crnt_map.save(file_name)

print('new map is saved')

if input('Do you want to open the map? Y for Yes, anything for no: ') == 'Y':
    webbrowser.open(file_name)

print('Goodbye')
