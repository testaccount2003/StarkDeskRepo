'''inpt = int(input("Enter the number upto which you want to generate a pattern: "))
for i in range(1,inpt+1):
    print()
    for j in range(1, i+1):
        
        print(i, end = "")
''' 
'''l = ['Tony', 'Stark', 'is', 'a', 'Billionaire']
for item in l:
    print(item, end = ' ')
'''
'''#Q.1.searching an element in the tuple and print the position number
t = (15,23,27,45,36)
print('Elements in the ready-made tuple: ')
print(t)
print()
x = int(input("Enter an element to be found in the current tuple and display its position: "))
n = len(t)
print()
flag = 0
for i in range(0,n,1):
    if t[i] == x:
        flag = 1
        break
    else:
        flag=0
if flag == 1:
    print("The element is found at position", i + 1)
else:
    print("The element is not found")
'''
'''# Creation of an Array

import array as arr 

a = arr.array('i',[1,2,3])
print("The Array before insertion is: ", end = " ")
for i in range(3):
    print([a[i]],end = " ")

# Inserting using insert()

a.insert(24,4)
print()
print("The Array after insertion is: ", end = " ")
for i in a:
    print([i], end = " ")
'''
# Python program for linked list implementation of stack

# Class to represent a node


# class StackNode:

# 	# Constructor to initialize a node
# 	def _init_(self, data):
# 		self.data = data
# 		self.next = None


# class Stack:

# 	# Constructor to initialize the root of linked list
# 	def _init_(self):
# 		self.root = None

# 	def isEmpty(self):
# 		return True if self.root is None else False

# 	def push(self, data):
# 		newNode = StackNode(data)
# 		newNode.next = self.root
# 		self.root = newNode
# 		print (data,"pushed to stack")

# 	def pop(self):
# 		if (self.isEmpty()):
# 			return float("-inf")
# 		temp = self.root
# 		self.root = self.root.next
# 		popped = temp.data
# 		return popped

# 	def peek(self):
# 		if self.isEmpty():
# 			return float("-inf")
# 		return self.root.data


# # Driver code
# stack = Stack()
# stack.push(10)
# stack.push(20)
# stack.push(30)

# print (stack.pop(),"Popped from stack")
# print ("Top element is: ",stack.peek())




""" 
	Write a Program to count the frequencies of all the elements of a list and
    Also print the following:
    i) List of Unique elements.
   ii) List of Duplicate elements.
   
"""


'''
l = [12,5,4,5,8,9,12,4,8,52,45,8,20,52,45,89,21,16]
Unique = []
Duplicate = []
for i in range(len(l)):
	if l[i] in Unique:
		continue
	else:
		count = l.count(l[i])
		if count > 1:
			Duplicate.append(l[i])
			Duplicate.sort()
		else:
			pass
		Unique.append(l[i])
		Unique.sort()
		print(f"The number {l[i]} has {count} occurance(s) in the list")
print(f"The Unique Element list is {Unique}")
print(f"The Duplicate Element list is {Duplicate}")
'''


l = [45,85,36,21,57,95,24,37,52,89,27,15,51]
gl = sort(l)
print(gl)

















