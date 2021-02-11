from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/stock_info/')
def stock_info() -> str:
    return render_template('stock_info.html')

@app.route('/stock_info/', methods = ['POST'])
def stock_ext_info() -> str:
    import pandas
    from pandas_datareader import data
    import datetime
    from bokeh.plotting import figure, output_file, show
    from bokeh.embed import components
    from bokeh.resources import CDN

    def is_increased_value(open_val, closed_val) -> str:
        if closed_val > open_val:
            res = 'Increased'
        elif open_val > closed_val:
            res = 'Decreased'
        else:
            res = 'Equal'
        return res

    source = 'yahoo'
    use_def = False
    hours_12_ms = 12 * 60 * 60 * 1000

    if use_def:
        company_symbol = 'GOOG'
        start_time_str = '2016-03-01'
        end_time_str = '2016-03-10'
    else:
        #company_symbol = input('Enter company: ')
        #start_time_str = input('Enter start time in format: YYYY-M-D: ')
        #end_time_str = input('Enter end time in format: YYYY-M-D: ')
        company_symbol = request.form['Company']
        start_time_str = request.form['Start Date']
        end_time_str = request.form['End Date']

    start_time = datetime.datetime(int(start_time_str.split('-')[0]),int(start_time_str.split('-')[1]),int(start_time_str.split('-')[2]))
    end_time = datetime.datetime(int(end_time_str.split('-')[0]),int(end_time_str.split('-')[1]),int(end_time_str.split('-')[2]))

    print(start_time)
    print(end_time)

    crnt_data = data.DataReader(name = company_symbol, data_source = source, start = start_time, end = end_time)

    crnt_fig = figure(x_axis_type = 'datetime', width = 500, height = 300, title = f'Stock Candlestick Chart - {company_symbol}', sizing_mode = 'scale_width')

    crnt_data['Status'] = [is_increased_value(open_val, closed_val) for open_val, closed_val in zip(crnt_data.Open, crnt_data.Close)]
    #print(crnt_data)
    crnt_data['Middle'] = (crnt_data.Open + crnt_data.Close)/2
    crnt_data['Height'] = abs(crnt_data.Open - crnt_data.Close)

    neg_dates = crnt_data.index[crnt_data.Open > crnt_data.Close]
    pos_dates = crnt_data.index[crnt_data.Open <= crnt_data.Close]

    #print(pos_dates)
    crnt_fig.segment(crnt_data.index, crnt_data.High, crnt_data.index, crnt_data.Low, color = 'black')
    rec_pos = crnt_fig.rect(x = pos_dates, y = crnt_data.Middle[crnt_data.Status == 'Increased'], width = hours_12_ms, height = crnt_data.Height[crnt_data.Status == 'Increased'], color = '#00FF7F', line_color = 'black' )

    rec_neg = crnt_fig.rect(x = neg_dates, y = crnt_data.Middle[crnt_data.Status == 'Decreased'], width = hours_12_ms, height = crnt_data.Height[crnt_data.Status == 'Decreased'], color = '#FF6347', line_color = 'black' )

    js_script, div_script = components(crnt_fig)
    cdn_js = CDN.js_files
    cdn_css = CDN.css_files
    print(cdn_css)

    return render_template('stock_info.html', js_script = js_script, div_script = div_script, cdn_js = cdn_js[0])

@app.route('/')
def home() -> str:
    #return 'Home Page'
    return render_template('home.html')


@app.route('/about/')
def about() -> str:
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
