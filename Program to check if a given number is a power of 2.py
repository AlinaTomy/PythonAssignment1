# Question 10: PROGRAM TO CHECK IF A NUMBER IS A POWER OF TWO
# explanation:
# The powers of 2 have only one set bit in their Binary representation.
# if we subtract 1 from a power of 2 what we get is 1s till the last unset bit,
# and if we apply Bitwise AND operator we should get only zeros.
# Suppose if there is a 1 to the left of first set bit, i.e., it is not a power of 2.
# We can clearly see that n & (n - 1) will not return 0.
# 16	    0	0	0	1	0	0	0	0
# 16-1=15	0	0	0	0	1	1	1	1
# 16 AND 15	0	0	0	0	0	0	0	0
# Hence, 16 is a power of 2.
# similarly,
# 15	    0	0	0	0	1	1	1	1
# 15-1=14	0	0	0	0	1	1	1	0
# 15 AND 14	0	0	0	0	1	1	1	0
# Hence, 15 is not a power of 2.
# therefore in order to check if a number (say n) is a power of two,
# we perform BITWISE AND OPERATION between n and (n-1)

n = int(input("enter the number you want to check for:"))
if (n & (n-1) != 0):
    print ("Number not power of 2")
else:
    print ("Number power of 2")


