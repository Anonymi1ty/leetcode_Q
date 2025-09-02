"""
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

实现 MinStack 类:

MinStack() 初始化堆栈对象。
void push(int val) 将元素val推入堆栈。
void pop() 删除堆栈顶部的元素。
int top() 获取堆栈顶部的元素。
int getMin() 获取堆栈中的最小元素。
"""

# 思路：
    # 1. 使用递归来交换每一对节点
    # 2. 递归的终止条件是当前节点或下一个节点为空

    
from collections import deque
class MinStack:

    def __init__(self):
        # 记录栈中的元素
        self.stack = deque()
        # 记录最小值栈
        self.min_stack = deque()

    def push(self, val: int) -> None:
        # 将元素压入栈中
        self.stack.append(val)
        
        if not self.min_stack or val <= self.min_stack[-1]:
            # 如果最小值栈为空或者当前值小于等于最小值栈顶元素，则将当前值压入最小值栈
            self.min_stack.append(val)
            
        

    def pop(self) -> None:
        # 弹出栈顶元素
        if self.stack:
            top = self.stack.pop()
            # 如果弹出的元素是当前最小值，则也从最小值栈中弹出
            if top == self.min_stack[-1]:
                self.min_stack.pop()
        

    def top(self) -> int:
        # 获取栈顶元素
        return self.stack[-1] if self.stack else None
        

    def getMin(self) -> int:
        # 获取当前最小值
        return self.min_stack[-1] if self.min_stack else None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()