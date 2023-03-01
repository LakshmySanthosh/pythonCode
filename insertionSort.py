# initializing array
a = []

# taking array input
n = int(input("Enter the number of elements in the array: "))
for i in range(0, n):
    m = int(input(f"Enter element {i+1}: "))
    a.append(m)

# sorting using insertion sort
for i in range(1, n):
    key = a[i]
    j = i
    while j > 0 and a[j-1] > a[j]:
        a[j-1], a[j] = a[j], a[j-1]
        j = j-1

print(f"The array sorted using insertion sort is {a}")
