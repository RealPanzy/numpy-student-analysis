import numpy as np

np.random.seed(42)

number_of_students = 10

maths_scores = np.random.randint(10, 60, number_of_students)
python_scores = np.random.randint(10, 60, number_of_students)
english_scores = np.random.randint(10, 60, number_of_students)

scores = np.column_stack((maths_scores, python_scores, english_scores))

subjects = ["Maths", "Python", "English"]

print("Subjects:", subjects)

print("Scores: \n", scores)

sum_scores=np.sum(scores,axis=0,keepdims=True)
mean_scores=np.mean(scores,axis=0,keepdims=True)
median_scores=np.median(scores,axis=0,keepdims=True)
std_scores=np.std(scores,axis=0,keepdims=True)
print("Sum of marks: [Maths, Python, English]---" ,sum_scores)
print("Mean of marks: [Maths, Python, English]--" ,mean_scores)
print("Median : [Maths, Python, English]--------" ,median_scores)
print("Standard deviation: [Maths, Python, English]--" ,std_scores)

top_students= np.where( (scores[:,0]>50) | (scores[:,1]>50) |(scores[:,2]>50))
print("Students who atleast topped a subject (index)- ",top_students[0])

failed_students = np.where( (scores[:,0]<20) | (scores[:,1]<20) | (scores[:,2]<20))
print("Students who atleast failed a subject (index)- ",failed_students[0])

header="Maths, Python, English"
stacked=np.vstack((scores,sum_scores,mean_scores,median_scores,std_scores))

np.savetxt('studentdata.csv',stacked,delimiter=',',header=header,fmt="%.2f")

print("Saved data successfully as 'studentdata.csv' and the sum, mean, median and std is saved inside the csv file.")