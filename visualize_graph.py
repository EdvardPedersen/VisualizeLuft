import csv

from pandas import read_csv
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource

data = read_csv('data.csv', header=0, parse_dates=[0], squeeze=True)
data = data.set_index('timestamp')
data = data.resample('30S').mean()
source = ColumnDataSource(data)


p = figure(x_axis_type="datetime")
p.circle(x='timestamp', y='pmTwoFive', source=source, size=3, color='green')
p.line(x='timestamp', y='pmTwoFive', source=source, line_color='green')

show(p)
