names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
import random

student_scores = {student: random.randint(1, 100) for student in names}
passed_students = {student: value for (student, value) in student_scores.items() if int(value) > 50}
print(passed_students)
