
## 链表题目一

### 141. 环形链表
+ **题目：**
	+ 给定一个链表，判断链表中是否有环。
	+ 给定一个链表，判断链表中是否有环。
	+ 如果链表中存在环，则返回 true 。 否则，返回 false 。
	+ 进阶：
		+ 你能用 O(1)（即，常量）内存解决此问题吗？
+ **解析：**
	+ 原理分析：知道套路的聪明小伙伴可能马上就说：这还不简单，直接快慢指针啊！但是在真实面试场景时万一碰到较真的面试官问你：
		+ ** 怎么证明快慢指针在环中是可以相遇的？**
		+ ** 为什么快指针步长要为 2 ？3，4，5可以吗？**
		+ **  如何确定环的起始结点呢？**
[以上问题参考资料](https://leetcode-cn.com/problems/linked-list-cycle/solution/xiang-jie-wei-shi-yao-yong-yi-bu-liang-b-i6xo/)　to-do
	+ 算法流程：
		 + 我们定义两个指针，一快一满。慢指针每次只移动一步，而快指针每次移动两步。
		 + 初始时，快慢指针的位置都在 head。
		 + 如果在移动的过程中，快指针反过来追上慢指针，就说明该链表为环形链表。否则快指针将到达链表尾部，该链表不为环形链表。

+ **代码：**
```python
def hasCycle(head):
    if not head: return False
    slow = fast = head
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True
    return False
```

### 142. 环形链表 II
+ **题目：**
	+ 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
	+ 进阶：
		+ 你是否可以使用 O(1) 空间解决此题？
	
+ **解析：**
	+ 算法流程：
		 + 我们定义两个指针，一快（fast）一慢（slow）。慢指针每次只移动一步，而快指针每次移动两步。
		 + 初始时，快慢指针的位置都在 head。
		 + 如果在移动的过程中，快指针反过来追上慢指针，就说明该链表为环形链表。否则快指针将到达链表尾部，该链表不为环形链表。
		 + 如果发现 slow 与 fast 相遇，我们再额外使用一个指针 start，起始它指向链表头部；随后，它和 slow 每次向后移动一个位置。最终，它们会在入环点相遇。

+ **代码：**
```python
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
```

### 160. 相交链表
+ **题目：**
	+ 编写一个程序，找到两个单链表相交的起始节点。
	+ 注意：
		+ 如果两个链表没有交点，返回 null.
		+ 在返回结果后，两个链表仍须保持原有的结构。
		+ 可假定整个链表结构中没有循环。
		+ 程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。

+ **解析：**
	+ 算法流程：
		+ 创建两个指针 pa 和 pb，分别初始化为链表 A 和 B 的头结点。然后让它们向后逐结点遍历。
		+ 当 pa 到达链表的尾部时，将它重定位到链表 B 的头结点 ); 类似的，当 pb 到达链表的尾部时，将它重定位到链表 A 的头结点。
		+ 若在某一时刻 pa 和 pb 相遇，则 pa或者pb 为相交结点。
		+ 如果两个链表存在相交，它们末尾的结点必然相同。因此当 pa或者pb 到达链表结尾时，记录下链表 A或B 对应的元素。若最后元素不相同，则两个链表不相交。

+ **代码：**
```python
def getIntersectionNode(headA, headB):
	if not headA or not headB: return
	pa, pb = headA, headB
	while pa != pb:
		pa = pa.next if pa else headB
		pb = pb.next if pb else headA
	return pa
```
