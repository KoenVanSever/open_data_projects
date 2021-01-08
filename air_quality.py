import re
import folium

def process_geolocation(string):
    if re.match("\d+\.\d+,\d+\.\d+", string):
        coordinates = string.strip().split(",")
        ret = tuple(map(float, coordinates))
        return ret
    else:
        print("Geolocation format not correct!")
        return None
    
def plot_locations_on_folium_map(df, m, rad = 100):
    if not df.Unit.nunique() == 1:
        raise ValueError("Non uniform units for pollutant")
    max_polutant = df.Value.max()
    high_thr = max_polutant*2/3
    low_thr = max_polutant/3
    unit = df.Unit.values[0]
    pol = df.Pollutant.values[0]
    base = " {} {} measured".format(unit, pol)
    for _, row in df.iterrows():
        co = process_geolocation(row.Coordinates)
        if co == None:
            raise ValueError("Faulty geolocation format in dataframe")
        val = row.Value
        col = None
        if val < low_thr:
            col = "green"
        elif val >= low_thr and val < high_thr:
            col = "orange"
        else:
            col = "red"
        tip = str(val) + base
        folium.Circle(location = co, radius = rad, color = col, tooltip = tip).add_to(m)