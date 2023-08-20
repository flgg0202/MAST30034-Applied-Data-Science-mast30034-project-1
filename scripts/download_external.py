import requests

# set url
url = "https://data.cityofnewyork.us/api/views/2fra-mtpn/rows.csv?accessType=DOWNLOAD"
file_path = "../data/raw/NYPD_crime_data.csv"

# downloading
response = requests.get(url)

# debug
if response.status_code == 200:
    # save the data
    with open(file_path, 'wb') as file:
        file.write(response.content)
else:
    print("Error:", response.status_code)
