class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        else:
            node.next = self.head
            self.head = node

    def print(self):
        if self.head is None:
            print('prazna lista')
        else:
            llstr = ""
            node = self.head
            while node:
                llstr += str(node.data) + '--->'
                node = node.next
        print(llstr)


ll = LinkedList()
ll.insert_at_beginning(2)
ll.insert_at_beginning(3)
ll.insert_at_beginning(4)
ll.print()
