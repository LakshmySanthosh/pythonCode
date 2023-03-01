# initializing array
a = []

# taking array input
n = int(input("Enter the number of elements in the array: "))
for i in range(0, n):
    m = int(input(f"Enter element {i+1}: "))
    a.append(m)

# sorting using bubble sort
for i in range(0, n):
    for j in range(0, n-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print(f"The array sorted using bubble sort is {a}")
