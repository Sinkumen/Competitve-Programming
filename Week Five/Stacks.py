def reverseString(word):
    stack = []
    for letter in word:
        stack.append(letter)
    reversed = [""]
    while(len(stack) > 0):
        reversed[0] += stack.pop()
    print(reversed[0])
    return reversed[0]


reverseString(None)
