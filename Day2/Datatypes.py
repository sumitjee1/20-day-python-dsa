#DATA DELVE (Day2)
#program for different data types
#numeric DATATYPES
a = 10          # int
b = 3.14        # float
c = 2 + 3j      # complex
print("integer value of a is =",a)
print("float value of b is =",b)
print("complex value of c is =",c)

#STRING DATATYPE
inp=input("Please enter any string(statement):")
print("you have written :",inp)

#LIST DATATYPE
fruits = ["apple", "banana", "cherry"] 
numbers = [1, 2, 3, 4, 5] 
print("In fruits you have :",fruits)
print("In numbers you have :",numbers)

#TUPLE DATATYPE (similar to list but tuple is immutable and list can be changed)
fruits1 = ("apple", "banana", "cherry")  
numbers1 = (1, 2, 3, 4, 5)
print("In fruits you have :",fruits1)
print("In numbers you have :",numbers1)

#SET DATATYPE(its unorderd)
fruits_set = {"apple", "banana", "cherry"}  
numbers_set = {1, 2, 3, 4, 5} 
print("In fruits you have :",fruits_set)
print("In numbers you have :",numbers_set)

#DICTIONARY DATATYPE(It have keys and values)
person1 = {"name": "rohit", "age": 30, "city": "delhi"}
person2 = {"name": "aman", "age": 20, "city": "noida"}
person3 = {"name": "ritika", "age": 35, "city": "amritsar"}
print("The details of person 1 is :",person1)
print("The details of person 2 is :",person2)
print("The details of person 3 is :",person3)