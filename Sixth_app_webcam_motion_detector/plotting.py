from motion_detector import df
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

df['Start_String'] = df['Start_Time'].dt.strftime('%Y-%m-%d %H-%m-%s')
df['End_String'] = df['End_Time'].dt.strftime('%Y-%m-%d %H-%m-%s')

cds = ColumnDataSource(df)

fig = figure(x_axis_type = 'datetime', height = 250, width = 500, title = 'Motion graph')
fig.yaxis.minor_tick_line_color = None

hover = HoverTool(tooltips=[('Start', '@Start_String'),('End', '@End_String')])
fig.add_tools(hover)

quad_gliff = fig.quad(left= 'Start_Time', right = 'End_Time', bottom = 0, top = 1, color = 'green', source = cds)



output_file('graph.html')
show(fig)
