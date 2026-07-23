import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('students.csv')

#print(df.head())

plt.figure(figsize=(10, 5))
plt.bar(df["StudentName"],df["FinalMarks"], 
        color=['green', 'blue', 'orange', 'red', 'purple'])
plt.xlabel("Student")
plt.ylabel("Marks")
plt.title("Final Marks of Students")
plt.grid(True)
plt.show()