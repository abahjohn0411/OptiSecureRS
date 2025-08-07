# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Create a file path
file_path = r'C:\Users\ASUS PC\Desktop\AMDARI INTERNSHIP\optiSecure\OptiSecure_RS\dataCleaning\df.csv'

def preprocessing(file_path):
    '''Data Preprocessing Script'''
    
    # Load dataset
    df = pd.read_csv(file_path, 
                     parse_dates=['IssuanceDate', 'ExpiryDate', 'ClaimDate', 'InteractionDate', 'ResponseTime', 'RenewalDate'])

    # Identify numeric and categorical columns
    num_col = df.select_dtypes(include=[np.number]).columns
    cat_col = df.select_dtypes(include=['object']).columns

    # Handle missing values
    df[num_col] = df[num_col].fillna(df[num_col].median())
    for col in cat_col:
        df[col] = df[col].fillna(df[col].mode()[0])
    # Handle missing numerical values
    #from sklearn.impute import SimpleImputer
    #num_col = df.select_dtypes(include = [np.number])
    #imputer = SimpleImputer(strategy='median')
    #df_num = imputer.fit_transform(num_col)
    #df_num = pd.DataFrame(df_num, columns=num_col.columns)

    # Handle missing categorical values
    #from sklearn.impute import SimpleImputer
    #cat_col = df.select_dtypes(include = [object])
    #imputer = SimpleImputer(strategy='most_frequent')
    #df_cat = imputer.fit_transform(cat_col)
    #df_cat = pd.DataFrame(df_cat, columns=cat_col.columns)
    

    # Handle outliers using IQR method
    for col in num_col:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        df[col] = np.where((df[col] < lower_bound) | (df[col] > upper_bound), 0, df[col])

    # Clean and standardize text columns
    for col in cat_col:
        df[col] = df[col].astype(str).str.strip().str.lower()
        df[col] = df[col].astype('category')

    # Scale selected numeric columns
    scaler = StandardScaler()
    df_scale = ['Income', 'Premium']
    df[df_scale] = scaler.fit_transform(df[df_scale])

    # Confirm completion
    print(f"✅ Data preprocessing completed successfully. Data shape: Rows: {df.shape[0]}, Columns: {df.shape[1]}")
    print(df.describe(include=(np.number)))
  
    print(df.dtypes)
    print(df.info)

    return df

if __name__ == "__main__":
    df_cleaned = preprocessing(file_path)





    

