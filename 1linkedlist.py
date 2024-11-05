# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 09:36:11 2024

@author: abish
"""

class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head = None
        self.avail=None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        
    def insert(self,data,index):
        new_node=Node(data)
        i=1
        cur=self.head
        while i<index:
            cur=cur.next
            i=i+1
        cu1=cur.next
        cur.next=new_node
        cur=cur.next
        cur.next=cu1
        
    def delete(self,data, index):
        i=1
        cur=self.head
        while i<index:
            cur=cur.next
            i=i+1
        cur1=cur.next
        cur2=cur1.next
        cur.next=cur2
        self.avail=cur1
        self.avail.next=None
        
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Create linked list and append nodes based on user input
ll = LinkedList()

n = int(input("Enter the number of nodes: "))
for _ in range(n):
    data = int(input("Enter node value: "))
    ll.append(data)

print("Linked List:")
ll.print_list()

data=int(input(" enter the data to be inserted : "))
index= int(input("enter the index at which data to be inserted : "))
ll.insert(data, index)

print("Linked List:")
ll.print_list()

data=int(input(" enter the data to be deleted : "))
index= int(input("enter the index at which data to be deleted : "))
ll.delete(data, index)

print("Linked List:")
ll.print_list()