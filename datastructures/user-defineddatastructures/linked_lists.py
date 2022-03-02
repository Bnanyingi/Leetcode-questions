'''
- A linked list is a sequence of data elements, which are connected together via links.
- Each data element contains a connection to the next data element in form of a pointer.
- Since python does not have linked lists in it's standard library, we implement it using the concept of nodes.
- The first element is called the head and the other elements are reffered to as nodes.
- Each element of a linked list contains data and a link to the next element. The link to the next element is called Next.
- The order of elements in a linked list is not given by their physical placement in memory. Instead, each element points to the next.
- There are three types of linked lists: Singly linked list, Doubly linked list and Circular linked list.
'''

########################################################################################################################################################################
# Singly Linked list
class Node(object):
  def __init__(self, data=None, next_node=None):
    self.data = data
    self.next_node = next_node
class LinkedList(object):
   def __init__(self, head=None):
     self.head = head
   def size(self):
     current = self.head
     count = 0
     while current:
       count += 1
       current = current.next_node
     return count
   def Display(self): 
      temp = self.head 
      while (temp): 
        print (temp.data, " -> ", end = '') 
        temp = temp.next_node
      print("")
   def insert_at_head(self, data):
      new_node = Node(data)
      new_node.next_node = self.head
      self.head = new_node
   def get_next_node (self,node):
      return node.next_node.data
if __name__=='__main__': 
   llist = LinkedList() 
   llist.head = Node(2) 
   s = Node(3) 
   t = Node(4) 
   llist.head.next_node = s;
   s.next_node = t
   llist.Display()
   print(s.data)
   print(llist.size())
   print(llist.get_next_node(s))
   llist.insert_at_head(10)
   llist.Display()


################################################################################################################
# Doubly Linked list

# Initialise the Node
class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None
# Class for doubly Linked List
class doublyLinkedList:
    def __init__(self):
        self.start_node = None
    # Insert Element to Empty list
    def InsertToEmptyList(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("The list is empty")
    # Insert element at the end
    def InsertToEnd(self, data):
        # Check if the list is empty
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        # Iterate till the next reaches NULL
        while n.next is not None:
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.prev = n
    # Delete the elements from the start
    def DeleteAtStart(self):
        if self.start_node is None:
            print("The Linked list is empty, no element to delete")
            return 
        if self.start_node.next is None:
            self.start_node = None
            return
        self.start_node = self.start_node.next
        self.start_prev = None;

    # Delete the elements from the end
    def delete_at_end(self):

        # Check if the List is empty
        if self.start_node is None:
            print("The Linked list is empty, no element to delete")
            return 
        if self.start_node.next is None:
            self.start_node = None
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        n.prev.next = None

    # Traversing and Displaying each element of the list
    def Display(self):
        if self.start_node is None:
            print("The list is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                print("Element is: ", n.item)
                n = n.next
        print("\n")

# Create a new Doubly Linked List
NewDoublyLinkedList = doublyLinkedList()


# Insert the element to empty list
NewDoublyLinkedList.InsertToEmptyList(10)


# Insert the element at the end
NewDoublyLinkedList.InsertToEnd(20)
NewDoublyLinkedList.InsertToEnd(30)
NewDoublyLinkedList.InsertToEnd(40)
NewDoublyLinkedList.InsertToEnd(50)
NewDoublyLinkedList.InsertToEnd(60)


# Display Data
NewDoublyLinkedList.Display()

# Delete elements from start
NewDoublyLinkedList.DeleteAtStart()

# Delete elements from end
NewDoublyLinkedList.DeleteAtStart()






##################################################################################################
# Circular linked list

import os
class _Node:
    '''
    Creates a Node with two fields:
    1. element (accesed using ._element)
    2. link (accesed using ._link)
    '''
    __slots__ = '_element', '_link'

    def __init__(self, element, link):
        '''
        Initialses _element and _link with element and link respectively.
        '''
        self._element = element
        self._link = link


class CicularLL:
    '''
    Consists of member funtions to perform different
    operations on the circular linked list.
    '''

    def __init__(self):
        '''
        Initialises head, tail and size with None, None and 0 respectively.
        '''
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        '''
        Returns length of linked list
        '''
        return self._size

    def isempty(self):
        '''
        Returns True if circular linked list is empty, otherwise False.
        '''
        return self._size == 0

    def addLast(self, e):
        '''
        Adds the passed element at the end of the circular linked list.
        '''
        newest = _Node(e, None)

        if self.isempty():
            self._head = newest
            newest._link = self._head
        else:
            newest._link = self._tail._link
            self._tail._link = newest

        self._tail = newest
        self._size += 1

    def addFirst(self, e):
        '''
        Adds the passed element at the beginning of the circular linked list.
        '''
        newest = _Node(e, None)

        newest._link = self._head
        if self.isempty():
            self._head = newest
            self._tail = newest
        else:
            self._tail._link = newest
            self._head = newest
        self._size += 1

    def addAnywhere(self, e, index):
        '''
        Adds the passed element at the passed index position of the circular linked list.
        '''
        newest = _Node(e, None)
        if index >= self._size:
            print(
                f"Index out of range. It should be between 0 - {self._size - 1}")
        elif self.isempty():
            print("List was empty, item will be added in the End.")
            self.addLast(e)
        elif index == 0:
            self.addFirst(e)
        else:
            p = self._head
            for _ in range(index - 1):
                p = p._link
            newest._link = p._link
            p._link = newest
            print(f"Added Item at index {index}!\n\n")
            self._size += 1

    def removeFirst(self):
        '''
        Removes element from the beginning of the circular linked list.
        Returns the removed element.
        '''
        if self.isempty():
            print("List is Empty")
            return

        e = self._head._element
        self._head = self._head._link
        self._tail._link = self._head
        self._size -= 1
        return e

    def removeLast(self):
        '''
        Removes element from the end of the circular linked list.
        Returns the removed element.
        '''
        if self.isempty():
            print("List is Empty")
            return

        p = self._head  # you can also use self._tail._link as it also points to head node
        if p._link == self._head:
            return self.removeFirst()
        else:
            while p._link._link != self._head:
                p = p._link
            e = p._link._element
            p._link = self._head
            self._tail = p

        self._size -= 1
        return e

    def removeAnywhere(self, index):
        '''
        Removes element from the passed index position of the circular linked list.
        Returns the removed element.
        '''
        if index >= self._size:
            print(
                f"Index out of range. It should be between 0 - {self._size - 1}")
        elif self.isempty():
            print("List is Empty")
            return
        elif index == 0:
            return self.removeFirst()
        elif index == self._size - 1:
            return self.removeLast()
        else:
            p = self._head
            for _ in range(index - 1):
                p = p._link
            e = p._link._element
            p._link = p._link._link
            self._size -= 1
        return e

    def display(self):
        '''
        Utility function to display the circular linked list.
        '''
        if self.isempty() == 0:
            p = self._head
            while True:
                print(p._element, end='-->')
                p = p._link
                if p == self._head:
                    break
            print(f'({p._element} head)')
        else:
            print("Empty")

#########################################################################


def options():
    '''
    Prints Menu for operations
    '''
    options_list = ['Add Last', 'Add First', 'Add Anywhere',
                    'Remove First', 'Remove Last', 'Remove Anywhere',
                    'Display List', 'Exit']

    print("MENU")
    for i, option in enumerate(options_list):
        print(f'{i + 1}. {option}')

    choice = int(input("Enter choice: "))
    return choice


def switch_case(choice):
    '''
    Switch Case for operations
    '''
    os.system('cls')
    if choice == 1:
        elem = int(input("Enter Item: "))
        CL.addLast(elem)
        print("Added Item at Last!\n\n")

    elif choice == 2:
        elem = int(input("Enter Item: "))
        CL.addFirst(elem)
        print("Added Item at First!\n\n")

    elif choice == 3:
        elem = int(input("Enter Item: "))
        index = int(input("Enter Index: "))
        CL.addAnywhere(elem, index)

    elif choice == 4:
        print("Removed Element from First:", CL.removeFirst())

    elif choice == 5:
        print("Removed Element from last:", CL.removeLast())

    elif choice == 6:
        index = int(input("Enter Index: "))
        print(f"Removed Item: {CL.removeAnywhere(index)} !\n\n")

    elif choice == 7:
        print("List: ", end='')
        CL.display()
        print("\n")

    elif choice == 8:
        import sys
        sys.exit()

###############################################################################


if __name__ == '__main__':
    CL = CicularLL()
    while True:
        choice = options()
        switch_case(choice)

 
