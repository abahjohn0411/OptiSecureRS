from connect import getdb
from sqlalchemy import text
import csv
import os

def select_df():
    db = getdb()

    query = text("""
        SELECT 
            c.CustomerID, c.Age, c.Gender, c.Income, c.Location, c.MaritalStatus,
            p.PolicyID, p.PolicyType, p.Premium, p.CoverageDetails, p.IssuanceDate, p.ExpiryDate,
            cl.ClaimAmount, cl.ClaimType, cl.ClaimDate,
            bi.InteractionType, bi.InteractionDate, bi.ResponseTime,
            r.RenewalStatus, r.RenewalDate, r.RenewalPremium
        FROM customer c
        LEFT JOIN policy p ON c.CustomerID = p.AssociatedCustomerID
        LEFT JOIN claims cl ON c.CustomerID = cl.CustomerID
        LEFT JOIN behavioral_interaction bi ON c.CustomerID = bi.CustomerID
        LEFT JOIN renewal r ON c.CustomerID = r.CustomerID AND p.PolicyID = r.PolicyID
    """)

    result = db.execute(query)
    df = result.fetchall()
    headers = result.keys()

    save_path = r"C:\Users\ASUS PC\Desktop\AMDARI INTERNSHIP\optiSecure_RS\dataBase"
    

    os.makedirs(save_path, exist_ok=True)

    file_path = os.path.join(save_path, "df.csv")

    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(df)

    print(f"Data written to: {file_path}")
    return df

if __name__ == "__main__":
    select_df()
