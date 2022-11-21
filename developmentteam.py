class Development:
    def __init__(self,name,dep):
        self.name=name
        self.dep=dep
    
    def coding(self):
        print(self.name,"from",self.dep)
        print("Coding is start!")

#if __name__=="__main__":
#    name=input("Enter a name:")
#    dep=input("Enter a department:")
#    develop=Development(name,dep)
#    develop.coding()


class Odoo(Development):
    def __init__(self,name,dep)->None:
        self.name=name
        self.dep=dep

    
    

class Web(Development):
    def __init__(self,name,dep)->None:
        self.name=name
        self.dep=dep


name=input("Enter a name:")
odoo=Odoo(name,"Odoo")
odoo.coding()

name=input("Enter a name:")
web=Web(name,"Web")
web.coding()
        