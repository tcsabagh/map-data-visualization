import pandas as pd
import folium
from folium.plugins import MiniMap

file = "../data/ABC123.xlsx"

# Előszűrések
df = pd.read_excel(file, usecols=[0, 1, 2, 3, 4, 5])
df.columns = ['time', 'rendszam', 'name', 'weight', 'lon', 'lat']
df['weight'] = df['weight'].fillna(0)
df['coordinates'] = df['lat'].astype(str) + ',' + df['lon'].astype(str) + ',' + '0'

# Térkép középpont
map_center = [47.1625, 19.5033]

# Interaktív térkép létrehozása
m = folium.Map(location = map_center, zoom_start=8)
MiniMap().add_to(m) # MiniMap
folium.plugins.Geocoder().add_to(m) # Kereső

# Markerek generálása
for index, row in df.iterrows():
    data = f"<div style=\"width:250px;\"><b>Hely:</b> {row['name']}<br><b>Időpont:</b> {row['time']}<br><b>Súly: </b>{row['weight']} kg</div>"
    folium.Marker(
        location = [row['lon'], row['lat']],
        tooltip = "Több infóért kattints!",
        icon = folium.Icon(color="red"),
        popup = data
    ).add_to(m)

# Térkép mentése HTML-be
m.save("../output/ABC123.html")