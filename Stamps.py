#***************************************************************************
#
# Define a procedure, stamps, which takes as its input a positive integer in
# pence and returns the number of 5p, 2p and 1p stamps (p is pence) required 
# to make up that value. The return value should be a tuple of three numbers 
# (that is, your return statement should be followed by the number of 5p,
# the number of 2p, and the nuber of 1p stamps).
#
# The answer should use as few total stamps as possible by first using as 
# many 5p stamps as possible, then 2 pence stamps and finally 1p stamps as 
# needed to make up the total.
#
# Examples:
# print stamps(28)
#>>> (5,1,1)
#
#***************************************************************************

def stamps(n):
    a = n / 5
    b = ( n % 5) / 2
    c = ( n % 5) % 2
    return a,b,c
