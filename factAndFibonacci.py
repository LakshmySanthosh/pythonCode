n = int(input("Enter a number to find factorial: "))
fact = 1
for i in range(1,n+1):
    fact *= i
print(f"Factorial of the number {n} is {fact}\n")

n = int(input("Enter the range to print fibonacci series: "))
a=0
b=1
print("The fibonacci series is: ")
for i in range(n):
    print(a)
    a, b = b, a + b


