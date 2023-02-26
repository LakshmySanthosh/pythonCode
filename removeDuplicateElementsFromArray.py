# initializing array
a = []
unique = []
duplicate = []

# taking array input
n = int(input("Enter the number of elements in the array: "))
for i in range(0, n):
    m = int(input())
    a.append(m)

# removing duplicate elements and printing the array
for i in range(0, n):
    if a[i] not in unique:
        unique.append(a[i])
print(f"Array after removing duplicate elements is {unique}")
