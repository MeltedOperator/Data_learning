
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

class QueueFromStacks:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []
    
    def enqueue(self, item):
        self.stack_in.append(item)
        pass
    
    def dequeue(self):
        # Если stack_out пуст, перекладываем из stack_in
        if len(self.stack_out) == 0:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

    def show(self):
        print(self.stack_in)
        print(self.stack_out)
        
queue = QueueFromStacks()
queue.enqueue(1)
queue.enqueue(3)
queue.enqueue(5)
queue.dequeue()
queue.show()