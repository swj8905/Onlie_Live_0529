import folium

map = folium.Map(location=[37.4984, 127.02660], zoom_start=17)
map.save("./map.html")