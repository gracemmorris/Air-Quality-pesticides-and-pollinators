# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 23:14:42 2023

@author: grace
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors
import mpl_toolkits.basemap
from mpl_toolkits.basemap import Basemap

df_path = "just_pantrap_predictions.xlsx"
df = pd.read_excel(df_path)

map = Basemap(width=1100000,height=1200000,projection='lcc',

            resolution='i',lat_1=35.,lat_2=55,lat_0=54.5,lon_0=-5.)



map.drawcoastlines(color='black')

map.drawcountries(color='black')

map.drawmapboundary(fill_color='lightskyblue')

map.fillcontinents(color='white',lake_color='blue')

c2=[[0, "black"],[20,"blue"],[30,"cyan"],[40,"green"], [60, "yellow"],[70, "white"] ]

colours2 = pd.DataFrame(c2, columns = ["Pollinator Count", "Colour"])
bees_colourmap= matplotlib.colors.LinearSegmentedColormap.from_list(colours2["Pollinator Count"], colours2["Colour"])


map.scatter(
      df['y'],
      df['x'],
      latlon=True,
      c=df['predicted_count'], # We're adding that
      cmap="CMRmap",
      s=0.5,
      vmin=0,
      vmax=7000
      )


plt.title('Predictions of Polinator Populations in the UK in 2019 from Pan Trap Surveys')
plt.colorbar(label='Predicted number of pollinators throughout the year');
