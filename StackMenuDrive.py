class Stack:
    def __init__(self, n):
        self.tos = -1
        self.data = []
        self.n = n

    def Insert(self):
        if self.tos == self.n - 1:
            print("Element can't be inserted, stack is full!")
            exit()
        else:
            self.tos += 1
            x = input("Enter an element: ")
            self.data.append(x)

    def __str__(self):
        return "Stack: " + ", ".join(self.data)

S = Stack(5)

while True:
    S.Insert()
    print(S)
