"""
读者来到图书馆排队借还书，图书管理员使用两个书车来完成整理借还书的任务。书车中的书从下往上叠加存放，图书管理员每次只能拿取书车顶部的书。排队的读者会有两种操作：

push(bookID)：把借阅的书籍还到图书馆。
pop()：从图书馆中借出书籍。
为了保持图书的顺序，图书管理员每次取出供读者借阅的书籍是 最早 归还到图书馆的书籍。你需要返回 每次读者借出书的值 。

如果没有归还的书可以取出，返回 -1 。

示例 1：

输入：
["BookQueue", "push", "push", "pop"]
[[], [1], [2], []]
输出：[null,null,null,1]
解释：
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.pop(); // return 1, queue is [2]
"""

# 思路：两个stack实现队列
# 1. 定义两个栈，一个用于入队，一个用于出队

from collections import deque
class CQueue:

    def __init__(self):
        # 初始化两个栈
        self.stack1 = deque()
        self.stack2 = deque()
        

    def appendTail(self, value: int) -> None:
        # 入队操作，将元素压入栈1
        self.stack1.append(value)
        

    def deleteHead(self) -> int:
        # 出队操作
        if not self.stack2:
            # 如果栈2为空，将栈1中的元素全部弹出到栈2中
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop() if self.stack2 else -1
        


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()