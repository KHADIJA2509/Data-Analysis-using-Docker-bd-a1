import pandas as pd

df = pd.read_csv("processed_data.csv")

# Handling missing values (filling age with median)
df["Age"].fillna(df["Age"].median(), inplace=True)

# Encoding categorical variables
df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
df["Embarked"].fillna("S", inplace=True)
df["Embarked"] = df["Embarked"].map({"S": 0, "C": 1, "Q": 2})

# Dropping irrelevant columns
df.drop(columns=["Name", "Ticket", "Cabin"], inplace=True)

# Saving cleaned data
df.to_csv("res_dpre.csv", index=False)
print("Preprocessing complete. Proceeding to exploratory data analysis...")
exec(open("eda.py").read())