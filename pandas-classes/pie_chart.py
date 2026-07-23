import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('students.csv')

#print(df.head())
# Pie chart: Pass vs Fail
result_count = df["Result"].value_counts()

plt.figure(figsize=(6, 6))

plt.pie(
result_count,
labels=result_count.index,
autopct="%.1f%%",
startangle=90
)

plt.title("Pass vs Fail Percentage")
plt.show()
