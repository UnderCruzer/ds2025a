from wsgiref.util import application_uri


class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

# a = Node("ABC")
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head             # current 지역변수 생성, self.head의 주소를 가짐
        while current.link:
            current = current.link
        current.link = Node(data)
    def __str__(self):
        #return "Linked list"
        current = self.head
        result = ""
        while current is not None:
            #print(current.data)
            result = result + str(current.data) + "->"
            current = current.link
        return result + "end"
ll = LinkedList() # 링크드리스트 객체 생성, 헤드의 none값 만듬, self.head가 false이지만 if문에의해 true,
ll.append(8)
ll.append(10)
ll.append(-9)
print(ll)