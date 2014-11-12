import pandas as pd
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt


fig, ax = subplots(figsize=(12,12))
map_global = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180, resolution='l')
data_global = pd.read_csv("/Users/apple/Desktop/class/14fall/big_data_project/test/total.csv", header=None,names=['lat', 'long'])
data_global.count()

map_global.drawcoastlines()
map_global.drawcountries()
map_global.fillcontinents(color='coral')
map_global.drawmapboundary()

# x,y = map_global(data_global.long.values, data_global.lat.values)
map_global.plot(-118.660298, 33.700624, 'bo', markersize=90)


fig, ax = subplots(figsize=(12,12))
map_us = Basemap(llcrnrlon=-119, llcrnrlat=22, urcrnrlon=-64,urcrnrlat=49, projection='lcc', lat_1=33, lat_2=45, lon_0=-95) # us
info = map_us.readshapefile('st99_d00','states',drawbounds=True)

data_us = pd.read_csv("/Users/apple/Desktop/class/14fall/big_data_project/test/us.csv", header=None, names=['lat', 'long'])
data_us.count()

map_us.drawcoastlines()
map_us.drawcountries()
map_us.fillcontinents(color='coral')
map_us.drawmapboundary()

x,y = map_us(data_us.long.values, data_us.lat.values)
map_us.plot(x, y, 'bo', markersize=2)


fig, ax = subplots(figsize=(12,12))

map_nyc = Basemap(llcrnrlat=40.55, urcrnrlat=40.82, llcrnrlon=-74.1, urcrnrlon=-73.82,\
              projection='lcc',lon_0=(-74.1 + -73.82) / 2,lat_0=(40.55 + 40.82)/2, resolution='l')

data_nyc = pd.read_csv("/Users/apple/Desktop/class/14fall/big_data_project/test/nyc.tsv", header=None, names=['lat', 'long'], sep=r'\s+')
data_nyc.count()
info = map_nyc.readshapefile('USA_adm/USA_adm2','states',drawbounds=True)

map_nyc.drawcoastlines()
map_nyc.drawcountries(color='coral')
map_nyc.fillcontinents()
map_nyc.drawmapboundary()

x,y = map_nyc(data_nyc.long.values, data_nyc.lat.values)
map_nyc.plot(x, y, 'bo', markersize=2)