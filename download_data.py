import os

# If kaggle.json is in the same folder, set config dir
os.environ['KAGGLE_CONFIG_DIR'] = os.path.abspath('.')

# Download and unzip the dataset
os.system("kaggle datasets download computingvictor/transactions-fraud-datasets --unzip")

print("Download completed!")
