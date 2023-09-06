# practice
courses = [
		{'title' : 'Python' , 'teacher' : 'Amiri'} ,
		{'title' : 'HTML'   , 'teacher' : 'Dehyami'},
		{'title' : 'PHP'    , 'teacher' : 'Enayati'},
		{'title' : 'Backend', 'teacher' : 'Abdolvand'}
]


class Users():   # parent
    """docstring for users"""
    def __init__(self, firstname, lastname):
        #super(users, self).__init__()
        self.fname = firstname
        self.lname = lastname

    def fullname(self):
        the_print = f'My name is {self.fname} {self.lname}'
        print(the_print)
        print (len(the_print)*'-')

class Student(Users):  # child
    """docstring for Student"""
    def __init__(self, firstname, lastname,email):
        super().__init__(firstname, lastname)
        self.email = email
        self.registered_courses = []
        self.payed = 0
        
    def fullname(self):
        print(f'I am student \nthe email is: {self.email}')
        super().fullname()

    def printcourse(self):
        # if self.registered_courses != None: ------> [] != None so dont go to else
        # if len(self.registered_courses) ==0:  ----> its OK
        if self.registered_courses:
            for item in self.registered_courses:
                print(item['title'])
        else:
            print('you dont have any course yet')

class Teacher(Users):
    """docstring for Teacher"""
    def __init__(self, firstname, lastname, id_code):
        super().__init__(firstname, lastname)
        self.code = id_code


    def fullname(self):
        print(f"i'm a teacher")
        super().fullname()


u1 = Users('ali', 'mmw')
u1.fullname()

s1 = Student('hossein', 'abdolvand', 'dd@#g.com')
s1.fullname()

t1 = Teacher('ostad' , 'os2', 12122)
t1.fullname()

# +++++++++++++++++++87++++++++++++++++++++++++++
s1.registered_courses.append(courses[2])

print(s1.registered_courses)

# s1.registered_courses.append(courses[0:1])  ---->   show error
s1.registered_courses.append(courses[0])
s1.printcourse()

print(10*"-=-")

s2 = Student('ahm', 'ahmadsi', 'fffdffdfdff@gmaill.com')
s2.printcourse()
