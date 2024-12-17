#Code To Identify Unique Items from Multiple Lists

list1 = [1, 2, 3]
list2 = [3, 4, 5]
list3 = [5, 6, 7]

unique_items = set(list1 + list2 + list3)
print("Unique items from all lists:", unique_items)
