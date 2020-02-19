# Question 7: PYTHON PROGRAM THAT DISPLAYS WHICH LETTERS ARE IN TWO STRINGS BUT NOT IN BOTH

# We first take two string inputs from the users and store them in separate variables
# we convert the two strings into sets and perform the operation of symmetric difference using ^ operator
# by doing so, we get the letters that are in the two strings but not present in both
# In mathematics, the symmetric difference, also known as the disjunctive union,
# of two sets is the set of elements which are in either of the sets and not in their intersection
# we then store the result in a list
# we then print the list(which now contains the symmetric difference of the two strings)

str1 = str(input("enter the first string:"))
str2 = str(input("enter the second string:"))
a = list(set(str1) ^ set(str2))
print("the letters that are in the two strings but not in both:", a)
