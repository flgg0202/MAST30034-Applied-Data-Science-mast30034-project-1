import requests

#set url
url = "https://data.cityofnewyork.us/api/geospatial/2fra-mtpn?method=export&format=GeoJSON"
file_path = "../data/raw/NYPD_boundaries_data.geojson"

# downloading
response = requests.get(url)

# debug
if response.status_code == 200:
    # save the data
    with open(file_path, 'wb') as file:
        file.write(response.content)
else:
    print("Error:", response.status_code)
