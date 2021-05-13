'''
Cracking the coding interview
Chapter 2 - Linked List pg 94
Linked List - Partition
----------------------------------------
Question: Write code to partition a linked list around a value of x. Such that all nodes less than x come before all nodes greater than or equal to x
Example: 1 -> 2 -> 3 -> 5 -> 8 -> 5 -> 10 - None
input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 (x = 5)
output: 3 -> 1 -> 2      ->     10 -> 5 -> 5 -> 8
Constraits or Questions you need to ask:
- Try brute force method. 
- Travese the linked list and ask if the given node is < or >= x and if < append to front of new list and if >= append to end of list
Solution notes:
- append to front of list
- append to end of list
- Partition function that takes in a list and x
'''
#Node class
class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

#Wrapper class
class linked_list:
    def __init__(self):
        self.head = node()

    #Print the linked list
    def display(self):
        elements = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            elements.append(cur.data)
        print(elements)

    #Print the data in the linked list
    def print(self):
        cur = self.head
        while cur:
            if(cur.data == None):
                cur = cur.next
            print(cur.data)
            cur = cur.next

    #Add a node to the end of a linked list
    def append(self,data):
        new_node = node(data)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node

    #Add a node to the end of a linked list
    def appendtoEnd(self,data):
        new_node = node(data)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node

    #Add a node to the front of a linked list
    def appendtoFront(self,data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node

    #Partition function to organize the linked list
    def partitionList(self, partition):
        #Initialize new linked list
        newLinkedList = linked_list()

        cur = self.head
        while cur.next != None:
            cur = cur.next
            #If cur.data is less than partition, append to front
            if(cur.data < partition):
                newLinkedList.appendtoFront(cur.data)
            elif(cur.data >= partition):
                newLinkedList.appendtoEnd(cur.data)
        newLinkedList.print()





myList = linked_list()
#While list is empty
#myList.display()

#Adding elements to linked list
myList.append(3)
myList.append(5)
myList.append(8)
myList.append(5)
myList.append(10)
myList.append(2)
myList.append(1)

#Display current linked list
myList.partitionList(5)