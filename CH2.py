#MARIAM ALMALKI
grades = []
num = int(input("Enter number of students: "))
for i in range(num):
    
    name = input("Enter the student's name: ")
    grade = float(input("Enter grade: "))
    grades.append(grade)
    
SORTED = sorted(grades)

print( SORTED[1] )
