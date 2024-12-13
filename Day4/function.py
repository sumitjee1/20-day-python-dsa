def greet(): #(Defining the function)
    print("Hello,Namaste,sasriyakal")

greet() #(Calling the function)

#parameter in function
def greet(name):
    print(f"Hello, {name}! Welcome to Python 20-Day Challenge")

greet("rohit")
greet("amaira")

#returning something from function
def square(number):
    return number * number

result = square(5)
print(f"The square of 5 is {result}")

#function with N number of arguments
def print_numbers(*arg):
    for number in arg:
        print(number)

print_numbers(1, 2, 3, 4, 5)