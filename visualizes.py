import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the dataset
df = pd.read_csv("houseRental.csv")
sns.histplot(df['Rent'], kde=True)
plt.show()
