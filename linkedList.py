
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None

    def insert(self,data):
        newNode = Node(data)

        if not self.start:
            self.start = newNode
        else:
            temp = self.start

            while temp.next:
                temp = temp.next
            temp.next = newNode

    def display(self):
        
        temp = self.start

        while temp:
            print(temp.data, end="\t")
            temp = temp.next


List = LinkedList()

while True:

    num = input("Enter number : ")
    List.insert(num)
    print("The list is ",end = "\t")
    List.display()

    ch = input("\n\nEnter 'y' to continue : ")

    if ch != 'y':
        break


