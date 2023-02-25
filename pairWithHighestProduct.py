# initializing array
a = []

# taking array input
n = int(input("Enter the number of elements: "))
print("Enter the elements")
for i in range(0, n):
    m = int(input())
    a.append(m)
print(f"The array is {a}")

# giving values of first two elements to x and y
x = a[0]
y = a[1]

# finding the pair with highest product
for i in range(0, n):
    for j in range(i+1, n):
        if a[i]*a[j] > x*y:
            x = a[i]
            y = a[j]

# printing the pair with highest product
print(f"Maximum product is {x*y}")
print(f"The numbers that give the maximum product are: {x} and {y}")
