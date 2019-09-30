from typing import *

class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. 
        If the index is invalid, return -1.
        """
        # possible indices, when size == 1: 0
        # possible indices, when size == 2: 0, 1
        # possible indices, when size == 3: 0, 1, 2
        if 0 <= index and index < self.size:
            i = 0
            cur = self.head

            while i < index:
                cur = cur.next
                i += 1

            return cur.val

        return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. 
        After the insertion, the new node will be the first node of the linked list.
        """
        new_node = ListNode(val)

        if self.size == 0:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.size += 1
        
    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new_node = ListNode(val)

        if self.size == 0:
            self.head = new_node
        else:
            cur = self.head

            while cur.next != None:
                cur = cur.next
            
            cur.next = new_node
            new_node.prev = cur

        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. 
        If index equals to the length of linked list, the node will be appended to the end of linked list. 
        If index is greater than the length, the node will not be inserted.
        """
        if 0 <= index and index < self.size:
            if index == 0:
                self.addAtHead(val)
            else:
                i = 0
                cur = self.head
                new_node = ListNode(val)

                while i < index:
                    cur = cur.next
                    i += 1

                cur.prev.next = new_node
                new_node.prev = cur.prev
                new_node.next = cur
                cur.prev = new_node

                self.size += 1
        elif index == self.size:
            self.addAtTail(val)
        
    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if 0 <= index and index < self.size:
            if index == 0:
                self.head = self.head.next

                if self.size != 1:
                    self.head.prev.next = None
                    self.head.prev = None
            elif index == self.size-1:
                i = 0
                cur = self.head

                while i < index:
                    cur = cur.next
                    i += 1
                
                cur.prev.next = None
                cur.prev = None
            else:
                i = 0
                cur = self.head

                while i < index:
                    cur = cur.next
                    i += 1
                
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
            
            self.size -= 1

    def print(self):
        cur = self.head

        print("list --->", end=" ")

        while cur != None:
            print(cur.val, end=" ")
            cur = cur.next
        
        print('size', self.size, end=" ")
        print()

# myList = MyLinkedList()
# myList.addAtHead(1)
# myList.print()
# myList.addAtTail(3)
# myList.print()
# print(myList.get(0))
# print(myList.get(1))
# print(myList.get(-99))
# print(myList.get(2))
# print(myList.get(99))
# myList.addAtIndex(1, 2)
# myList.print()
# print(myList.get(0))
# print(myList.get(1))
# print(myList.get(2))
# myList.addAtIndex(3, 4)
# myList.print()
# myList.addAtIndex(99, 4)
# myList.print()
# myList.addAtIndex(-99, 4)
# myList.print()
# myList.addAtIndex(0, 7)
# myList.print()
# myList.addAtIndex(1, 8)
# myList.print()
# myList.deleteAtIndex(0)
# myList.print()
# myList.deleteAtIndex(1)
# myList.print()
# myList.deleteAtIndex(3)
# myList.print()

# myList = MyLinkedList()
# myList.addAtHead(5)
# myList.print()
# myList.addAtHead(2)
# myList.print()
# myList.deleteAtIndex(1)
# myList.print()
# myList.addAtIndex(1, 9)
# myList.print()
# myList.addAtHead(4)
# myList.print()
# myList.addAtHead(9)
# myList.print()
# myList.addAtHead(8)
# myList.print()
# print(myList.get(3))
# myList.addAtTail(1)
# myList.print()
# myList.addAtIndex(3, 6)
# myList.print()
# myList.addAtHead(3)
# myList.print()

# myList = MyLinkedList()
# myList.addAtHead(1)
# myList.print()
# myList.deleteAtIndex(0)
# myList.print()

myList = MyLinkedList()
myList.addAtIndex(-1, 0)
myList.print()
print(myList.get(0))
myList.deleteAtIndex(-1)
myList.print()