# Lists contain regular Python objects, separated by commas and surrounded by brackets.
# The elements in a list can have any data type, and they can be mixed.
# You can even create a list of lists.

# creating a list
list_1 = [1, 2, 3]
list_2 = ["a", "b", "c", "d", "e", "f"]
list_3 = ["a", 7, "apple", {"Rabbit": 1}]
list_4 = [list_1, list_2]
print("\nThe  created lists are:\n")
print(f"List 1: {list_1}")
print(f"List 2: {list_2}")
print(f"List 3: {list_3}")
print(f"List 4: {list_4}\n")

# appending to a list
list_5 = list(["Apple"])
print(f"List before appending values: {list_5}")
list_5.append("orange")
list_5.append("Banana")
print(f"List after appending values: {list_5}\n")

# calling list element by its index
list_6 = list("christmas")
print(f"List: {list_6}")
print(f"element at index 0: {list_6[0]}")
print(f"element at index 5: {list_6[5]}")
print(f"element at last index: {list_6[-1]}\n")

# merging two lists
print(f"List 1: {list_1}")
print(f"List 2: {list_2}")
print(f"List 1 + List 2 : {list_1+list_2}\n")

# removing list elements using pop
print(f"List : {list_2}")
list_2.pop(4)
print(f"List after removing element using pop : {list_2}\n")

# removing list elements using del
print(f"List : {list_2}")
del(list_2[2])
print(f"List after removing element using del : {list_2}\n")

# removing specific elements from a list
print(f"List : {list_6}")
list_6.remove("m")
print(f"List after removing element using remove : {list_6}\n")

# removing list elements using pop
print(f"List : {list_6}")
list_6.clear()
print(f"List after clearing it : {list_6}")

