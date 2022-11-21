class library:
    def __init__(self,name,password):
        self.name=name
        self.password=password

    def login(self):
        print(self.name," login")


class Person:
    def __init__(self,name):
        self.name=name

    def bookChecking(self):
        print("Book checking!")