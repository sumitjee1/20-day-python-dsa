#Code to implement Queue using list
queue = []

def enqueue(item):
    queue.append(item)

def dequeue():
    if not is_empty():
        return queue.pop(0)  # Removes and returns the first element
    else:
        return "Queue is empty!"

def peek():
    if not is_empty():
        return queue[0]  
    else:
        return "Queue is empty!"

def is_empty():
    return len(queue) == 0

def size():
    return len(queue)

def display():
    if is_empty():
        return "Queue is empty!"
    return queue

enqueue(10)  # Add 10
enqueue(20)  # Add 20
enqueue(30)  # Add 30

print("Queue after enqueue:", display()) 
dequeued_element = dequeue() 
print("Dequeued element:", dequeued_element)
print("Queue after dequeue:", display())  
front_element = peek()  
print("Front element:", front_element) 
print("Is the queue empty?", is_empty())  
print("Size of the queue:", size()) 
