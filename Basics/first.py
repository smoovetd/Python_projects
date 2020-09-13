import datetime

def find_winner(**kwargs):
    print(kwargs)
    print(kwargs.get)
    return max(kwargs, key = kwargs.get)

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

print('--------------------------------')



find_winner(Andi = 17, Marry = 19, Sim = 45, Kae = 34)
print('--------------------------------')
st = 'The American black bear (Ursus americanus) is a medium-sized bear native to North America. It is the continent\'s smallest and most widely distributed bear species. American black bears are omnivores, with their diets varying greatly depending on season and location. They typically live in largely forested areas, but do leave forests in search of food. Sometimes they become attracted to human communities because of the immediate availability of food. The American black bear is the world\'s most common bear species.'

print(st[:92])
print(st[0:93])
