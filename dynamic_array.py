# create an implementation of dynamic array 
class MyArray:

	def __init__(self):
		self.array=[0]*2
		self.current_index=0
		self.capacity=2

	def add(self,item):
		if self.current_index==self.capacity:
			self.resize_array()
		self.array[current_index]=item
		self.current_index+=1

	def remove(self):
		if self.current_index==0:
			raise Exception("Empty List")
		self.current_index-=1 #remove last item

	def resize_array():
		self.capacity+=1
		new_array=[0]*self.capacity
		for i in self.array:
			new_array[i]=self.array[i] # copy element of previous array to new
		return new_array

	def get(self,index):
		if index <0 or index>self.current_index:
			raise Exception("Index not found")
		return self.array[index]

	def size(self):
		return len(self.array)


		
