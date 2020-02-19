# Question-2: PROGRAM TO FIND THE SECOND LARGEST NUMBER IN THE LIST

List =[]
num= int(input("enter the number of elements in the list:"))
for i in range(1,num+1):
    element=int(input("enter the elements:"))
    List.append(element)
print(List.sort())
print("the second largest element in the list is:", List[-2])