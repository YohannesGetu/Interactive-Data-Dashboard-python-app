from pandas_datareader import data
import datetime
from bokeh.plotting import figure, show, output_file 

start = datetime.datetime(2021,7,1)
end = datetime.datetime(2021,7,10)

df = data.DataReader(name="AAPL", data_source="yahoo", start=start, end=end)

p = figure(x_axis_type='datetime', width=1000, height=300)
p.title.text = "Candlestick Chart"

print(df)