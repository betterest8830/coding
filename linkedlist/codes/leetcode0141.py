#!/usr/bin/env python3
# -*-coding:utf-8 -*-

from tools import ListNode, generateList, printList
from tools import generateCycleList

def hasCycle(head):
    if not head: return False
    slow = fast = head
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True
    return False


if __name__ == '__main__':
    ll = generateList([1,2,3,4]) 
    cll = generateCycleList()
    print(hasCycle(ll))       
    print(hasCycle(cll))       


