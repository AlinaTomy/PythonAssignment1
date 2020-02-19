# Question-6: PYTHON PROGRAM THAT MAPS TWO LISTS INTO A DICTIONARY
# can be done in 2 different ways

# method 1: using the zap() method
keys = ["Apple", "Grapes", "Banana"]
values = ["red", "green", "yellow"]
print(keys)
print(values)
new_dict = dict(zip(keys, values))
print(new_dict)

# method 2: using dictionary comprehension
keys =["Name", "RollNo", "Age"]
values =["Alina", 4, 23]
print("List containing Keys:", keys)
print("List containing Values:", values)
new_dict = {keys[i]:values[i] for i in range(len(keys))}
print("The resultant New Dictionary is:", new_dict)

# method 3: taking input from users and later using zip function
keys = []
values = []
n = int(input("enter the number of elements in the dictionary:"))

for i in range(0,n):
    element = (input("enter element for Keys List:"))
    keys.append(element)
print("List containing Keys:", keys)

for i in range(0,n):
    element = (input("enter element for Values List:"))
    values.append(element)
print("List containing values:", values)
new_dict =dict(zip(keys,values))
print("the resultant new dictionary is:",new_dict)









