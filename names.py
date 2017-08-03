students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

# Michael Jordan
# John Rosales
# Mark Guillen
# KB Tonel

def names(arr):
    for student in range(0, len(arr)):
        print arr[student]["first_name"], arr[student]["last_name"]

names(students)

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

# Students
# 1 - MICHAEL JORDAN - 13
# 2 - JOHN ROSALES - 11
# 3 - MARK GUILLEN - 11
# 4 - KB TONEL - 7
# Instructors
# 1 - MICHAEL CHOI - 11
# 2 - MARTIN PURYEAR - 13

def list(arr):
    students = users["Students"]
    instructors = users["Instructors"]
    print "Students"
    for student in range(0, len(students)):
        print str(student+1), "-", students[student]["first_name"], students[student]["last_name"], "-", str(len(students[student]["first_name"]) + len(students[student]["last_name"]))
    print "Instructors"
    for instructor in range(0, len(instructors)):
        print str(instructor+1), "-", instructors[instructor]["first_name"], instructors[instructor]["last_name"], "-", str(len(instructors[instructor]["first_name"]) + len(instructors[instructor]["last_name"]))
list(users)