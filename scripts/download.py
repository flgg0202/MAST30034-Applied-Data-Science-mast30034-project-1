from urllib.request import Request, urlopen
import os
import sys

base_path = "../data/raw"
years = ["2022", "2023"]

for year in years:
    path = os.path.join(base_path, year)
    os.makedirs(path, exist_ok=True)

URL = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_"

year_2022 = 2022
year_2023 = 2023

Month_2022 = range(7,13)
Month_2023 = range(1,5)

output_relative_dir = f'../data/landing'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.3'
}

def download_with_progress(url, output_dir):
    req = Request(url, headers=headers)
    with urlopen(req) as response:
        length = int(response.headers['content-length'])
        chunk_size = max(4096, length // 100)  # At most 100 chunks, at least 4KiB
        read_so_far = 0
        
        with open(output_dir, 'wb') as out_file:
            while True:
                chunk = response.read(chunk_size)
                if not chunk:
                    break
                
                read_so_far += len(chunk)
                out_file.write(chunk)
                
                percent_done = read_so_far * 100 / length
                sys.stdout.write("\r>> Downloaded %d%%" % percent_done)
                sys.stdout.flush()

    sys.stdout.write("\n")  # Move to the next line after the download is finished

for month in Month_2022:
    print(f'starting {year_2022} {month}')
    month = str(month).zfill(2)
    url = f'{URL}{year_2022}-{month}.parquet'
    output_dir = f'{output_relative_dir}/{year_2022}/{year_2022}-{month}.parquet'
    
    download_with_progress(url, output_dir)
            
    print(f'finished {year_2022} {month}')

# Similarly for 2023...
for month in Month_2022:
    print(f'starting {year_2023} {month}')
    month = str(month).zfill(2)
    url = f'{URL}{year_2023}-{month}.parquet'
    output_dir = f'{output_relative_dir}/{year_2023}/{year_2022}-{month}.parquet'
    
    download_with_progress(url, output_dir)
            
    print(f'finished {year_2023} {month}')