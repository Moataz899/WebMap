import folium

fg = folium.FeatureGroup("map")

fg.add_child(folium.GeoJson(data=(open("egypt_states.json", "r", encoding="utf-8-sig").read())))


map = folium.Map(location=[26.8206, 30.8025], zoom_start=6)

map.add_child(fg)

universities = [
    {"name": "Cairo University", "lat": 30.0277, "lon": 31.2336, "image": "https://www.gettyimages.com/photos/university-egypt"},
    {"name": "The American University in Cairo", "lat": 30.0185, "lon": 31.4994, "image": "https://www.gettyimages.com/photos/university-egypt"},
    {"name": "Alexandria University", "lat": 31.2001, "lon": 29.9187, "image": "https://www.gettyimages.com/photos/university-egypt"},
    {"name": "Ain Shams University", "lat": 30.0771, "lon": 31.2859, "image": "https://www.gettyimages.com/photos/university-egypt"},
    {"name": "Mansoura University", "lat": 31.0409, "lon": 31.3785, "image": "https://www.gettyimages.com/photos/university-egypt"},
    {"name": "Al-Azhar University", "lat": 30.0459, "lon": 31.2625, "image": "https://www.gettyimages.com/photos/university-egypt"},
    {"name": "Assiut University", "lat": 27.1801, "lon": 31.1837, "image": "https://www.gettyimages.com/photos/university-egypt"},
    {"name": "Helwan University", "lat": 29.8414, "lon": 31.3342, "image": "https://www.gettyimages.com/photos/university-egypt"},
    {"name": "Zagazig University", "lat": 30.5877, "lon": 31.5020, "image": "https://www.gettyimages.com/photos/university-egypt"},
    {"name": "Future University in Egypt", "lat": 30.0300, "lon": 31.4900, "image": "https://www.gettyimages.com/photos/university-egypt"}
]

for uni in universities:
    folium.Marker(
        location=[uni["lat"], uni["lon"]],
        popup=f'<strong>{uni["name"]}</strong><br><img src="{uni["image"]}" width="100">',
        icon=folium.Icon(color='blue')
    ).add_to(map)

map.save("sample.html")
