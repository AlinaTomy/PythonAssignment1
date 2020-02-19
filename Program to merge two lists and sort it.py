# Question 4: PYTHON PROGRAM TO MERGE TWO LISTS INTO ONE AND SORT IT
# given below are 4 methods to do the same

#method1: by using concetenation (+ operator) and then by using sort() method
list1 = [1, 9, 3, 4]
list2 = [5, 11, 98, 8]
list3 = list1 + list2
print("the merged list is:", (list3))
list3.sort()
print("the new sorted list is:", list3)

#method2: taking input from users to create 2 lists and later merging and sorting them
listA=[]
listB=[]
numA=int(input("enter the number of elements in list_A:"))
for i in range(numA):
    elementA=int(input("enter the elements:"))
    listA.append(elementA)
print("elements in list_A are:",listA)

numB=int(input("enter the number of elements in list_B:"))
for i in range(numB):
    elementB=int(input("enter the elements:"))
    listB.append(elementB)
print("elements in list_B are:",listB)

listC= listA + listB
print("the newly merged listC is:",(listC))
listC.sort()
print("the newly sorted listC is:",listC)

#method3: by pre defining a function- Merge()
def Merge(list1, list2):
    final_list = list1 + list2
    final_list.sort()
    return (final_list)
list1 = [5,67,1]
list2 = [56,90,7]
print(Merge(list1,list2))

#method4:  using the extend() method and then sorting it
list1 = [1, 22, 3]
list2 = [94, 5, 78]
list1.extend(list2)
list1.sort()
print(list1)

