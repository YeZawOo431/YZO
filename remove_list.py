def remove_list(first,second):
    #third_list=list(set(first).difference(second)) #set difference method
    #third_list=list(set(first)-set(second))    #set difference method
    third_list=[element for element in first if element not in second]  #list comprehension
    return third_list        

first_list=["red","blue","green","orange","pink","black","gray","white","yellow"]
sec_list=["yellow","pink","black","blue"]
#first_list=[1,2,3,4,5,6,7,8]
#sec_list=[6,7,8]
#print(set(first_list))
#print(set(sec_list))
print("Result List: ",remove_list(first_list,sec_list))
