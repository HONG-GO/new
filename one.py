print("上传")
Course_list = []


class School(object):
    def __init__(self, school_name):
        self.school_name = school_name
        self.student_list = []
        self.teachers_list = []

        global Course_list

    def hire(self, obj):
        self.teachers_list.append(obj.name)
        print("我们现在聘请一个新老师{}".format(obj.name))

    def enrol(self, obj):
        self.students_list.append(obj.name)
        print("我们又有一个新学员{}".format(obj.name))


class Grade(School):
    def __init__(self, school_name, grade_code, grade_course):
        super(Grade, self).__init__(school_name)
        self.code = grade_code
        self.course = grade_course
        self.members = []
        Course_list.append(self.course)
        print("我们现在有了{}的{}的{}".format(self.school_name, self.code, self.course))

    def course_info(self):
        print("课程大纲{} 是 day01,day02,day03".format(self.course))


Python = Grade("BJ", 3, 'Python')
Linux = Grade("CD", 1, 'linux')


class School_member(object):
    def __init__(self, name, age, sex, role):
        self.name = name
        self.age = age
        self.sex = sex
        self.role = role
        self.course_list = []
        print("我叫{}，我是一个{}".format(self.name, self.role))


stu_mum_id = 00


class Student(School_menber):
    def __init__(self, name, age, sex, role, course):
        super(Student, self).__init__(name, age, sex, role)
        global stu_mum_id
        stu_mum_id += 1
        stu_id = course.school_name + "S" + str(course.code) + str(str_mum_id).zfill(2)
        # zfill 填充的作用，当只有一位数时前面填充0，只能对str类型做操作
        self.id = stu_id
        self.mark_list = {}

    def study(self, course):
        print("我来这里学习{}课，我的学号是{}".format(course.course, self, id))

    def pay(self, course):
        print("我交了一千块钱给{}".format(course.course))
        self
        course_list.append(course.course)

    def Praise(self, obj):
        print("{}觉得{}课真棒".format(self.name, obj.name))

    def mark_check(self):
        for i in self.mark_list.items():
            print(i)

    def out(selfJ):
        print("我离开了")


tea_mum_id = 00


class Teacher(School_mumber):
    def __init__(self, name, age, sex, role, course):
        super(Teachers, self).__init__(name, age, sex, role)
        glogal
        tea_mum_id
        tea_mum_id += 1
        tea_id = course.school_name + "T" + str(course.code) + str(tea_mum_id).zfill(2)
        self.id = tea_id

    def teachers(self, course):
        print("我来这里讲{}门课，我的id是{}".format(course.course, self.id))

    def record_mark(self, Date, course, obj, level):
        obj.mark_list["Day" + Date] = level


a = Student("小张", 18, "M", "student", Python)
python.error(a)
a.study(Python)
a.pay(python)

a = Student("小王", 22, "F", "student", Python)
python.error(b)
b.study(Python)
b.pay(python)

t = Teachers("小周", 30, "M", "teacher", Python)
Python.hire(t)
t.teach(Python)
t.record_mark('1', Python, a, "A")
t.record_mark('1', Python, a, "B")
t.record_mark('2', Python, a, "A")
t.record_mark('2', Python, a, "A")

print(b.course_list)
b.mark_check
b.out()
print("给好评")
a.praise(t)