import sys
import pandas as pd

if len(sys.argv) != 2:
    print("Usage: python load.py <dataset-path>")
    sys.exit(1)

dataset_path = sys.argv[1]
df = pd.read_csv(dataset_path)

# Save and pass the path to next script
df.to_csv("processed_data.csv", index=False)
print("Dataset loaded. Proceeding to data preprocessing...")
exec(open("dpre.py").read())
