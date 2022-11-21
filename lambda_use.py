square=lambda side:side*side

side=int(input("Enter a number:"))
print("Square: ",square(side),"\n")


print("lambda 1: ",(lambda a,b,c:a*b*c)(1,2,3))
print("lambda 2: ",(lambda a,b,c=3:a*b*c)(1,2))
print("lambda 3: ",(lambda a,b,c:a*b*c)(1,2,c=3))
print("lambda 4: ",(lambda *addargs:sum(addargs))(1,2,3))
print("lambda 5: ",(lambda **addkwargs:sum(addkwargs.values()))(one=1,two=2,three=3))
print("lambda 6: ",(lambda a,b=0,c=0:a*b*c)(1,b=2,c=3),"\n")

fullname=lambda firstname,lastname:f"What is your name?\nMy name is {firstname} {lastname}"

print(fullname("John","Smith"))

def fun(lastname):
    return lambda firstname:f"What is your name?\nMy name is {firstname} {lastname}"

fullname=fun("Smith")
print(fullname("John"))

mylist=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
newlist=list(filter(lambda x:(x%2==0),mylist))
print(newlist)