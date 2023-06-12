class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.course_grades:
                lecturer.course_grades[course] += [grade]
            else:
                lecturer.course_grades[course] = [grade]
        else:
            return 'Ошибка'
            
    def avarage_student(self):
        total = 0
        for i in self.grades:
            rate = 0
            avarage_grade = 0
            for j in self.grades[i]:
                rate += j
            avarage_grade = rate/len(self.grades[i])
            total += avarage_grade
        avarage_total_student = total/len(self.grades)
        return round(avarage_total_student, 1)
    
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Некорректное сравнение')
            return
        return self.avarage_student() < other.avarage_student()
        
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.avarage_student()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res
    
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.course_grades = {}

    def avarage_lec(self):
        total = 0
        for i in self.course_grades:
            rate = 0
            avarage_course = 0
            for j in self.course_grades[i]:
                rate += j
            avarage_course = rate/len(self.course_grades[i])
            total += avarage_course
        avarage_total_lec = total/len(self.course_grades)
        return round(avarage_total_lec, 1)
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Некорректное сравнение')
            return
        return self.avarage_lec() < other.avarage_lec()

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avarage_lec()}'
        return res

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
            
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

def avarage_grade_for_student(student_list, course):
    total_grades = []
    counter = 0
    for student in student_list:
        if course in student.grades:
            grades = student.grades[course]
            total_grades.extend(grades)
            counter += len(grades)
    if counter > 0:
        average_grade = sum(total_grades) / counter
        print(f'Средняя оценка за домашние задания курса {course} - {round(average_grade, 1)}')
    else:
        return 'Нет оценок для данного курса'

def avarage_grade_for_lecturer(lecturer_list, course):
    total_grades = []
    counter = 0
    for lecturer in lecturer_list:
        if course in lecturer.course_grades:
            grades = lecturer.course_grades[course]
            total_grades.extend(grades)
            counter += len(grades)
    if counter > 0:
        average_grade = sum(total_grades) / counter
        print(f'Средняя оценка за лекции курса {course} - {round(average_grade, 1)}')
    else:
        return 'Нет оценок для данного курса'

student_1 = Student('Ruoy', 'Eman', 'Male')
student_1.courses_in_progress += ['Python', 'Java']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Egor', 'Velikiy', 'Male')
student_2.courses_in_progress += ['Python', 'FullStack']
student_2.finished_courses += ['Введение в программирование']

rev_1 = Reviewer('Ivan', 'Ivanov')
rev_1.courses_attached += ['Python', 'FullStack']

rev_2 = Reviewer('Anna', 'Vladimirovna')
rev_2.courses_attached += ['Python', 'Java']

lec_1 = Lecturer('Petr', 'Petrov')
lec_1.courses_attached += ['Python', 'FullStack', 'Java']

lec_2 = Lecturer('Eva', 'Boyko')
lec_2.courses_attached += ['FullStack', 'Java']

students_list = [student_1, student_2]
lecturers_list = [lec_1, lec_2]

rev_1.rate_hw(student_1, 'Python', 10)
rev_1.rate_hw(student_1, 'Python', 8)
rev_1.rate_hw(student_1, 'Python', 10)

rev_2.rate_hw(student_1, 'Java', 10)
rev_2.rate_hw(student_1, 'Java', 9)
rev_2.rate_hw(student_1, 'Java', 10)

rev_1.rate_hw(student_2, 'FullStack', 9)
rev_1.rate_hw(student_2, 'FullStack', 10)
rev_1.rate_hw(student_2, 'FullStack', 9)

rev_2.rate_hw(student_2, 'Python', 10)
rev_2.rate_hw(student_2, 'Python', 7)
rev_2.rate_hw(student_2, 'Python', 8)

student_1.rate_lec(lec_1, 'Python', 9)
student_1.rate_lec(lec_1, 'Java', 7)
student_1.rate_lec(lec_2, 'Java', 9)
student_2.rate_lec(lec_1, 'Python', 10)
student_2.rate_lec(lec_1, 'FullStack', 9)
student_2.rate_lec(lec_2, 'FullStack', 9)


print(student_1)
print()
print(student_2)
print()
print(student_1 > student_2)
print()
print(rev_1)
print()
print(rev_2)
print()
print(lec_1)
print()
print(lec_2)
print()
print(lec_1 > lec_2)
print()
avarage_grade_for_student(students_list, 'Python')
avarage_grade_for_student(students_list, 'FullStack')
avarage_grade_for_student(students_list, 'Java')

print()

avarage_grade_for_lecturer(lecturers_list, 'Python')
avarage_grade_for_lecturer(lecturers_list, 'FullStack')
avarage_grade_for_lecturer(lecturers_list, 'Java')