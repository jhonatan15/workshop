class Teachers:
    id = ''
    name = ''
    subjects = []

    def __init__(self, id, name, subjects):
        self.id = id
        self.name = name
        self.subjects = subjects


    def print_names(self):
        print (self.names)

class Students:
    id = ''
    name = ''
    subjects = []

    def __init__(self, id, name, subjects):
        self.id = id
        self.name = name
        self.subjects = subjects

class Subject:
    id = ''
    name = ''
    schedule = ''

    def __init__(self, id, name, schedule):
        self.id = id
        self.name = name
        self.schedule = schedule


class classNotes:
    id = ''
    valor = ''


# ------------------------ Define Teachers ------------------
teacher_1 = Teachers(
    id = 1,
    name = 'Carlos Ramirez',
    subjects = ['Math', 'physics', 'Chemistry']
)

teacher_2 = Teachers(
    id = 2,
    name = 'Paola Campos',
    subjects = ['Astronomy', 'biology']
)

teacher_3 = Teachers(
    id = 3,
    name = 'Andres Garcia',
    subjects = ['Math', 'English', 'Chemistry']
)

teacher_4 = Teachers(
    id = 4,
    name = 'Stefania Ortiz',
    subjects = ['Geography', 'physics', 'Arts']
)


# ------------------------ Define Students ------------------

student_1 = Students(
    id = 1,
    name = 'Jhonatan Ruiz',
    subjects = ['Math', 'Physics', 'Astronomy']

)

student_2 = Students(
    id = 2,
    name = 'Bryan Portela',
    subjects = ['Biology', 'English']

)

student_3 = Students(
    id = 3,
    name = 'Irina Davila',
    subjects = ['Math', 'Physics', 'Geography']

)

student_4 = Students(
    id = 4,
    name = 'Jose Barrio',
    subjects = ['Arts', 'Chemistry', 'Astronomy']

)

student_5 = Students(
    id = 5,
    name = 'Joaquin Valencia',
    subjects = ['Math', 'Chemistry', 'English']

)

student_6 = Students(
    id = 6,
    name = 'Alejandro Bernal',
    subjects = ['Arts', 'Geography']

)

student_7 = Students(
    id = 7,
    name = 'Andres Saavedra',
    subjects = ['Arts', 'Biology']

)



# ------------------------ Define Subjects ------------------

subject_1 = Subject(
    id = 1,
    name = 'Math',
    schedule =

)

subject_2 = Subject(
    id = 2,
    name = 'Physics',
    schedule =

)

subject_3 = Subject(
    id = 3,
    name = 'Astronomy',
    schedule =

)

subject_4 = Subject(
    id = 4,
    name = 'Biology',
    schedule =

)

subject_5 = Subject(
    id = 5,
    name = 'English',
    schedule =

)

subject_6 = Subject(
    id = 6,
    name = 'Arts',
    schedule =

)

subject_6 = Subject(
    id = 6,
    name = 'Geography',
    schedule =

)
subject_6 = Subject(
    id = 6,
    name = 'Chemistry',
    schedule =

)


# ------------------------ Define Students ------------------
