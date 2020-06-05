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


	# inserting between two nodes in the link list

	def atPosition(self,pos,data): # pos ranges from 0 to length to list

		
		temp = self.head
		len = 0

		while(temp!=None):
			temp = temp.next
			len = len+1

		if pos > len+1 : 
			print("not enough nodes in the list")
			return


		if pos == 0:
			insertAtStart(data)
			return

		else :

			temp = self.head

			for i in range(pos-1):
				temp = temp.next

			newNode = Node(data)
			newNode.next = temp.next
			temp.next = newNode
			print("Node inserted at position " + str(pos))

	def removeNode(self, data) :

		temp = self.head

		if temp == None : # no nodes in the list
			print("list is empty hence, node not found")
			return

		# check for head node

		if self.head.data == data :
			self.head = self.head.next
			print("node deleted")
			return

		else :

			while (temp.next != None):
				if temp.next.data == data :
					temp.next = temp.next.next
					print("node deleted")
					return
				temp = temp.next

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

# insert at position 
pos = 2
data = 11
list.atPosition(pos,data)

# remove node
data = 7
list.removeNode(data)

# printing the list
list.printList()
