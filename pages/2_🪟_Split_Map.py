import folium
import leafmap.foliumap as leafmap

m = leafmap.Map(height=600, center=[39.4948, -108.5492], zoom=12)
url = 'Attibut1Jour-1.tif'
url2 = 'Attibut1Jour0.tif'
m.split_map(url, url2)
m.to_streamlit(height=700)
