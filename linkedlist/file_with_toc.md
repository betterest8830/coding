<a name="index">**Index**</a>
&emsp;<a href="#0">链表题目一</a>  
&emsp;&emsp;<a href="#1">141. 环形链表</a>  
&emsp;&emsp;<a href="#2">142. 环形链表 II</a>  

## <a name="0">链表题目一</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>

* [链表题目一](#链表题目一)
	* [141. 环形链表](#141. 环形链表)
	* [142. 环形链表 II](#142. 环形链表 II)

### <a name="1">141. 环形链表</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
+ **题目：**
	+ 给定一个链表，判断链表中是否有环。
	+ 给定一个链表，判断链表中是否有环。
	+ 如果链表中存在环，则返回 true 。 否则，返回 false 。
	+ 进阶：
		+ 你能用 O(1)（即，常量）内存解决此问题吗？
+ **解析：**

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

### <a name="2">142. 环形链表 II</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
+ **题目：**
	+ 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
	+ 进阶：
		+ 你是否可以使用 O(1) 空间解决此题？
	
+ **解析：**

+ **代码：**