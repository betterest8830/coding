#!/usr/bin/env python3
# -*-coding:utf-8 -*-


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def generateList(nums):
    dummy=pre=ListNode(0)
    for num in nums:
        cur = ListNode(num)
        pre.next, pre = cur, cur
    return dummy.next

def printList(head):
    stk = []
    while head:
        stk.append(str(head.val))
        head = head.next
    print('->'.join(stk))

def generateCycleList():
    '''
    head = [3,2,0,-4], pos = 1
    '''
    nums = [3,2,0,-4]
    head1, head2, head3, head4 = list(map(ListNode, nums))
    head1.next, head2.next, head3.next, head4.next = head2, head3, head4, head2
    return head1

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    head = generateList(nums)
    printList(head)
  
        


