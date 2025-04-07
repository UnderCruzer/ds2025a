# print(1+2))
def is_valid_parentheses(expression : str) -> bool:
    # str 매개변수 데이터 타입 . bool 리턴 타입
    stack = list()
    for letter in expression:
        if letter == "(":
            stack.append(letter)
        if letter == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0
# 여는 괄호가 더 많을 때 False
print(is_valid_parentheses(")1+2())"))
print(is_valid_parentheses("(1+2))"))
print(is_valid_parentheses("(1+2)"))
print(is_valid_parentheses("((1+2)/2)"))