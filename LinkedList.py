class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove(self, data):
        if not self.is_empty():
            if self.head.data == data:
                self.head = self.head.next
            else:
                current = self.head
                while current.next:
                    if current.next.data == data:
                        current.next = current.next.next
                        break
                    current = current.next

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

# 示例用法
my_list = LinkedList()

print(my_list.is_empty())  # 输出: True

my_list.add(10)
my_list.add(20)
my_list.add(30)

print(my_list.display())  # 输出: [10, 20, 30]

print(my_list.search(20))  # 输出: True
print(my_list.search(40))  # 输出: False

my_list.remove(20)

print(my_list.display())  # 输出: [10, 30]
