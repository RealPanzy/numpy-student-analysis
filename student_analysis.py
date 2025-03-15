import numpy as np
import pandas as pd

np.random.seed(42)

number_of_students = 10

maths_scores = np.random.randint(10, 60, number_of_students)
python_scores = np.random.randint(10, 60, number_of_students)
english_scores = np.random.randint(10, 60, number_of_students)

scores = np.column_stack((maths_scores, python_scores, english_scores))
df=pd.DataFrame(scores)
df.columns=["Maths", "Python", "English"]
df["Total Score"]=df[["Maths","Python","English"]].sum(axis=1)
print("Scores: \n", df)

top_students= np.where( (scores[:,0]>50) | (scores[:,1]>50) |(scores[:,2]>50))
print("Students who atleast topped a subject (index)- ",top_students[0])

failed_students = np.where( (scores[:,0]<20) | (scores[:,1]<20) | (scores[:,2]<20))
print("Students who atleast failed a subject (index)- ",failed_students[0])

header="Maths, Python, English"
aggregated_scores=df[["Maths","Python","English"]].agg(["sum","mean","max","min","median"])
print(aggregated_scores)
df.to_csv('studentdata.csv',index=True)

with open("studentdata.csv", "a") as f:
    f.write("\nAggregated Scores\n") 
    aggregated_scores.to_csv(f)