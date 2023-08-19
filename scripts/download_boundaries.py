import requests

# 指定URL和文件路径
url = "https://data.cityofnewyork.us/api/geospatial/2fra-mtpn?method=export&format=GeoJSON"
file_path = "../data/landing/NYPD_boundaries_data.csv"

# 使用requests下载数据
response = requests.get(url)

# 确保请求成功
if response.status_code == 200:
    # 将数据写入文件
    with open(file_path, 'wb') as file:
        file.write(response.content)
else:
    print("Error:", response.status_code)
