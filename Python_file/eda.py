import pandas as pd

df = pd.read_csv("res_dpre.csv")

# Use .format() instead of f-strings for Python 2 compatibility
insight1 = "Average Age of passengers: {:.2f}".format(df['Age'].mean())
insight2 = "Survival Rate: {:.2f}%".format(df['Survived'].mean() * 100)
insight3 = "Most common embarkation port: {}".format(df['Embarked'].mode()[0])

# Writing insights to separate files
with open("eda-in-1.txt", "w") as f:
    f.write(insight1)

with open("eda-in-2.txt", "w") as f:
    f.write(insight2)

with open("eda-in-3.txt", "w") as f:
    f.write(insight3)

print("EDA completed. Proceeding to visualization...")

# Execute the next script
exec(open("vis.py").read())
