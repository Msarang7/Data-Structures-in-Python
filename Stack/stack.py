class Stack:

	def __init__(self):
		self.stack = []

	def push(self,data):

		self.stack.append(data)
		return data

	def peek(self):

		print("Element at top of the stack : " + str(self.stack[-1]))
		return self.stack[-1]

	def pop(self):

		if len(self.stack) == 0:
			print("no elements to pop")
		else :
			print("element popped")
			return self.stack.pop()

	def printStack(self):
		
		print(self.stack)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.printStack()
stack.peek()
stack.pop()
stack.printStack()