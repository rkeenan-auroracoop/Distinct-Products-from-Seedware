import json
import os
import pandas as pd
import pyodbc
import datetime
from datetime import date

readFile = open(r'C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\2020 Harvest Data\2020 Harvest Data.json',)

data = json.load(readFile)

df=pd.DataFrame(data)

print(df)

CompanyAndProductdf = df[['I_Company_Name','I_Variety']]

#print(CompanyAndProductdf)

#print(df.I_Variety.unique())

print(CompanyAndProductdf.nunique()) 

finalReport = CompanyAndProductdf.drop_duplicates()

print(finalReport)

finalReportSorted = finalReport.sort_values(by='I_Company_Name')

finalReportSorted.to_csv(r'C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\2020 Harvest Data\Unique Products Name from Seedware.csv', index=False )