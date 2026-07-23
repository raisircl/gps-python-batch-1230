# Histogram: marks distribution
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('students.csv')

plt.figure(figsize=(8, 5))

plt.hist(
    df["FinalMarks"],
    bins=5,
    color="green",
    edgecolor="black"
)

plt.title("Distribution of Final Marks")
plt.xlabel("Marks Range")
plt.ylabel("Number of Students")

plt.savefig("histogram.png")

plt.show()
