import pandas as pd

df=pd.read_csv('student_performance.csv')

#r,c = df.shape

#print(f"Number of rows: {r}, Number of columns: {c}")
#print(df[['StudentName','FinalMarks']])

#high_scorers = df[df['FinalMarks']>=75]
#print(high_scorers[['StudentName','FinalMarks']])
#good_students = df[(df['Attendance']>=75) & (df['FinalMarks']>=70)]

#good_students_sorted_df=good_students.sort_values(by=['FinalMarks','Attendance'],ascending=[False,False])
#print(good_students_sorted_df[['StudentName','FinalMarks','Attendance']])

#print(good_students_sorted_df)

#good_students_sorted_df.to_csv('good_students.csv',index=False)

#result_count_students = df['Result'].value_counts()
#print(result_count_students)

#print(good_students_sorted_df.iloc[3:6,[1,8,9]])

#print(good_students_sorted_df.loc[0:5,['StudentName','FinalMarks','Attendance']])

#selected_course_students = df[df['Course'].isin(['MCA','BTECH'])]
#print(selected_course_students)

students_with_y=df[df['StudentName'].str.startswith('R')]

print(students_with_y)
