# initializing arrays
a = []
unique = []
duplicate = []

# taking array input
n = int(input("Enter the number of elements of the array: "))
print("Enter the elements")
for i in range(0, n):
    m = int(input())
    a.append(m)
print(f"The array is {a}")

# finding duplicate elements
for i in range(0, n):
    if a[i] not in unique:
        unique.append(a[i])
    elif a[i] not in duplicate:
        duplicate.append(a[i])

# printing duplicate elements
if not duplicate:
    print("No duplicate elements!!!")
else:
    print(f"The duplicate elements are: {duplicate}")
