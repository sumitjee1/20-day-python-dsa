def find_max_min(numbers):
    max_value = numbers[0]
    min_value = numbers[0]

    for num in numbers:
        if num > max_value:
            max_value = num
        if num < min_value:
            min_value = num

    return max_value, min_value

numbers = [45, 12, 89, 23, 67, 38, 5]
max_value, min_value = find_max_min(numbers)
print(f"Max value: {max_value}")
print(f"Min value: {min_value}")