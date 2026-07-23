import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("dataset/student_performance.csv")

#print(df.head())
#print(df.info())
sns.set_theme(style="whitegrid")


# Other useful styles:
# darkgrid
# whitegrid
# dark
# white
# ticks

plt.figure(figsize=(7, 5))

sns.countplot(
    data=df,
    x="Course",
    hue="Result",
    palette="Set2"
)

plt.title("Students Count")
plt.xlabel("Course")
plt.ylabel("Number of Students")
plt.savefig("charts/pass_fail_count_course.png", dpi=300, bbox_inches="tight")
plt.show()
