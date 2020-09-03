class Note:
	def __init__(self,data):
		self.item =data
		self.ref=None

class LinkedList:
	def __init__(self):
		self.start_node=None

	# reaing through the elements of linked list
	def traverse_list(self):
		if self.start_node is None:
			print("List has no elements")
		else:
			n=self.start_node
			while n is not None:
				print(n.item, " ")
				n=n.ref

	def insert_at_start(self,data):
		new_node=Node(data)
		new_node.ref=self.start_node
		self.start_node=new_node