from sklearn.cluster import KMeans

df = pd.read_csv("res_dpre.csv")

# Selecting features for clustering
features = df[['Age', 'Fare', 'Pclass']]
features.dropna(inplace=True)

# Applying K-Means with 3 clusters
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(features)

# Saving cluster counts
cluster_counts = df['Cluster'].value_counts()
with open("k.txt", "w") as f:
    f.write(str(cluster_counts))

print("Modeling completed. All processes done.")
