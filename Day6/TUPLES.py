#Code to study tuple and perform various operations on it
#Creating a tuple
my_tuple = (10, 20, 30, 40, 50)
print("Original tuple:", my_tuple)

#Indexing
print("\nIndexing:")
print("First element:", my_tuple[0])  # Index 0
print("Last element:", my_tuple[-1])  # Negative index

#Slicing
print("\nSlicing:")
print("Slice from index 1 to 3:", my_tuple[1:4])  # Excludes index 4
print("Slice from start to index 2:", my_tuple[:3])
print("Slice from index 2 to end:", my_tuple[2:])
print("Full tuple with step 2:", my_tuple[::2])  # Every second element

#Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated = tuple1 + tuple2
print("\nConcatenation:")
print("Concatenated tuple:", concatenated)

#Repetition
repeated = tuple1 * 3
print("\nRepetition:")
print("Repeated tuple:", repeated)

#Membership check
print("\nMembership Check:")
print("Is 2 in tuple1?", 2 in tuple1)
print("Is 10 in tuple1?", 10 in tuple1)

#Length of the tuple
print("\nLength:")
print("Length of my_tuple:", len(my_tuple))

#Maximum and Minimum
print("\nMaximum and Minimum:")
print("Maximum in my_tuple:", max(my_tuple))
print("Minimum in my_tuple:", min(my_tuple))

#Nested Tuples
nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print("\nNested Tuple:")
print("Nested tuple:", nested_tuple)
print("First sub-tuple:", nested_tuple[0])
print("Second element of first sub-tuple:", nested_tuple[0][1])

#Iteration
print("\nIteration:")
for item in my_tuple:
    print(item)
