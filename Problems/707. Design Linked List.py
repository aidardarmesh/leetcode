from typing import *

class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. 
        If the index is invalid, return -1.
        """
        idx = 0
        node = self.head
        
        while node:
            if idx == index:
                return node.val
            
            node = node.next
            idx += 1
        
        return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. 
        After the insertion, the new node will be the first node of the linked list.
        """
        node = ListNode(val)
        
        if not self.head:
            self.head = node
            return
        
        node.next = self.head
        self.head = node
        
    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = ListNode(val)
        
        if not self.head:
            self.head = node
            return
        
        tail = self.head
        
        while tail and tail.next:
            tail = tail.next
            
        tail.next = node
        node.prev = tail

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. 
        If index equals to the length of linked list, the node will be appended to the end of linked list. 
        If index is greater than the length, the node will not be inserted.
        """
        # addAtHead
        if index == 0:
            self.addAtHead(val)
            return
        
        # list is not empty
        node = ListNode(val)
        prev = cur = self.head
        idx = 0
        
        while cur:
            if idx == index:
                prev.next = node
                node.next = cur
                return
            
            prev = cur
            cur = cur.next
            idx += 1
        
        if idx == index:
            prev.next = node
        
    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if not self.head:
            return
        
        # delete at 0th
        if index == 0:
            self.head = self.head.next
            return
        
        prev = cur = self.head
        idx = 0
        
        while cur:
            if idx == index:
                prev.next = cur.next
                return
            
            prev = cur
            cur = cur.next
            idx += 1
