def checkParentesis(text):
    stack = []
    brackets = {"]": "[", ")": "(", ">": "<"}
    for letter in text:
        if letter == "(" or letter == "[" or letter == "<":
            stack.append(letter)
        if letter == ")" or letter == "]" or letter == ">":
            if(len(stack) == 0):
                return False
            if stack.pop() != brackets[letter]:
                return False

    if len(stack) > 0:
        return False
    return True


print(checkParentesis("((1+2)) + [<>]"))
