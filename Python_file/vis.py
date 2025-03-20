import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("res_dpre.csv")

plt.figure(figsize=(8, 5))
sns.histplot(df['Age'], bins=20, kde=True)
plt.title("Age Distribution of Titanic Passengers")
plt.xlabel("Age")
plt.ylabel("Count")
plt.savefig("vis.png")
print("Visualization created. Proceeding to model training...")
exec(open("model.py").read())
