# function to find factorial of a number
def fact(r):
    factorial = 1
    for k in range(1, r):
        factorial = factorial*k
    if r == 1:
        return 1
    else:
        return factorial


# Taking number of rows as input
n = int(input("Enter the number of rows: "))

# creating and printing pascal's triangle
for i in range(0, n):
    for j in range(0, n-i):
        print(" ", end="")
    for j in range(0, i+1):
        nCr = fact(i)/(fact(j)*fact(i-j))
        print(int(nCr), end=" ")
    print()
