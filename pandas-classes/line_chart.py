import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('students.csv')

#print(df.head())

plt.figure(figsize=(10, 5))
plt.plot(df["StudentName"],df["FinalMarks"], marker='o', color='b')
plt.xlabel("Student")
plt.ylabel("Marks")
plt.title("Final Marks of Students")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()