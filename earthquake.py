# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 03:22:33 2017

@author: deng sta maria

The 3-month data is pulled from http://www.phivolcs.dost.gov.ph/html/update_SOEPD/EQLatest.html

Plot the location of the earthquakes and represent via magnitude.

"""
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import pandas as pd
from urllib.request import urlopen

#Q1 2017 data only
jan_url = "http://www.phivolcs.dost.gov.ph/html/update_SOEPD/EQLatest-Monthly/2017_January.htm"
jan_html = urlopen(jan_url).read()
jan_table = pd.read_html(jan_html)
jan_df=jan_table[3].dropna(how='any')

feb_url ="http://www.phivolcs.dost.gov.ph/html/update_SOEPD/EQLatest-Monthly/2017_February.htm"
feb_html = urlopen(feb_url).read() 
feb_table = pd.read_html(feb_html)
feb_df=feb_table[3].dropna(how='any')

mar_url = "http://www.phivolcs.dost.gov.ph/html/update_SOEPD/EQLatest-Monthly/2017_March.html"
mar_html = urlopen(mar_url).read() 
mar_table = pd.read_html(mar_html)
mar_df=mar_table[3].dropna(how='any')

df = pd.concat([jan_df,feb_df,mar_df])

df.rename(columns={0:'Date - Time',1:'Latitude',2:'Longitude',3:'Depth (km)',4:'Magnitude',5:'Location' }, inplace=True)

#save file
df.to_csv('earthquake.csv', sep=',')

#draw map using basemap
fig = plt.figure(figsize=(10,10))
plt.title('Philippine Earthquakes \n Q1 of 2017 ')
map = Basemap(llcrnrlon=115,llcrnrlat=0,urcrnrlon=130,urcrnrlat=25,projection='tmerc', lat_0 = 12.8797, lon_0 = 121.7740)
map.shadedrelief()

#plot quake points
x, y = map(df.Longitude.tolist(),df.Latitude.tolist())
map.scatter(x, y, c=df.Magnitude,marker='o')
map.colorbar().set_label('Magnitude')
plt.show()


