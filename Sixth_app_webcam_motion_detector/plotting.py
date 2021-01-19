from motion_detector import df
from bokeh.plotting import figure, show, output_file

fig = figure(x_axis_type = 'datetime', height = 250, width = 500, title = 'Motion graph')
quad_gliff = fig.quad(left= df['Start Time'], right = df['End Time'], bottom = 0, top = 1, color = 'green')

fig.yaxis.minor_tick_line_color = None

output_file('graph.html')
show(fig)
