class student:
    def __init__(self,name,id,current_class) -> None:
        self.name=name
        self.id=id
        self.current_class=current_class
    
    def __repr__(self) -> str:
        return f'stuent name: {self.name}, id: {self.id}, current_class: {self.current_class} '
    
class teacher:
    def __init__(self,name,id, course_name) -> None:
        self.name=name
        self.id=id
        self.course_name=course_name
    def __repr__(self) -> str:
        return f'teacher name: {self.name}, id: {self.id}, course_name: {self.course_name}'
    
class school:
    def __init__(self,name) -> None:
        self.name=name
        self.teachers=[]
        self.students=[]
    
    def add_teacher(self,name,course_name):
        id=len(self.students)+1
        Teacher=teacher(name,id,course_name)
        self.teachers.append(Teacher)
    
    def enroll(self,name,fee):
        if fee<6500:
            print("need more fee")
        else:
            id=len(self.students)+1
            Student=student(name,id,'c')
            self.students.append(Student)
    
    def __repr__(self) -> str:
        print("welcome",self.name)
        print(".................................")
        print('...........OUR teacher........................')
        for teacher in self.teachers:
            print(teacher)
        print('......................')
        print(">>>>>>>>>>>>..................our steudent...........")
        for stuent in self.students:
            print(student)
        
        print("....all done...    best of luck")



phitron = school('Phitron')
phitron.enroll('alia', 5200)
phitron.enroll('rani', 8000)
phitron.enroll('aishwaraiya', 7000)
phitron.enroll('vaijaan', 90000)

phitron.add_teacher('Tom Cruise', 'Algo')
phitron.add_teacher('Decap', 'DS')
phitron.add_teacher('AJ', 'Database')

print(phitron)