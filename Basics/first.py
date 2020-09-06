import datetime

crnt_date = datetime.datetime.now()

print(crnt_date)

#----------------------- Section 3

student_grades = [1, 2,3,4,5,6]
grades = list(range(1,6))

print(student_grades)
print(grades)


avr = sum(student_grades)/student_grades.__len__()
print(avr)

#----------------------- Section 5
print(isinstance(3.65,float))
