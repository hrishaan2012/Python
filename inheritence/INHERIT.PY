class person:
    def __Init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber

class employee(person):
    def __init__(self,name,idnumber,salary,post):
        self.salary=salary
        self.post=post
        person.__Init__(self,name,idnumber)

a=employee("Rahul",886012,200000,"Intern")
print("Name:",a.name,"ID:",a.idnumber,"Salary:",a.salary,"Post:",a.post)