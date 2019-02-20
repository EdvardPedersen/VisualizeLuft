import csv

from numpy import interp
from pandas import read_csv
import folium
import branca.colormap as cm

data = read_csv('data.csv', header=0, parse_dates=[0], squeeze=True)

print(data)

m = folium.Map(location = [data.iat[1,1], data.iat[1,2]])

print(cm.linear)

for cmap in cm.linear._colormaps:
    print(cmap)

for _, row in data.iterrows():
    lat = row[1]
    lon = row[2]
    pm25 = row[4]
    interpolated_pm25 = interp(pm25, [1,15], [0,1])
    c = cm.linear.GnBu_04(interpolated_pm25)
    text = "PM2.5: " + str(pm25)
    folium.Circle(location=[lat, lon], radius = 30, popup = text, stroke = False, fill = True, fill_color = c).add_to(m)

m.save('data.html')
