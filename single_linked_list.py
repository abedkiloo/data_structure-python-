class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.start_node = None

    # reaing through the elements of linked list
    def traverse_list(self):
        if self.start_node is None:
            print("List has no elements")
        else:
            n = self.start_node
            while n is not None:
                print(n.item, " ")
                n = n.ref

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.ref is not None:
            n = n.ref
        n.ref = new_node

    def insert_after_item(self, x, data):
        n = self.start_node
        print(n.ref)
        while n is not None:
            if n.item == x:
                break
            n = n.ref
        if n is None:
            print("item not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def insert_before_item(self, x, data):
        if self.start_node is None:
            print("List has no item")

        if x == self.start_node.item:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
            return

        n = self.start_node
        print(n.ref)
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref

        if n is None:
            print("item not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def insert_at_index(self, index, data):
        if index == 1:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node

        i = 1
        n = self.start_node
        while i < index - 1 and n is not None:
            n = n.ref
            i += 1
        if n is None:
            print("Index not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def get_count(self):
        if self.start_node is None:
            return 0
        n = self.start_node
        count = 0
        while n is not None:
            count += 1
            n = n.ref
        return count

    def search_item(self, x):
        if self.start_node is None:
            print("List has no elements")
            return
        n = self.start_node
        while n is not None:
            if n.item == x:
                print("Item found")
                return True
            n = n.ref
        print('item not found')

    def make_linked_list(self):
        n = int(input("Enter the size of linked list"))
        while n > 0:
            value = int(input("Enter the value for the node:"))
            self.insert_at_end(value)
            n -= 1


    # deleting linked list
    def delete_at_start(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return 
        self.start_node=self.start_node.ref

    def delete_last_element(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return 
        n=self.start_node
        while n.ref.ref is not None:
            n=n.ref
        n.ref=None

    def delete_element_by_value(self,x):

# deletion of the first element
        if self.start_node.item==x:
            self.start_node=self.start_node.ref
            return
        n=self.start_node
        while n is not None:
            if n.ref.item==x:
                break
            n=n.ref
        if n.ref is None:
            print("item not found in the list")
        else:
            n.ref = n.ref.ref

    def reverse_list(self):
        prev=None
        n=self.start_node
        while n is not None:
            next=n.ref
            n.ref=prev
            prev=n
            n=next
        self.start_node=prev

    def bubble_sort(self):
        end=None
        while end !=self.start_node:
            p=self.start_node
            while p.ref !=end:
                q=p.ref
                if p.item >q.item:
                    p.item, q.item=q.item, p.item
                p=p.ref 
            end =p


new_linked_list = LinkedList()
new_linked_list.insert_at_end(5)
new_linked_list.insert_at_end(10)
new_linked_list.insert_at_end(15)
print(" Nodes after insert at end")
new_linked_list.traverse_list()
print(" Nodes after insert at start")
new_linked_list.insert_at_start(20)
new_linked_list.traverse_list()
new_linked_list.insert_after_item(10, 17)
print(" Nodes after insert at after certain item (after 10) insert 17")
new_linked_list.traverse_list()
new_linked_list.insert_before_item(17, 25)
print(" Nodes before insert at after certain item (after 10) insert 25")
new_linked_list.traverse_list()
new_linked_list.insert_at_index(3, 8)
print(" insert after index")
new_linked_list.insert_at_index(3, 8)
new_linked_list.traverse_list()
print("item count {}".format(new_linked_list.get_count()))
print("Search for item 5 (found)")
new_linked_list.search_item(5)
print("Search for item 59 (not found)")
new_linked_list.search_item(59)
new_linked_list2=LinkedList()
# new_linked_list2.make_linked_list()
# print(" new inserted linked list")
# new_linked_list2.traverse_list()

print("Delete the last element")
new_linked_list.delete_last_element()
new_linked_list.traverse_list()


print("Delete the start element")
new_linked_list.delete_at_start()
new_linked_list.traverse_list()


print("Reverseed List")
new_linked_list.reverse_list()
new_linked_list.traverse_list()
print("Bubble sorted List")

new_linked_list.bubble_sort()
new_linked_list.traverse_list()


