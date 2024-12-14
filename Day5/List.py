#Creating a list
my_list = [10, 20, 30, 40, 50, 60]

# 1.Indexing - Accessing elements at a specific index
print("Indexing:")
print("Element at index 0:", my_list[0])
print("Element at index 2:", my_list[2])  
print("Element at index -1:", my_list[-1]) 
print("Element at index -2:", my_list[-2])  

# 2.Slicing-Extracting a subset of the list
print("\nSlicing:")
print("Elements from index 1 to 4:", my_list[1:4]) 
print("Elements from index 2 to the end:", my_list[2:]) 
print("Elements from the beginning to index 3:", my_list[:3])
print("Every second element:", my_list[::2])  

# 3.Modifying a list
print("\nModifying a list:")
my_list[1] = 25 
print("After changing index 1 to 25:", my_list)

# 4.Adding elements to a list
print("\nAdding elements:")
my_list.append(70)  
print("After appending 70:", my_list)

my_list.insert(2, 15)  
print("After inserting 15 at index 2:", my_list)

# 5.Removing elements from a list
print("\nRemoving elements:")
my_list.remove(30)  # Removes the first occurrence of value 30
print("After removing 30:", my_list)

removed_element = my_list.pop(3)  
print("After popping element at index 3 :", removed_element)
print("List after pop:", my_list)

# 6.List length
print("\nLength of the list:", len(my_list))

# 7.Checking if an element exists
print("\nCheck if 50 is in the list:", 50 in my_list)  

# 8.Iterating over a list
print("\nIterating over the list:")
for item in my_list:
    print(item, end=" ")

# 9.List concatenation and repetition
print("\n\nConcatenating and repeating lists:")
another_list = [100, 200, 300]
concatenated_list = my_list + another_list
print("Concatenated list:", concatenated_list)

repeated_list = my_list * 2
print("Repeated list (2 times):", repeated_list)

# 10.Sorting and reversing a list
print("\nSorting and Reversing:")
my_list.sort() 
print("Sorted list:", my_list)

my_list.reverse() 
print("Reversed list:", my_list)

