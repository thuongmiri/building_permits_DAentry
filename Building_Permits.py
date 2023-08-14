import pandas as pd
import numpy as np
sf_permits = pd.read_csv('D:\Thuong Vo MKT\Python\RawData\Building_Permits.csv')
np.random.seed(0)
#Explore percentage of missing value
total_cells=np.product(sf_permits.shape)
missingvalues=sf_permits.isnull().sum()
total_missingvalues=(missingvalues.sum()/total_cells)*100
#26.26% data has been missed
#fill missing data with after value or 0 with remaining missing data
sf_permits_with_na_dropped=sf_permits.dropna(axis=1)
subset_sf_permits=sf_permits.loc[:,'Street Number Suffix':'Zipcode']
subset_sf_permits=subset_sf_permits.fillna(method='bfill',axis=0).fillna(0)
print(subset_sf_permits.head())