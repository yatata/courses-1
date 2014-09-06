# Define a procedure, factorial, that
# takes one number as its input
# and returns the factorial of
# that number.

def factorial(n):
    x = 1
    while n > 1:
        x = x * n
        n = n - 1 
    return x
   
print factorial(4)
#>>> 24
print factorial(5)
#>>> 120
print factorial(6)
#>>> 720