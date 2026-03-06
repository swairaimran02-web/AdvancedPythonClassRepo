# import os
# import numpy as np
# data={}
# name=[]
# marks=np.array()
# subject=("oop","os","AI")
# file_name="student.txt"
# if(os.path.exists(file_name)):
#     print("file already exist")
# else:
#     with open("student.txt","w") as file:
#         file.write("Student Records\n")
#     print("File did not exist. File created successfully.")
# dat=input("enter data of 3 students")
# for i in range(0,5):
#     nm=input("enter name : ")
#     name.append(nm)
#     data["namee"]=name.index[0]
#     rolno=int(input("enter roll no : "))
#     data["roll no"]=rolno
#     mark=int(input(f"enter marks of  {subject.index(0)} : "))
#     marks.append(mark)
#     mark=int(input(f"enter marks of {subject.index(0)} : "))
#     marks.append(mark)
#     mark=int(input(f"enter marks of {subject.index(0)} : "))
#     marks.append(mark)
#     avg=((marks[0]+marks[1]+marks[2])/3)*100
#     data["Average"]=avg
#     if avg >= 80:
#         data["grade"]="A"
#     elif avg >= 60:
#         data["grade"]="B"
#     elif avg >= 40:
#         data["grade"]="C"
#     else:
#        data["grade"]="F"
    
#     print(data={"namee":name,"roll no":rolno,"total":totl,"Average":avg,"grade":grd})
    
import os
from array import array

# Tuple for subjects (fixed)
subjects = ("OOP", "OS", "AI")

# File name
file_name = "students.txt"

# Check if file exists
if not os.path.exists(file_name):
    with open(file_name, "w") as file:
        file.write("Student Records\n")

# Lists to store data
names = []
all_students = []

# Loop for 5 students
for i in range(5):
    print(f"\nEnter data for Student {i+1}")

    name = input("Enter name: ")
    roll = input("Enter roll number: ")

    # Array for marks
    marks = array('i')

    for subject in subjects:
        mark = int(input(f"Enter marks for {subject}: "))
        marks.append(mark)

    # Calculations
    total = sum(marks)
    avg = total / 3

    # Grade logic
    if avg >= 80:
        grade = "A"
    elif avg >= 60:
        grade = "B"
    elif avg >= 40:
        grade = "C"
    else:
        grade = "F"

    # Store in dictionary
    student = {
        "name": name,
        "roll": roll,
        "total": total,
        "average": avg,
        "grade": grade
    }

    all_students.append(student)
    names.append(name)

    # Write to file
    with open(file_name, "a") as file:
        file.write(f"Name: {name} | Roll: {roll} | Total: {total} | "
                   f"Avg: {avg:.2f} | Grade: {grade}\n")

# Read file and display only Grade A students
print("\nStudents with Grade A:\n")

with open(file_name, "r") as file:
    lines = file.readlines()
    for line in lines:
        if "Grade: A" in line:
            print(line.strip())

# Find Top Scorer
top_student = max(all_students, key=lambda x: x["total"])

print("\nTop Scorer → "
      f"{top_student['name']} with {top_student['total']} marks")