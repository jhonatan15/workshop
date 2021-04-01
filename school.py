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

class Subjects:
    id = ''
    name = ''
    Schedule = ''

class classNotes:
    id = ''
    valor = ''


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
