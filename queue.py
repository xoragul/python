# from collections import deque

# queue = deque()

# queue.append(10)
# queue.append(20)
# queue.append(30)
# print("Queue:", list(queue))  




# from collections import deque

# queue = deque()

# queue.append(10)
# queue.append(20)
# queue.append(30)

# front_element = queue.popleft()
# print("Dequeued element:", front_element)  


from  collections import deque

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)

front_element=queue.popleft()
print("deque elements:", front_element)




from collections import deque

queue = deque()

queue.append(10)
queue.append(20)
queue.append(30)


front_element = queue[1]
print("Front element:", front_element)  


from collections import deque

queue = deque()

queue.append(10)
queue.append(20)
queue.append(30)

print("Is queue empty?", len(queue) == 0)
