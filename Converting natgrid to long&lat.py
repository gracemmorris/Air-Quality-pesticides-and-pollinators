import pandas as pd
import OSGridConverter


df = pd.read_excel('Just_Pan_Trap.xlsx')

# convert OS GridCode to lat and long co-ordinates
def osgb36_to_wgs84(OS_Grid_Code):
    cvt_wgs84 = OSGridConverter.grid2latlong(OS_Grid_Code)
    latitude, longitude = cvt_wgs84.latitude, cvt_wgs84.longitude
    return latitude, longitude


df[['x', 'y']] = df.apply(lambda row: pd.Series(osgb36_to_wgs84(row['OS_Grid_Code'])), axis=1)


df.to_excel('LatLongPanTrap.xlsx', index=False)







