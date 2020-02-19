# Question-3, PROGRAM TO PUT EVEN AND ODD NUMBERS IN A LIST TO TWO DIFFERENT LISTS
# there are two ways for the same

# method1: using for function,
# even numbers when divided by 2 gives 0 as remainder,
# while odd numbers give other numbers as remainder
MainList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = []
odd_list = []
for i in (MainList):
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)
print("list with even elements:", even_list)
print("list with odd elements:", odd_list)

# method2: taking input from users and then creating two different lists containing odd and even elements
MainList = []
even_list = []
odd_list = []
num = int(input("enter the number of elements in List:"))
for i in range(0, num):
    element=int(input("enter elements:"))
    MainList.append(element)
for i in (MainList):
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)
print(MainList)
print("list with even elements:", even_list)
print("list with odd elements:", odd_list)
