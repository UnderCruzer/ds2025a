class Node:
    def __init__(self, data):
        self.data = data
        self.link = None


class Stack:
    def __init__(self):
        self.items = list()
        self.top = None

    def push(self, item):
        self.items.append(item)

    def push(self, data):
        node = Node(data)
        if self.top is None:
            self.top = node
        else:
            node.link = self.top
            self.top = node  # top update

    def pop(self):
        if self.top is None:
           # raise IndexError("스택이 비어있습니다")
            return "stack is empty"
        popped_node = self.top
        self.top = self.top.link
        popped_node.link = None
        return popped_node.data


    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        return self.items[-1]
        if self.top is None:
            return "Stack is empty!"
        popped_node = self.top
        self.top = self.top.link
        return popped_node.data


s1 = Stack()
s2 = Stack()
s1.push("Data structure")
s1.push("Database")
print(s1.pop())
print(s1.pop())
