import pandas as pd

df = pd.read_excel("data_cleaning/customer_call_list.xlsx")
df
#drop duplicates 
df = df.drop_duplicates()


#remove unnecessary columns 
df = df.drop(columns = "Not_Useful_Column")


#fix the last name  
#df["Last_Name"] = df["Last_Name"].str.lstrip("/")
#df["Last_Name"] = df["Last_Name"].str.lstrip("...")
#df["Last_Name"] = df["Last_Name"].str.rstrip("_")

df["Last_Name"] = df["Last_Name"].str.strip("/._")

 #standaddise the phone number column the

#raphlace anything but the specified characters 
df["Phone_Number"] = df["Phone_Number"].str.replace("[^a-zA-Z0-9]", "", regex= True)
#format the column (ca use for loop)
#df["Phone_Number"] = df["Phone_Number"].apply(lambda x: x[0:3] + "-" x[3:6] + "-" x[6:10])

df["Phone_Number"] = df["Phone_Number"].apply(lambda x:str(x))

df["Phone_Number"] = df["Phone_Number"].apply(lambda x: x[0:3] + "-" + x[3:6] + "-" + x[6:10])
df["Phone_Number"] = df["Phone_Number"].str.replace("nan--", "")
df["Phone_Number"] = df["Phone_Number"].str.replace("Na--", "")

#split the adress column into 3
df[["Street_Address", "City", "Zip_Code"]] = df["Address"].str.split(",", n=2, expand=True)

df["Paying Customer"] = df["Paying Customer"].str.replace("Yes", "Y")
df["Paying Customer"] = df["Paying Customer"].str.replace("No", "N")
#df["Paying Customer"] = df["Paying Customer"].str.replace("N/a", "")

df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace("Yes", "Y")
df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace("No", "N")

df = df.replace("N/a", " ")
#df = df.replace("NaN", " ")
df = df.fillna("")


#get a list of numbers to contact 
for x in df.index:
    if df.loc[x, "Do_Not_Contact"] == "Y":
        df.drop(x, inplace=True)


for x in df.index:
    if df.loc[x, "Phone_Number"] == "":
        df.drop(x, inplace=True)

df = df.reset_index(drop=True)
print(df)