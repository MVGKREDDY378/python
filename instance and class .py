class student:
    school_name='abc school'
    def _init_(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print('student',self.name,self.age,student.school_name)
    def change_age(self,new_age):
        self.new_age
    def modify_school_name(cls,new_name):
        cls.schoolname=new_name
    s1=student("harry",12)
    s1.show()
    s1.change_age(14)
    student.modify_school_name('xyzschool')
    s1.show
