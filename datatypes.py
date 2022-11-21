# number
num1=2
num2=3

print(num1**num2)
print(num1/num2)
print(num1//num2)

print(float(num2))
num3=3.5
print(int(num3))

#string
first='First String'
second="SECOND"
third="""third"""

print(first[3])
print(first[-1])
print(first[3:5])
print(first[3:])
print(first[:5])
print(len(first))
print(first.upper())
print(first.lower())
print(first.count("i"))
print(first.find("i"))
print(second.isupper())
print(third.islower())

#list
lst=[1,2,"hi","python",2.3,5,2,"Hi",2]

newlst=[2,3,4]
appendlst=["Append","Testing","is","start",1]
extendlst=["Extend","Testing","is","start",2]
print(lst,type(lst))
print(lst[0])
print(lst[1:3])
print(lst[2:])
print(lst[:3])
print(newlst*2)
print(lst+newlst)
#print(lst)
lst.extend(extendlst)
print(lst)


lst.append(appendlst)
print(lst)

print(lst.count(2))

sortlst=['A','d','C','e',"B"]
#sortlst.sort()
#print(sortlst)
print(sorted(sortlst))
reverselst=['A','d','C','e',"B"]
reverselst.reverse()
print(reverselst)

a=['A','c','D','G','f']
print(sorted(a))
ls=sorted(a,key=lambda x:x.upper())
print(ls)

lst1=[1,2,3,[4,5,6]]
print(lst1[3])

#tuple
tup=(1,2,"Hi",3,"Python")
print(tup,type(tup))
print(list(tup))

#dictionary
dic={"id":243,"name":"John",'address':"Yangon"}
print(dic,type(dic))
print(dic.keys())
print(dic.values())

