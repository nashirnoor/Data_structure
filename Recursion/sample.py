# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.prev = None
#         self.next = None

# def reverse_string(input_string):
#     # Create an empty doubly linked list
#     dummy = Node(None)
#     current = dummy
    
#     # Create nodes for each character and link them together
#     for char in input_string:
#         new_node = Node(char)
#         current.next = new_node
#         new_node.prev = current
#         current = new_node
    
#     # Traverse the doubly linked list to reverse the string
#     reversed_string = ''
#     current = current.prev  # Skip the dummy node
#     while current:
#         reversed_string += current.data
#         current = current.prev
    
#     return reversed_string

# # Test the function
# input_string = "Hello, World!"
# reversed_str = reverse_string(input_string)
# print("Original string:", input_string)
# print("Reversed string:", reversed_str)


min_value = 2 
result = min_value * 2  
print("Result of division:", result)  
