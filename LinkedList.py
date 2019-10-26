import PyQt5

class LinkedList:

    def __init__(self):
        self.head = None

    def add(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            current = self.head
            while current.next != None:
                current = current.next

            current.next = Node(value)

    def printValues(self):
        current = self.head
        while current.next != None:
            print(current.value)
            current = current.next
        print(current.value)



class Node:

    def __init__(self, value):
        self.value = value
        self.next = None