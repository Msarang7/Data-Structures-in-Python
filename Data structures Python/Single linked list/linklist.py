class Node:
	def __init__(self, data = None):
		self.data = data
		self.next = None

# class Node ends here

class linklist :
	def __init__(self):
		self.head = None


	def printList(self):

		temp = self.head
		while temp != None :
			print(temp.data)
			print("->")
			temp = temp.next

	def insertAtStart(self,data):

		newNode = Node(data)
		newNode.next = self.head
		self.head = newNode

	def insertAtEnd(self,data):

		newNode = Node(data)
		
		if self.head == None: # if linklist is empty
			self.head = newNode
			return 

		temp = self.head
		while(temp.next != None): # traversing to last node
			temp = temp.next
		temp.next = newNode

# class linklist ends here


# printing the list 
list = linklist() # creating a list
list.head = Node(1) # adding the first node

e2 = Node(2)
e3 = Node(3)
e4 = Node(4)
e5 = Node(5)

# linking the nodes

list.head.next = e2
e2.next = e3
e3.next = e4
e4.next = e5

# insert at the beginning
list.insertAtStart(6)

# insert at the end
list.insertAtEnd(7)

# printing the list
list.printList()





