# Question 1: PROGRAM TO FIND THE LARGEST NUMBER IN A LIST
# 4 ways to find out the largest number in a list

# method 1: Sort the list in ascending order and display the last element
List = [23,32,45,54,6,67,87,8]
List.sort()
print("the largest number in the list is:", List[-1])

# method 2: display the largest number using built-in method max()
List = [23,32,45,54,6,67,87,8]
print("the largest number in the list is:", max(List))

# method 3: displaying the largest element in a list entered by the user using Max() method
List =[]
num= int(input("enter the number of elements in the list:"))
for i in range(1,num+1):
    element=int(input("enter the elements:"))
    List.append(element)
print(List)
print("the largest element in the list is:", max(List))

# method 4: displaying the largest element in a list entered by the user using sort() method
List =[]
num= int(input("enter the number of elements in the list:"))
for i in range(1,num+1):
    element=int(input("enter the elements:"))
    List.append(element)
print(List.sort())
print("the largest element in the list is:", List[-1])