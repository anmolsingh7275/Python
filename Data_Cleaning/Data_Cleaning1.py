import pandas as pd

df = pd.read_csv("Data_Cleaning/uber_data.csv")
# df = df.drop(columns = ["Month2","EmployeeID","Name"])
# Handle missing value like NAN which value have NAN will be removed 

# df_clean = df.dropna() # Deltet row  which have  atleast one NAN value  delete complete row 

# 3️⃣ Drop Based on Specific Columns
# df =df.dropna(subset=["Driver Ratings"])

# This will drop rows where Math column has NaN.
# print(df.isnull().sum()) # IT will tell us how many rows have NAN value 

# Fill NAN value with  1
# df = df.fillna("1")
# print(df.isnull().sum())
# df = df.fillna({"Customer Ratings" : "0"})
# print(df)
# print(df)
# print(df)

# df["Customer_Ridde"] = df["Customer_Ridde"].replace({"grass" : "GRASS", 
#                                                      "Lost" :"lost"}) # You can replace  key by  this pf any colummn 
 # Automatically  dp the evrything in lower case 
# df["Booking ID"] = df["Booking ID"].str.lower()
# print(df["Booking ID"])
# Change DataType
# df["Driver Ratings"] = df["Driver Ratings"].astype(bool)
# print("Driver Ratings")
 
 # Remove Duplicate
df = df.drop_duplicates()
print(df)