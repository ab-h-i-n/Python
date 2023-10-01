class Stack:
    def __init__(self, n):
        self.tos = -1
        self.data = []
        self.n = n

    def Push(self):
        if self.tos == self.n - 1:
            print("Element can't be inserted, stack is full!")
            return
        else:
            self.tos += 1
            x = input("Enter an element: ")
            self.data.append(x)
        print(self)

    def Pop(self):
        if self.tos == -1:
            print("Stack is empty!")
            return
        else:
            x = self.data.pop()
            print(f"Element {x} has been removed!")
            self.tos -= 1
        print(self)

    def __str__(self):
        if self.tos == -1:
            return "Stack is empty!"
        else:
            return "Stack: " + ", ".join(self.data)


S = Stack(5)

while True:
    print("1. Push")
    print("2. Pop")
    print("0. Exit")
    ch = int(input("Enter your choice : "))

    if ch == 1:
        S.Push()
    elif ch == 2:
        S.Pop()
    else:
        exit()
