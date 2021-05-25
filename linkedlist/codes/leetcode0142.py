#!/usr/bin/env python3
# -*-coding:utf-8 -*-

from tools import ListNode, generateList, printList
from tools import generateCycleList


def detectCycle(head):
    if not head: return
    slow = fast = start = head
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            while start != slow:
                start, slow = start.next, slow.next
            return start
    return


if __name__ == '__main__':
    ll = generateList([1,2,3,4]) 
    cll = generateCycleList()
    print(detectCycle(ll))       
    print(detectCycle(cll))       


