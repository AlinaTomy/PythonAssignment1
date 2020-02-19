# Question-8: PYTHON PROGRAM TO PRINT AN INVERTED STAR PATTERN
# We first take a value from the user (the number of rows) and store it in a variable n
# Then the for loop enables i to range between n-i to 0 with a decrement of 1 with each iteration
# After that, for each iteration,
# ” ” is multiplied with n-i and
# ‘*’ is multiplied with i to create correct space between the stars
# ie  Multiply empty spaces with n-i and ‘*’ with i and print both of them
# And finally desired pattern will be printed.

n = int(input("enter the number of rows you want in the pattern:" ))
for i in range(n, 0, -1):
    print((n-1)* ' ' + i * '*')
