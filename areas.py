#function
#def area(side1,side2):
#    return side1*side2

#lambda
area=lambda side1,side2:side1*side2


side=int(input("Enter a number for side1:"))
print("Square=",area(side,side))

leng=int(input("Enter a number for length:"))
width=int(input("Enter a number for width:"))
print("Rectangle=",area(leng,width))


