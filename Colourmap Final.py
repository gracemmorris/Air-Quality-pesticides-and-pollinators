# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 23:14:42 2023

@author: grace
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors
from mpl_toolkits.basemap import Basemap

df = pd.read_excel('just_pantrap_predictions.xlsx')


#draw basemap of the UK
map = Basemap(width=1100000,height=1200000,projection='lcc',

            resolution='i',lat_1=35.,lat_2=55,lat_0=54.5,lon_0=-5.)

 

map.drawcoastlines(color='black')

map.drawcountries(color='black')

map.drawmapboundary(fill_color='navy')

map.fillcontinents(color='white',lake_color='blue')
 

#create colourmap, edit colours and values as desired
c2=[[0, "black"],[10, "blue"],[20, "purple"], [30, "red"],\
    [40, "orange"],[50, "yellow"], [60, "green"],[70, "white"]]

colours2 = pd.DataFrame(c2, columns = ["Pollinator Count", "Colour"])
bees_colourmap= matplotlib.colors.LinearSegmentedColormap.from_list(colours2["Pollinator Count"], colours2["Colour"])
    
#create coloured plot of long, lat and predicted count values
map.scatter(
      df['y'],
      df['x'],
      latlon=True,
      c=df['predicted_count'], # We're adding that
      cmap=bees_colourmap,
      vmin=0,
      vmax=7000
      )


plt.title('Predictions of Polinator Populations in the UK in 2019')
plt.colorbar(label='Predicted number of pollinators throughout the year resulting from pan trap surveys');

