def myFun():
    print("This is my function")

myFun()

#paramater passing
def isFun(name):
    print("This is "+name+" function")

isFun("second")
isFun("third")

def isStudent(name,address):
    print(name," lives in ",address)

isStudent("John","Yangon")
isStudent("Jeni","Bago")

#arbitary
def myHome(father,mother,*kids,who):
    times=["Eldest","Second","Youngest"]
    print("Father name is ",father)
    print("Mother name is ",mother)   
    print(times[who]," child is ",kids[who])

ch=int(input("Who do you know?:"))
if ch>0 and ch<4:
    myHome("U Zaw","Daw Khin","Min","Su","Tun",who=ch-1)

#keyword
def myHome(**parents):
    print("Father name is "+parents["father"])
    print("Mother name is "+parents['mother'])

myHome(father="U Zaw",mother="Daw Khin")

