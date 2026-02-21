import pandas as pd

data = { "Name": [ "Anmol" ,"Kushagra" , " Aryaman" , "Zaid"],
        "Age" : [20, 21 , 22 , 23]
        }

df = pd.DataFrame(data , index =["Employee1" , "Emp2" , 'Emp3' , "Emp4"])
# print(df.loc["Emp2"]) using object location of varibale 

#Print column single column 

print(df["Name"])


# Add new column 

df['JOb'] = ["Engineeer", "IAS", "Doctor","Chaprasi"]

# Add new row

df.loc[len(df)] = ["Aman", 23, "Developer"]
df.loc["Emp5"] = [ "Aman" , 26 , "Developer"]
print(df)