# create an implementation of dynamic array 
class DynamicArray:

    def __init__(self):
        self.array = [0] *2
        self.current_index = 0
        self.capacity = 2

    def add(self, item):
        if self.current_index == self.capacity:
            self.resize_array()
        self.array[self.current_index] = item
        self.current_index += 1

    def remove(self):
        if self.current_index == 0:
            raise Exception("Empty List")
        self.current_index -= 1  # remove last item

    def remove_at(self, index):
        if index <= 0 or index > self.current_index:
            raise Exception("Index not found")
        new_array = self.array[self.capacity - 1]
        for i in self.array:
            if i == index: continue  # skip item
            new_array[i] = self.array[i]
        # update array,array size and current index
        self.capacity = len(new_array)
        self.array = new_array
        self.current_index = len(new_array) - 1

    def resize_array(self):
        self.capacity *= 2
        new_array = [0] * self.capacity
        for index, value in enumerate(self.array):
            new_array[value] = self.array[value]  # copy element of previous array to new
        return new_array

    def get(self, index):
        if index < 0 or index > self.current_index:
            raise Exception("Index not found")
        return self.array[index]

    def size(self):
        return len(self.array)

    def index_of(self, item):
        for index, value in enumerate(self.array):
            if value == item:
                return index

    def get_array_data(self):
        sting_array = "["
        for index, value in enumerate(self.array):
            sting_array += str(value)
            if  index != len(self.array) and value != self.array[-1]:
                sting_array += ","
        # sting_array + str(x) + ","
        sting_array += "]"

        return sting_array

    def contains(self, item):
        pass


new_array = DynamicArray()
new_array.add(9)
new_array.add(2)
print("Array \n {} \n".format(new_array.get_array_data()))
new_array.remove()


print("Array \n {} \n".format(new_array.get_array_data()))
print("Size of array \n {} \n".format(new_array.size()))
print("Index of 2 is {} \n".format(new_array.index_of(2)))
