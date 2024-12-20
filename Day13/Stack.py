#Code to create Stack using list and to perform various stack operations
class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        
        return len(self.stack) == 0

    def push(self, item):
       
        self.stack.append(item)

    def pop(self):
        
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty!"

    def peek(self):
       
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty!"

    def size(self):
        
        return len(self.stack)

    def display(self):
        
        if self.is_empty():
            return "Stack is empty!"
        return self.stack

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print("Stack:", stack.display())
print("Top element:", stack.peek())
print("Popped element:", stack.pop())
print("Stack after pop:", stack.display())
print("Is stack empty?", stack.is_empty())
print("Size of stack:", stack.size())
