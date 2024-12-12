#code to print sum of N numbers given by the user 
n = int(input("Enter a number: "))
sum_numbers = 0
for i in range(1, n + 1):  
    sum_numbers += i
print(f"The sum of numbers from 1 to {n} is {sum_numbers}.")
