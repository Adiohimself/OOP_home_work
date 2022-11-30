class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.mid_rating = float()

    def __str__(self):
        grades_count = 0
        courses_in_progress_string = '_'.join(self.courses_in_progress)
        finished_courses_string = '_'.join(self.finished_courses)
        for mark in self.grades:
            grades_count += len(self.grades[mark])
        self.mid_rating = sum(map(sum, self.grades.values())) / grades_count
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: {self.mid_rating:.2f}\nfКурсы в процессе изучения: {courses_in_progress_string}\nЗавершенные курсы: {finished_courses_string}'
        return res

    def rate_hw(self, lecturer, course, grade):
        """оценки лектору от студентов, если это лектор ведет лекции по данному курсу у этого студента"""
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]

    def __lt__(self, other):
        """сравнение студентов между собой по средней оценке за домашние задания"""
        if not isinstance(other, Student):
            print('Некорректное сравнение')
            return
        return self.mid_rating < other.mid_rating

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.mid_rating = float()
        self.grades = {}

    def __str__(self):
        grades_count = 0
        for mark in self.grades:
            grades_count += len(self.grades[mark])
        self.mid_rating = sum(map(sum, self.grades.values())) / grades_count
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.mid_rating:.2f}'
        return res

    def __lt__(self, other):
        """сравнение лекторов между собой по средней оценке за лекции"""
        if not isinstance(other, Lecturer):
            print('Некорректное сравнение')
            return
        return self.mid_rating < other.mid_rating

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        """выставление оценки студенту за домашние задания"""
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]

    def __str__(self):
        """определение средней оценки"""
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

best_lecturer_1 = Lecturer('Robin', 'Bobin')
best_lecturer_1.courses_attached += ['Python']
best_lecturer_2 = Lecturer('Sub', 'Zero')
best_lecturer_2.courses_attached += ['Python']
best_lecturer_3 = Lecturer('Grommash', 'Hellscream')
best_lecturer_3.courses_attached += ['Python']
# Создание лекторов и курсов

cool_reviewer_1 = Reviewer('Some', 'Buddy')
cool_reviewer_1.courses_attached += ['Python']
cool_reviewer_1.courses_attached += ['Python']
cool_reviewer_2 = Reviewer('Some', 'One')
cool_reviewer_2.courses_attached += ['Python']
cool_reviewer_2.courses_attached += ['Python']
# Создание проверяющих и курсов

student_1 = Student('Fred', 'Durst')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Введение в программирование']
student_2 = Student('Chester', 'Bennington')
student_2.courses_in_progress += ['Python']
student_2.finished_courses += ['Введение в программирование']

student_3 = Student('Kurt', 'Cobain')
student_3.courses_in_progress += ['Python']
student_3.finished_courses += ['Введение в программирование']
# Создание студентов и курсов и завершенных курсов

student_1.rate_hw(best_lecturer_1, 'Python', 8)
student_1.rate_hw(best_lecturer_1, 'Python', 10)
student_1.rate_hw(best_lecturer_1, 'Python', 9)
student_1.rate_hw(best_lecturer_2, 'Python', 5)
student_1.rate_hw(best_lecturer_2, 'Python', 7)
student_1.rate_hw(best_lecturer_2, 'Python', 7)
student_1.rate_hw(best_lecturer_1, 'Python', 7)
student_1.rate_hw(best_lecturer_1, 'Python', 6)
student_1.rate_hw(best_lecturer_1, 'Python', 8)
student_2.rate_hw(best_lecturer_2, 'Python', 8)
student_2.rate_hw(best_lecturer_2, 'Python', 7)
student_2.rate_hw(best_lecturer_2, 'Python', 8)
student_3.rate_hw(best_lecturer_3, 'Python', 9)
student_3.rate_hw(best_lecturer_3, 'Python', 10)
student_3.rate_hw(best_lecturer_3, 'Python', 7)
# Оценки лекторам

cool_reviewer_1.rate_hw(student_1, 'Python', 7)
cool_reviewer_1.rate_hw(student_1, 'Python', 9)
cool_reviewer_1.rate_hw(student_1, 'Python', 9)
cool_reviewer_2.rate_hw(student_2, 'Python', 6)
cool_reviewer_2.rate_hw(student_2, 'Python', 4)
cool_reviewer_2.rate_hw(student_2, 'Python', 8)
cool_reviewer_2.rate_hw(student_3, 'Python', 7)
cool_reviewer_2.rate_hw(student_3, 'Python', 9)
cool_reviewer_2.rate_hw(student_3, 'Python', 10)
cool_reviewer_2.rate_hw(student_3, 'Python', 8)
cool_reviewer_2.rate_hw(student_3, 'Python', 9)
cool_reviewer_2.rate_hw(student_3, 'Python', 7)
# Оценки студентам

print(f'Студенты:\n\n{student_1}\n\n{student_2}\n\n{student_3}')
print()
# Вывод информации о студентах

print(f'Лекторы:\n\n{best_lecturer_1}\n\n{best_lecturer_2}\n\n{best_lecturer_3}')
print()
# Вывод информации о лекторах

print(f'Сравнение студентов по средним оценкам: '
      f'{student_1.name} {student_1.surname} < {student_2.name} {student_2.surname} = {student_1 > student_2}')
print()
# Вывод результатов сравнения студентов по средним оценкам

print(f'Сравнение лекторов по средним оценкам: '
      f'{best_lecturer_1.name} {best_lecturer_1.surname} < {best_lecturer_2.name} {best_lecturer_2.surname} = {best_lecturer_1 > best_lecturer_2}')
print()
# Вывод результатов сравнения лекторов по средним оценкам

student_list = [student_1, student_2, student_3]

lecturer_list = [best_lecturer_1, best_lecturer_2, best_lecturer_3]

def student_rating(student_list, course_name):
    """подсчет средней оценки за домашние задания
    по всем студентам на определенном курсе"""
    sum_all = 0
    count_all = 0
    for stud in student_list:
       if stud.courses_in_progress == [course_name]:
            sum_all += stud.mid_rating
            count_all += 1
    mid_for_all = sum_all / count_all
    return f'{mid_for_all:.2f}'

def lecturer_rating(lecturer_list, course_name):
    """подсчет средней оценки за лекции всех лекторов на определенном курсе"""
    sum_all = 0
    count_all = 0
    for lect in lecturer_list:
        if lect.courses_attached == [course_name]:
            sum_all += lect.mid_rating
            count_all += 1
    mid_for_all = sum_all / count_all
    return f'{mid_for_all:.2f}'

print(f"Средняя оценка для всех студентов по курсу {'Python'}: {student_rating(student_list, 'Python')}")
print()
# Вывод результатов подсчета средней оценки по всем студентам для определенного курса

print(f"Средняя оценка для всех лекторов по курсу {'Python'}: {lecturer_rating(lecturer_list, 'Python')}")
print()
# Вывод результатов подсчета средней оценки по всем лекорам для определенного курса