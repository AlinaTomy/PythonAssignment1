# Question-9: PYTHON PROGRAM TO PRINT MULTIPLICATION TABLE OF A GIVEN NUMBER
# we first take a number from the user and store it in a variable n
# using the print statement, we print the table till 10
n = int(input("enter the number to display multiplication table: "))
for i in range(1, 11):
    print(n, "x", i, "=", n*i)
