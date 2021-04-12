from objects.subjects import Subjects
from objects.students import Students
from objects.teachers import Teachers
from functions.functions_1 import populate_data, check_subjects, check_students, check_subjects_st, check_notes, avg_notes

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

data = populate_data()

check_pass = None
def check_id(password, name_tch):
    #---------- function to check teacher and password ----------
    global check_pass
    for key, value in data.items():
        if key in['teachers']:
            for val in value:
                if val.id_2 == password:
                    check_pass = True
                    return(print('Welcome Teacher ' + name_tch))
                else:
                    check_pass = False
                    return(print ('You are not authorized'))

def start_program():
    print('---------------- Welcome ----------------')
    global check_pass
    flag = True

    while(flag):
        select = input('Are you a Teacher or a Student? \n 1. Teacher \n 2. Student \n 3. Exit ')
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
                            if check_pass == True:
                                flag_2 = True
                                while(flag_2):
                                    #-------Teachers Menu-----------------------------------
                                    select_opt = input('Select an option: \n 1. Assigned subjects \n 2. Enrolled students \n 3. Return ')
                                    if select_opt == '1':
                                        check_subjects(name_tch)
                                    elif select_opt == '2':
                                        check_students(name_tch)
                                    elif select_opt == '3':
                                        break
        elif select == '2':
            name_st = input('Write your name: ')
            name_st = name_st.title()
            for key, value in data.items():
                if key in['students']:
                    for val in value:
                        if val.name == name_st:
                            flag_2 = True
                            while(flag_2):
                                print('Welcome ' + val.name)
                                #-------Students Menu------------------------------------------
                                select_tch = input('Select an option: \n 1. Assigned subjects \n 2. Notes \n 3. Return ')
                                if select_tch == '1':
                                    print(' - Student -  |  - Teacher - ')
                                    check_subjects_st(name_st)
                                elif select_tch == '2':
                                    flag_3 = True
                                    while(flag_3):
                                        select_nt = input('Select an option: \n 1. Individual notes \n 2. Average score \n 3. Return ')
                                        if select_nt == '1':
                                            check_notes(name_st)
                                        elif select_nt == '2':
                                            avg_notes(name_st)
                                        elif select_nt == '3':
                                            break
                                elif select_tch == '3':
                                    break
        elif select == '3':
            print('Goodbye')
            break

start_program()
