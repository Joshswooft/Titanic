import pandas as pd
import numpy as np
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

# read in the data
df = pd.read_csv('data/train.csv', index_col=0)
print(df.head(5))
print(df.info())

# Visualise the data
df.hist()
plt.show()
fig, ax = plt.subplots(figsize=(12,12))
scatter_matrix(df, alpha=1, figsize=(12, 12), ax=ax)

# show scatter of each point against the survived column

# plt.show()

# How to handle missing data?
# How to handle duplicated data?
