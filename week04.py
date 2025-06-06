
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

    #def is_find(self, target):
    def remove(self, target):
        current = self.head
        if self.head.data == target:            #타겟의 값과 노드의 값이 일치
            self.head = self.head.link
            current.link = None
            return

        previous = None
        while current:
            if target == current.data:
                previous.link = current.link
                current.link = None
            previous = current
            current = current.link

    def search(self, target):
        current = self.head
        while current:
            if target == current.data:
                return f"{target}을 찾았습니다"
            else:
                current = current.link
        return f"{target}은 링크드리스트 안에 존재하지 않습니다"

    def __str__(self):
        #return "Linked list"
        current = self.head
        result = ""
        while current is not None:
            #print(current.data)
            #result = result + str(current.data) + "->"
            result = result + f"{current.data} ->"
            current = current.link
        return result + "end"


ll = LinkedList() # 링크드리스트 객체 생성, 헤드의 none값 만듬, self.head가 false이지만 if문에의해 true,
ll.append(8)
ll.append(10)
ll.append(-9)
print(ll)
print(ll.search(99))
print(ll.search(-9))
ll.remove(-9)
print(ll)