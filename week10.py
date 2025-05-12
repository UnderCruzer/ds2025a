class TreeNode:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.data, end='->')

def search():
    find_number = int(input("찾는 수는? "))
    current = root
    while True:
      if find_number == current.data:
          print(f"{find_number}을(를) 찾았습니다")
          break
      elif find_number < current.data:
          if current.left is None:
              print(f"{find_number}이(가) 존재하지 않습니다")
              break
          current = current.left
      else:
          if current.right is None:
              print(f"{find_number}이(가) 존재하지 않습니다")
              break
          current = current.right


def insert(root, value):
    node = TreeNode()
    node.data = value

    if root is None:  # 첫 번째 노드 처리
        return node

    current = root
    while True:
        if value < current.data:
            if current.left is None:
                current.left = node
                break
            current = current.left  # move
        else:
            if current.right is None:
                current.right = node
                break
            current = current.right  # move
    return root

if __name__ == "__main__":
    numbers = [10, 15, 8, 3, 9, 100, 7, 13]
    root = None

    # 2번째 원소 부터 마지막 원소까지
    for number in numbers:
        root = insert(root, number)

    print("BST 구성 완료")

    post_order(root)
    print()
    search()



#   find_number = int(input())
#   current = root
#   while True:
#       if find_number == current.data:
#           print(f"{find_number}을(를) 찾았습니다")
#           break
#       elif find_number < current.data:
#           if current.left is None:
#               print(f"{find_number}이(가) 존재하지 않습니다")
#               break
#           current = current.left
#       else:
#           if current.right is None:
#               print(f"{find_number}이(가) 존재하지 않습니다")
#               break
#           current = current.right