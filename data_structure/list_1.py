class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


class OrderedList:
    def __init__(self):
        self.head = None

    def search(self,item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return found

    def add(self,item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count


mylist = OrderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))




"""
Linear data structures maintain their data in an ordered fashion.

Stacks are simple data structures that maintain a LIFO, last-in first-out, ordering.

The fundamental operations for a stack are push, pop, and isEmpty.

Queues are simple data structures that maintain a FIFO, first-in first-out, ordering.

The fundamental operations for a queue are enqueue, dequeue, and isEmpty.


Stacks are very useful for designing algorithms to evaluate and translate expressions.

Stacks can provide a reversal characteristic.

Queues can assist in the construction of timing simulations.


Deques are data structures that allow hybrid behavior like that of stacks and queues.

The fundamental operations for a deque are addFront, addRear, removeFront, removeRear, and isEmpty.

Lists are collections of items where each item holds a relative position.

A linked list implementation maintains logical order without requiring physical storage requirements.

Modification to the head of the linked list is a special case. """
