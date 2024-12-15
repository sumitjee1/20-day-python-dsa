#Code to check if the element is present in the tuple or not
fruits = ("apple", "banana", "cherry", "date")

fruit_to_check = "banana"
if fruit_to_check in fruits:
    print(f"{fruit_to_check} is in the tuple.")
else:
    print(f"{fruit_to_check} is not in the tuple.")
