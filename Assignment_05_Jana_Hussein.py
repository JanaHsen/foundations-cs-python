class Course:
    def _init_(self, code, name, credit_hours): #class for the courses
        self.code = code
        self.name = name
        self.credit_hours = credit_hours

class Student: #class for the students with their name and id
    def _init_(self, id, name):
        self.id = id
        self.name = name
        self.courses = {} #dictionary that has the courses the student registered in

    def enroll(self, course): #class for enrolment in the courses
        if course.code in self.courses: #check if the student has already enrolled for the course
            print("Student already enrolled in this course")
        self.courses[course.code] = course #else add this course to the courses dictionary

class University:
    def _init_(self):
        self.students = []
        self.courses = {}

    def add_course(self, course):
        self.courses[course.code] = course

    def enroll_student(self, student_id, course_code):
        student = self.find_student(student_id)
        course = self.courses.get(course_code)
        if course:
            student.enroll(course)
        else:
            print("Course not found")
