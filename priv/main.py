class myclass:
    __privateVar = 27
    def __privVar(self):
       print ("i am inside the class")     

    def hello(self):
        print ("My class is",myclass.__privateVar)
foo=myclass()
foo.hello()
foo.__privateVar
