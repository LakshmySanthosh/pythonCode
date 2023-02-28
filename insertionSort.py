# initializing array
a = []

# taking array input
n = int(input("Enter the number of elements in the array: "))
for i in range(0, n):
    m = int(input())
    a.append(m)

# sorting using insertion sort
for i in range(1, n):
    key = a[i]
    j = i-1
    while j >= 0 & a[j] > key:
        a[j+1] = a[j]
        j = j-1
    a[j+1] = key
print(f"The sorted array is {a}")
############################################
############################################
############################################

