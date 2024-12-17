#Code to Group numbers into even and odd categories.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = {num for num in numbers if num % 2 == 0}
odd_numbers = set(numbers) - even_numbers

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
