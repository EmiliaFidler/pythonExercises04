# -- exercises 04 --

# singly linked list
# node class of the singly linked list
class SLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None  # pointer to the next node

    def __str__(self):
        return str(self.data)


# Singly linked list class
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, new_data):
        # Create the new node the pointer is set to None through the constructor of the SLLNode class
        new_node = SLLNode(new_data)
        if self.head is None:  # if the list is empty, the new node is the head
            self.head = new_node
        else:  # if it is not empty, we need to find the last node and append the new node
            current = self.head
            while current.next is not None:
                current = current.next
            # set the pointer of the last node to the new node
            current.next = new_node
        self.size += 1  # increase the size of the list

    def get_size(self):
        return self.size

    # string representation of the linked list
    def __str__(self):
        return str([node for node in self])

    # iteration function without this function we can not iterate over the list
    def __iter__(self):
        current = self.head
        while current:
            value = current.data
            current = current.next
            yield value

    """
    Exercise part 1,2,3,4

    Implement the given methods below according to the requirements in the exercise sheet.
    Make sure to return the correct values.
    """

    def insert_node(self, prev_node_data, new_node_data):
        if prev_node_data not in self:
            return False

        new_node = SLLNode(new_node_data)
        prev_node = self.get_node(prev_node_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        self.size += 1
        return True

    def get_node(self, data)
        # searches the list for the node with the given data
        # returns the node or None if it's not in the list
        cur_node = self.head
        while cur_node is not None and cur_node.data != data:
            cur_node = cur_node.next
        return cur_node

    def get_prev_node(self, data)
        # searches the list for the previous node of the node with the given data
        # returns the previous node or None if it's not in the list
        cur_node = self.head
        prev_node = None
        while cur_node is not None and cur_node.data != data:
            prev_node = cur_node
            cur_node = cur_node.next
        if cur_node is None:
            return None
        return prev_node

    def clear(self):
        self.head = None  # because of automatic garbage collection in Python
        self.size = 0

    def get_data(self, data):
        node = self.get_node(data)
        if node is None:
            return False
        return data

    def delete_node(self, data):
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return

        prev_node = self.get_prev_node(data)
        if prev_node is None:
            return

        tbd_node = prev_node.next  # tbd_node = to be deleted
        prev_node.next = tbd_node.next
        self.size -= 1


my_list = SinglyLinkedList()
print(my_list)
my_list.append(1)
my_list.append(2)
print(my_list.size)
print((my_list))
my_list.insert_node(1, 0)
print((my_list))
print(my_list.get_data(6))
print(my_list.get_prev_node(0))
my_list.delete_node(0)
print(my_list)
my_list.clear()
print(my_list)
print()


# exercise 5:

class DLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.data)


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, new_data):
        new_node = DLLNode(new_data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current
        self.tail = new_node
        self.size += 1

    def get_size(self):
        return self.size

    def __str__(self):
        return str([node for node in self])

    def __iter__(self):
        current = self.head
        while current:
            value = current.data
            current = current.next
            yield value

    def clear(self):
        self.head = None  # because of automatic garbage collection in Python
        self.size = 0

    def get_node(self, data):
        # searches the list for the node with the given data
        # returns the node or None if it's not in the list
        cur_node = self.head
        while cur_node is not None and cur_node.data != data:
            cur_node = cur_node.next
        return cur_node

    def insert_node(self, prev_node_data, new_node_data):
        if prev_node_data not in self:
            return False

        new_node = DLLNode(new_node_data)
        prev_node = self.get_node(prev_node_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next is not None:
            new_node.next.prev = new_node
        else:
            self.tail = new_node
        self.size += 1
        return True

    def delete_node(self, data):  # needs to be changed
        if self.head.data == data:
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1
            return

        if self.tail.data == data:
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1
            return

        tbd_node = self.get_node(data)
        tbd_node.prev.next = tbd_node.next
        tbd_node.next.prev = tbd_node.prev
        self.size -= 1


my_list = DoublyLinkedList()
print(my_list)
my_list.append(1)
my_list.append(2)
print(my_list.size)
print((my_list))
my_list.insert_node(1, 0)
print((my_list))
my_list.delete_node(0)
print(my_list)
my_list.clear()
print(my_list)


# exercise 6:

class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def top(self):
        if self.stack:  # list is here interpreted as a bool - empty list is falsy
            return self.stack[-1]  # index from the end
        else:
            return None

    def size(self):
        return len(self.stack)


print()
stack = MyStack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()
print(stack.top())
print(stack.stack)
print(stack)


# exercise 7:

class MyQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):  # aka push
        self.queue.append(element)

    def dequeue(self):  # aka pop
        return self.queue.pop(0)

    def show_left(self):
        return self.queue[-1]

    def show_right(self):
        return self.queue[0]

print()
queue = MyQueue()
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
print(queue.queue)
queue.dequeue()
queue.dequeue()
print(queue.queue)
print(queue.show_right())
print(queue.show_left())