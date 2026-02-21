import pandas as pd
df = pd.read_csv("pandas/data.csv" ,index_col = "Name")

# print(df)
# print(df.to_string())

# Selecetion by column

# print(df["Name"].to_string())
# print(df["Month1"].to_string())

# print(df[["Name" , "Month1" , "Month2"]].to_string()) // Doublee braces we use bacuase w using  multiple values 

# acces by columnn 

# print(df.loc[0])
# print(df.loc[0:11])

# print(df[df["Name"] == "Vihaan Nair"])


name = input("Enter a name: ")
# df.set_index("Name", inplace=True) # Setting name as a index 
try:
    print(df.loc[name])
except KeyError:
    print(f"{name} not found" )

# find which employee has  more month sales in all month on certain amount4
# sales more then 2000
# sales_2000= print(df[df["Month1"] >2000 ])
# print(sales_2000)

# set_month2 sales  == 0
# sales_Month2 = df[df["Month2"] = 0]
# print(sales_Month2)
