# print(1+2))


def is_valid_brackets(expression : str) -> bool:  # type hint
    stack = []
    brackets = {')':'(', '}':'{', ']':'[' }
    for letter in expression:
        if letter in brackets.values():     # 여는 괄호일 때 해당 기호를 스택에 집어넣는다
            stack.append(letter)
        if letter in brackets.keys():       # 닫는 괄호일 때
            if not stack or stack.pop() != brackets[letter]:
                return False

    return not stack

print(is_valid_brackets("([2+3])"))
print(is_valid_brackets("(2+{3*9})"))
print(is_valid_brackets(")1+2())"))
print(is_valid_brackets("(1+2))"))
print(is_valid_brackets("(1+2)"))
print(is_valid_brackets("((1+2)/2)"))