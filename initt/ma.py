class employee:
    def __init__(self):
        print("Employee created")
    def __del__(self):
        print("Destructor called")
def createobject():
        print("Making Object")
        object=employee()
        print("Functioning")
        return object
print("Creating object")
createobject()
print("Program Ended")