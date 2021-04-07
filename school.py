
from objects.subjects import Subjects
from objects.students import Students
from objects.teachers import Teachers

import datetime, random, calendar

# --------------- Function to know the day of the week -------------
#month_day = int(input("Enter the number of the day to #consult the calendar: "))
#month_day_1 = 0
#def dateMonth(month_day):
    #global month_day_1
    #print(calendar.weekday(2021, 4, month_day))
    #month_day_1 = calendar.weekday(2021, 4, month_day)

#dateMonth(month_day)

#days_week = {
    #'Monday' : 0,
    #'Tuesday' : 1,
    #'Wednesday' : 2,
    #'Thursday' : 3,
    #'Friday' : 4,
    #'Saturday' : 5,
    #'Sunday' : 6

#}

#for day, number in days_week.items():
    #if number == month_day_1:
        #print(day)


def populate_data():
    # all the data with which we will work is entered
    # ------------------------ Define Teachers ------------------
        # List of Teachers
    teachers = []

    teacher_1 = Teachers(
        id = 1,
        id_2 = '0001',
        name = 'Carlos Ramirez',
        subjects = [1, 2, 8]
    )

    teacher_2 = Teachers(
        id = 2,
        id_2 = '0001',
        name = 'Paola Campos',
        subjects = [3, 4]
    )

    teacher_3 = Teachers(
        id = 3,
        id_2 = '0001',
        name = 'Andres Garcia',
        subjects = [1, 5, 8]
    )

    teacher_4 = Teachers(
        id = 4,
        id_2 = '0001',
        name = 'Stefania Ortiz',
        subjects = [7, 2, 6]
    )

    teachers.append(teacher_1)
    teachers.append(teacher_2)
    teachers.append(teacher_3)
    teachers.append(teacher_4)
    # ------------------------ Define Students ------------------
        # List of Teachers
    students = []

    student_1 = Students(
        id = 1,
        name = 'Jhonatan Ruiz',
        subjects = {
            1 : 1,
            2 : 4,
            3 : 2
        },
        notes = {
            1 : 'Not rated yet',
            8 : 'Not rated yet',
            6 : 2.5
        }

    )

    student_2 = Students(
        id = 2,
        name = 'Bryan Portela',
        subjects = {
            4 : 2,
            5 : 3
        },
        notes = {
            1 : 'Not rated yet',
            8 : 'Not rated yet',
            6 : 2.5
        }

    )

    student_3 = Students(
        id = 3,
        name = 'Irina Davila',
        subjects = {
            1 : 3,
            2 : 1,
            7 : 4
        },
        notes = {
            1 : 'Not rated yet',
            8 : 'Not rated yet',
            6 : 2.5
        }

    )

    student_4 = Students(
        id = 4,
        name = 'Jose Barrio',
        subjects = {
            6 : 4,
            8 : 3,
            3 : 2
        },
        notes = {
            1 : 3.6,
            8 : 'Not rated yet',
            6 : 2.5
        }

    )

    student_5 = Students(
        id = 5,
        name = 'Joaquin Valencia',
        subjects = {
            1 : 3,
            8 : 1,
            6 : 4
        },
        notes = {
            1 : 'Not rated yet',
            8 : 'Not rated yet',
            6 : 2.5
        }

    )

    student_6 = Students(
        id = 6,
        name = 'Alejandro Bernal',
        subjects = {
            6 : 4,
            7 : 4
        },
        notes = {
            6 : 4.8,
            7 : 3.2
        }
    )

    student_7 = Students(
        id = 7,
        name = 'Andres Saavedra',
        subjects = {
            6 : 4,
            4 : 2
        },
        notes = {
            6 : 4.0,
            4 : 3.5
        }

    )

    students.append(student_1)
    students.append(student_2)
    students.append(student_3)
    students.append(student_4)
    students.append(student_5)
    students.append(student_6)
    students.append(student_7)


    # ------------------------ Define Subjects ------------------

    subjects = []

    subject_1 = Subjects(
        id = 1,
        name = 'Math',

    )

    subject_2 = Subjects(
        id = 2,
        name = 'Physics',

    )

    subject_3 = Subjects(
        id = 3,
        name = 'Astronomy',

    )

    subject_4 = Subjects(
        id = 4,
        name = 'Biology',

    )

    subject_5 = Subjects(
        id = 5,
        name = 'English',

    )

    subject_6 = Subjects(
        id = 6,
        name = 'Arts',

    )

    subject_7 = Subjects(
        id = 7,
        name = 'Geography',

    )

    subject_8 = Subjects(
        id = 8,
        name = 'Chemistry',

    )


    subjects.append(subject_1)
    subjects.append(subject_2)
    subjects.append(subject_3)
    subjects.append(subject_4)
    subjects.append(subject_5)
    subjects.append(subject_6)
    subjects.append(subject_7)
    subjects.append(subject_8)

    # ------------------------ Define Notes ------------------

    return {
        'teachers': teachers,
        'students': students,
        'subjects': subjects
    }

data = populate_data()

check_pass = None
def check_id(password, name_tch):
    global check_pass
    for key, value in data.items():
        if key in['teachers']:
            for val in value:
                if val.id_2 == password:
                    check_pass = True
                    print('Welcome Teacher ' + name_tch)
                    return True
                    continue
                else:
                    check_pass = False
                    print('You are not authorized')
                    return False
                    break

def check_subjects(name_tch):
    #---------- function to check subjects assigned to teachers ----------
    for key, value in data.items():
        if key in['subjects']:
            for val in value:
                for key_2, value_2 in data.items():
                    if key_2 in['teachers']:
                        for val_2 in value_2:
                            if val_2.name == name_tch:
                                if val.id in val_2.subjects:
                                    print(val.name)

def check_students(name_tch):
    for key, value in data.items():
        if key in['students']:
            for val in value:
                for key_2, value_2 in val.subjects.items():
                    for key_3, value_3 in data.items():
                        if key_3 in['teachers']:
                            for val_3 in value_3:
                             if val_3.name == name_tch:
                                 if value_2 == val_3.id:
                                     print(val.name)
#for key, value in data.items():
    #print('List of ', key)
    #if key in['teachers', 'students', 'subjects']:
        #for val in value:
        #    print(val.name)

def init_program():
    print('---------------- Welcome ----------------')
    global check_pass
    flag = True

    while(flag):
        select = input('''
            Are you a Teacher or a Student?
            1. Teacher
            2. Student
        ''')
        if select == '1':
            name_tch = input('Write your name: ')
            name_tch = name_tch.title()
            for key, value in data.items():
                if key in['teachers']:
                    for val in value:
                        if val.name == name_tch:
                            print(val.name)
                            password = input('Enter your password ')
                            check_id(password, name_tch)
                            print(check_pass)
                            if check_pass == True:
                                #-------Teacher's Menu-------
                                select_tch = input('''
                                    Select an option:
                                    1. Assigned subjects
                                    2. Enrolled students

                                ''')
                                if select_tch == '1':
                                    check_subjects(name_tch)
                                if select_tch == '2':
                                    check_students(name_tch)
        #elif select == 1:
            #print()

init_program()
