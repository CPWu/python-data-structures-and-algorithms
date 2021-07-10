# # Hello World Example - Output
# print("Hello World")

# # Arithmetic
# print(20 * 10)

# # String Concat
# print("Today is June " + str(4) + "th")

# # Elegant way of Concat
# print(f"Today is June {4}th")

# # Variables
# yearlySalary = 90000
# currency = "CAD"
# print(f"It would be great if Canada's average salary was: {yearlySalary} {currency}")

# # Functions
# def calculateSalary(hourly, hours):
#     castedHours = int(hours)
#     castedHourly = int(hourly)
#     print(f"Your annual salary is: {castedHours * castedHourly * 52}")

# hourly = input("Your hourly wage: \n")
# hours = input("How many hours do you work per week: \n")
# calculateSalary(hourly, hours)

# # Conditionals if/else
# inputNumber = input("How old are you? \n")
# inputNumber = int(inputNumber)

# if inputNumber > 0 and inputNumber < 18:
#     print("You are a kid!")
# elif inputNumber < 30:
#     print("The enjoyable adulthood years.")
# else:
#     print("Grinding for retirement, life is over.")

# # Calculte Function
# calculation_to_units = 24
# name_of_unit= "hours"
# 10,8
# def days_to_units(num_of_days):
#     if num_of_days > 0:
#         return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"

# # Validation Function
# def validate_input():
#     try:
#         user_input_number = int(num_of_days)
#         if user_input_number > 0:
#             calculated_value = days_to_units(user_input_number)
#             print(calculated_value)
#         elif user_input_number == 0:
#             print("You entered a 0, please enter a valid positive number.")
#         else:
#             print("You entered a negative number, please enter a positive number.")
#     except ValueError:
#         print("Invalid Input")

# # # Loops - While Loop
# # userInput = ""
# # while userInput != 'exit':
# #     userInput = input("Type anything or exit to quit.\n")

# # Lists
# user_input = ""
# while user_input != "exit":
#         user_input = input("Hello, enter number of days, and I will convert it to hours. \n")
#         list_of_days = user_input.split(",")
#         print(list_of_days)
#         print(set(list_of_days))
#         print(type(list_of_days))
#         print(type(set(list_of_days)))
#         for num_of_days in set(list_of_days):
#             validate_input()

# Doubly Linked List

# class Node(object):
#     def __init__(self, data):
#         self.data = data    
#         self.next = None
#         self.prev = None

# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     # O (1) time | O(1) space
#     def append(self, data):
#         # If there is an empty list
#         if self.head is None:
#             new_node = Node(data)
#             # Because its doubly linked new_node.prev is none 
#             new_node.prev = None
#             self.head = new_node
#         # If there is at least one node in doubly linked list
#         else:
#             # Create a node with data input
#             new_node = Node(data)
#             current_node = self.head
#             # If current node is not pointing none we know we have reached the end of the doubly linked list
#             while current_node.next:
#                 current_node = current_node.next
#             # Set the current_nodes next pointer to the new node and set the new node previous to the current node
#             current_node.next = new_node
#             new_node.prev = current_node

#     # O (1) time | O(1) space
#     def prepend(self, data):
#         # Similar to an append its possible that the doubly linked list is empty so just add the node to the doubly linked list
#         if self.head is None:
#             new_node = Node(data)
#             self.head = new_node
#             new_node.prev is None
#         # In the case where there is at least one node in the doubly linked list
#         else:
#             new_node = Node(data)
#             self.head.prev = new_node
#             new_node.next = self.head
#             self.head = new_node
#             new_node.prev = None

#     # O (n) time | O(1) space
#     def insertBefore(self, key, data):
#         # Case #1 - Doubly linked list with only one Node
#         current_node = self.head
#         while current_node:
#             # first node will have .prev point to None
#             if current_node.prev is None and current_node.data == key:
#                 self.prepend(data)
#                 return
#             # Case #2 - More than one node in the doubly linked list
#             elif current_node.data == key:
#                 new_node = Node(data)
#                 prev = current_node.prev
#                 prev.next = new_node
#                 current_node.prev = new_node
#                 new_node.next = current_node
#                 new_node.prev = prev
#             current_node = current_node.next


#     # O (n) time | O(1) space
#     def insertAfter(self, key, data):
#         # Case #1 - Doubly Linked List with only one Node
#         current_node = self.head
#         while current_node:
#             # first node that will have .next point to None
#             if current_node.next is None and current_node.data == key:
#                 self.append(data)
#                 return
#                 # Case #2 - More than one node insertion after
#             elif current_node.data == key:
#                 new_node = Node(data)
#                 next = current_node.next
#                 current_node.next = new_node
#                 new_node.prev = current_node
#                 new_node.next = next
#             current_node = current_node.next

#     # O (n) time | O(1) space
#     def deleteNode(self, key):
#         # Case 4: If the .next is none which would mean its the last node
#         current_node = self.head
#         while current_node:
#             if current_node.data == key and current_node == self.head:
#                 # Case 1: If its the head node and only one node in list
#                 if current_node.next is None:
#                     current_node = None
#                     self.head = None
#                     return
#                 # Case 2: If its the head node and there are more than one nodes in the list
#                 else: 
#                     next = current_node.next
#                     current_node.next = None
#                     next.prev = None
#                     current_node = None
#                     self.head = next
#                     return
#             elif current_node.data == key:
#                 # Case 3: If the .next is not None meaning its not the last node
#                 if current_node.next:
#                     next = current_node.next
#                     prev = current_node.prev
#                     prev.next = next
#                     next.prev = prev
#                     current_node.next = None
#                     current_node.prev = None
#                     current_node = None
#                     return
#                 # Case 4: If the .next is none which would mean its the last node
#                 else:
#                     prev = current_node.prev
#                     prev.next = None
#                     current_node.prev = None
#                     current_node = None
#                     return
#             current_node = current_node.next

#     # O (n) time | O(1) space
#     def deleteNodeAt(self, node):
#         # Case 4: If the .next is none which would mean its the last node
#         current_node = self.head
#         while current_node:
#             if current_node.data == node and current_node == self.head:
#                 # Case 1: If its the head node and only one node in list
#                 if current_node.next is None:
#                     current_node = None
#                     self.head = None
#                     return
#                 # Case 2: If its the head node and there are more than one nodes in the list
#                 else: 
#                     next = current_node.next
#                     current_node.next = None
#                     next.prev = None
#                     current_node = None
#                     self.head = next
#                     return
#             elif current_node == node:
#                 # Case 3: If the .next is not None meaning its not the last node
#                 if current_node.next:
#                     next = current_node.next
#                     prev = current_node.prev
#                     prev.next = next
#                     next.prev = prev
#                     current_node.next = None
#                     current_node.prev = None
#                     current_node = None
#                     return
#                 # Case 4: If the .next is none which would mean its the last node
#                 else:
#                     prev = current_node.prev
#                     prev.next = None
#                     current_node.prev = None
#                     current_node = None
#                     return
#             current_node = current_node.next

#     def reverse(self):
#         temp = None
#         current_node = self.head
#         # While not null
#         while current_node:
#             temp = current_node.prev # A
#             current_node.prev = current_node.next #
#             current_node.next = temp
#             current_node = current_node.prev
#         if temp:
#             self.head = temp.prev

#     def removeDuplicates(self):
#         current_node = self.head
#         nodes_seen = dict()

#         while current_node:
#             if current_node.data not in nodes_seen:
#                 nodes_seen[current_node.data] = 1
#                 current_node = current_node.next
#             else:
#                 next = current_node.next
#                 self.deleteNodeAt(current_node)
#                 current_node = next  

#     def pairs_with_sum(self, sum_val):
#         pairs = list()
#         p = self.head 
#         q = None 
#         while p:
#             q = p.next
#             while q:
#                 if p.data + q.data == sum_val:
#                     pairs.append("(" + str(p.data) + "," + str(q.data) + ")")
#                 q = q.next
#             p = p.next
#         return pairs

#     def print(self):
#         # Loop through the doubly linked list to print
#         current_node = self.head
#         while current_node:
#             print(current_node.data)
#             current_node = current_node.next

# # Instantiate a Doubly Linked List
# doublyLinkedList = DoublyLinkedList()

# # Append a few nodes to List
# doublyLinkedList.append(1)
# doublyLinkedList.append(2)
# doublyLinkedList.append(3)
# doublyLinkedList.append(3)
# doublyLinkedList.append(3)
# doublyLinkedList.append(3)
# # Prepend to the List
# #doublyLinkedList.prepend(0)

# # Insert a node after a node
# #doublyLinkedList.insertAfter(2, 15)

# # Insert a node before a node
# #doublyLinkedList.insertBefore(1, 15)

# # Deleting a Node
# # doublyLinkedList.deleteNode(1)
# # doublyLinkedList.deleteNode(15)

# # Reverse a Linked List
# #doublyLinkedList.reverse()

# # Removes Duplicates
# # doublyLinkedList.removeDuplicates()

# # Pairs with Sum
# print(doublyLinkedList.pairs_with_sum(5))

# doublyLinkedList.print()

# Another Version of the Doubly Linked List - Practice makes perfect.

# # This is an input class. Do not edit.
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.prev = None
#         self.next = None


# # Feel free to add new properties and methods to the class.
# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def setHead(self, node):
# 		if self.head is None:
# 			self.head = node
# 			self.tail = node
# 			return
# 		self.insertBefore(self.head, node)

#     def setTail(self, node):
# 	    if self.tail is None:
# 		    self.setHead(node)
# 		    return
# 		self.insertAfter(self.tail, node)

#     def insertBefore(self, node, nodeToInsert):
#         # If the node to insert is equivalent to the head/tail of the D.L.L because (only one node)
#         if nodeToInsert == self.head and nodeToInsert == self.tail:
#             return
#         self.remove(nodeToInsert)
#         nodeToInsert.prev = node.prev
#         nodeToInsert.next = node
#         if node.prev is None:
#             self.head = nodeToInsert
#         else:
#             node.prev.next = nodeToInsert
#         node.prev = nodeToInsert

#     def insertAfter(self, node, nodeToInsert):
#         if nodeToInsert == self.head and nodeToInsert == self.tail:
#             return
#         self.remove(nodeToInsert)
#         nodeToInsert.prev = node
#         nodeToInsert.next = node.next
#         if node.next is None:
#             self.tail = nodeToInsert
#         else:
#             node.next.prev = nodeToInsert
#         node.next = nodeToInsert

#     def insertAtPosition(self, position, nodeToInsert):
#         if position == 1:
#             self.setHead(nodeToInsert)
#             return
#         node = self.head
#         currentPosition = 1
#         while node is not None and currentPosition != position:
#             node = node.next
#             currentPosition += 1
#         if node is not None:
#             self.insertBefore(node, nodeToInsert)
#         else:
#             self.setTail(nodeToInsert)

#     def removeNodesWithValue(self, value):
#         node = self.head
#         while node is not None:
#             nodeToRemove = node
#             node = node.next
#             if nodeToRemove.value == value:
#                 self.remove(nodeToRemove)

#     def remove(self, node):
#         if node == self.head:
#             self.head = self.head.next
#         if node == self.tail:
#             self.tail = self.tail.prev
#         self.removeNodeBindings(node)

#     def containsNodeWithValue(self, value):
#         node = self.head
#         while node is not None and node.value != value:
#             node = node.next
#         return node is not None
	
#     def removeNodeBindings(self, node):
#         if node.prev is not None:
#             node.prev.next = node.next
#         if node.next is not None:
#             node.next.prev = node.prev
#         node.prev = None
#         node.next = None