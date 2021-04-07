class infStudent():

    def __init__(self, id, student_id, subject_id, teacher_id):
        self.id = id
        self.student_id = student_id
        self.subject_id = subject_id
        self.teacher_id = teacher_id

    def obt_avg(self, notes):
        sum_notes = 0
        count_notes = 0
        
