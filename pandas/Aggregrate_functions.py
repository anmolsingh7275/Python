import pandas as pd 

df = pd.read_csv("pandas/data.csv" )

# print(df["Month1"].mean())# for single column
# print(df[["Month1", "Month2" , "Month3"]].mean()) # for multiple column 

# Row wise mean 
# row_mean = df[["Month1", "Month2", "Month3"]].mean(axis=1)
# print(row_mean)   

# # with name  and thier rescpective row mean

# # First make sure column names have no extra spaces
# df.columns = df.columns.str.strip()

# # Select only month columns
# month_columns = [col for col in df.columns if "Month" in col]

# # Calculate row-wise mean
# df["Mean"] = df[month_columns].mean(axis=1)

# # Show Name and Mean
# print(df[["Name", "Mean"]])



#WHole dataframe 
# SUM 

# print(df.sum(numeric_only= True))
# print(df.min(numeric_only = True))
# print(df.max(numeric_only = True))
# print(df.count())

#Single Column

 
print(df["Month4"].min())