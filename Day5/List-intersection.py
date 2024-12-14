def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

# Test
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7]
print(intersection(list1, list2))