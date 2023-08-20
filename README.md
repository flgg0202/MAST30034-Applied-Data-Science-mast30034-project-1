
# MAST30034 Project 1 README.md
- Name: `GUOXUAN WANG`
- Student ID: `1266123`

**Research Goal:** My research goal is tip rate together with the crime count analysis 

**Timeline:** The timeline for the research area is 2022 - 2023.
To run the pipeline, please visit the `scripts` directory and run the files in order(If the scripts are not available,you can go to www.nyc.gov for tlc data and data.cityofnewyork.us for external data):
1. `download.py`: This downloads the raw data into the `data/raw` directory.
2. `download_external.py`: This downloads the external crime data into the 'data/raw' directory.
3. `download_boundaries.py`: This downloads the external boundary data into the 'data/raw' directory.
4. `TLC Preprocessing.ipynb.`: This filter the invalid data in raw tlc data and store the data to ../data/curated/first_clean
5. `data visualization and second clean.ipynb`: This plot and analyze the distribution of tlc data and store at ../data/curated/final_pd.csv as the preparations of data aggregation
6. `External Preprocessing.ipynb`: This filter the invalid data in external data and seperate the test data.The results are stored in ../data/curated/joined.csv and ../data/curated/test_joined.csv, which also contains the geo data, for further merge
7. `Data aggregation.ipynb`:This aggregate tlc data with external data, the merged data is stored at ../data/curated/merged_df.csv
8. `External Visualization.ipynb`: This produces several distribution plot and geo plot for the aggregated data
9. `Test Data Preprocessing.ipynb`: This clean the test data and stored at ../data/curated/merged_df_test.csv
10. `Modelling.ipynb`: This builds Random Forest Regression model and Gradient Boosting model include the error analysis