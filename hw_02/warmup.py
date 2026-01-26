
def reverse_string(string: str) -> str:

    """эта функция переворачивает строку наоборот без использования
    s[::-1], reversed()"""

    s = len(string)

    stack = []

    for i in range(0, s, 1):
        stack.append(string[i])

    string=""
    
    for i in range(0, s, 1):
        string+=stack.pop()

    return string


class QueueFromStacks:

    def __init__(self):

        """инициализируем два стека - stack_in и stack_out"""

        self.stack_in = []
        self.stack_out = []

    def enqueue(self, item):

        """добавляем элементы в stack_in"""
        
        self.stack_in.append(item)
        

    def dequeue(self):

        """в этой функции мы перекладываем элементы из stack_in
        в stack_out при условии если stack_out пустой"""

        # Если stack_out пуст, перекладываем из stack_in

        if len(self.stack_out) == 0:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

    def show(self):
        return self.stack_in, self.stack_out
    

queue = QueueFromStacks()

queue.enqueue(1)
queue.enqueue(3)
queue.enqueue(5)
queue.dequeue()
print(queue.show())

print(reverse_string("olleh"))