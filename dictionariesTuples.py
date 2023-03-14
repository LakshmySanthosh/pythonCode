# Tuples are immutable lists.
# Elements of a list can be modified, but elements in a tuple can only be accessed, not modified.

# Elements in a tuple are given inside () and separated by commas
tuple_1 = (1, 3, 5, 7, 8, 9, 10)

# Tuple with one element always has a comma at the end
tuple_2 = (45,)

print(f"\nTuple with multiple elements = {tuple_1}\n")
print(f"Tuple with 1 element = {tuple_2}\n\n")

# Dictionaries are made up of key: value pairs.
# In Python, lists and tuples are organized and accessed based on position.
# Dictionaries in Python are organized and accessed using keys and values.

# Elements in a dictionary are given inside {} and separated by commas

# dictionary using integer keys
dict_1 = {1: "Arya", 2: "Zara", 3: "Ankit"}
print(f"dictionary using integer keys = {dict_1}\n")
# dictionary using char keys
dict_2 = {"a": "hey", "b": "How", "c": "are", "d": "you?"}
print(f"dictionary using character keys = {dict_2}\n")

# changing elements of a dictionary
dict_3 = {0: "apple", 1: "orange", 2: "banana"}
print(f"dictionary before element change = {dict_3}")
dict_3[0] = "zero"
dict_3[1] = "one"
dict_3[2] = "two"
print(f"dictionary after element change = {dict_3}\n")

# adding elements to a dictionary
dict_4 = dict()
print(f"dictionary before adding elements = {dict_4}")
# dict_4 = {} can also be used
dict_4["a"] = "apple"
dict_4["b"] = "bat"
dict_4["c"] = "cat"
print(f"dictionary after adding elements = {dict_4}\n")

# removing element from dictionary
dict_5 = {"A": "Anjali", "B": "Bhavana", "C": "Chandana"}
print(f"Dictionary before removing element = {dict_5}")
dict_5.pop("B")
print(f"Dictionary after removing element = {dict_5}")
