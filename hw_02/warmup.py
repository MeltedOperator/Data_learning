
def reverse_string(string: str) -> str:
    s = len(string)
    stack = []
    for i in range(0, s, 1):
        stack.append(string[i])

    string=""
    
    for i in range(0, s, 1):
        string+=stack.pop()
    return string

print(reverse_string("olleh"))