import pandas as pd



df = pd.read_csv(r'C:\Users\ASUS PC\Desktop\AMDARI INTERNSHIP\optiSecure\dataCleaning\df.csv', parse_dates=['InteractionDate'])
print(df.head())