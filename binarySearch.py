# initializing array
a = []

# taking array input
n = int(input("Enter the number of elements in the array: "))
print("Enter sorted array")
for i in range(0, n):
    m = int(input())
    a.append(m)

# searching using binary search
first = 0
last = n
ele = int(input("Enter the element to search: "))
while first <= last:
    mid = int((first+last)/2)
    if a[mid] < ele:
        first = mid+1
    elif a[mid] > ele:
        last = mid-1
    else:
        print(f"Element found at {mid+1} position")
        break
if first > last:
    print("Element not found!!!")
