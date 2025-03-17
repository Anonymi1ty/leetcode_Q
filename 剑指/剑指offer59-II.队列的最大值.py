"""
请设计一个自助结账系统，该系统需要通过一个队列来模拟顾客通过购物车的结算过程，需要实现的功能有：

get_max()：获取结算商品中的最高价格，如果队列为空，则返回 -1
add(value)：将价格为 value 的商品加入待结算商品队列的尾部
remove()：移除第一个待结算的商品价格，如果队列为空，则返回 -1
注意，为保证该系统运转高效性，以上函数的均摊时间复杂度均为 O(1)

 

示例 1：

输入: 
["Checkout","add","add","get_max","remove","get_max"]
[[],[4],[7],[],[],[]]

输出: [null,null,null,7,4,7]
"""

# 思路：max的处理：当执行入队 add() 时： 若入队一个比队列某些元素更大的数字 x ，则为了保持此列表递减，需要将双向队列 尾部所有小于 x 的元素 弹出。

from collections import deque
class Checkout:

    def __init__(self):
        self.check = deque()
        self.max_check = deque()
        

    # 用列表的形式存储max，最大值放左边
    def get_max(self) -> int:
        if not self.max_check:
            return -1
        return self.max_check[0]
        

    def add(self, value: int) -> None:
        self.check.append(value)
        # 先要判断是否当前值比队列最后几个值大，如果大,挨个弹出，保证max_check的递减性质
        while self.max_check and self.max_check[-1] < value:
            self.max_check.pop()
        self.max_check.append(value)
        

    def remove(self) -> int:
        if not self.check:
            return -1
        else:
            remove = self.check.popleft()
            if remove == self.max_check[0]:
                self.max_check.popleft()
            return remove
        
        


# Your Checkout object will be instantiated and called as such:
# obj = Checkout()
# param_1 = obj.get_max()
# obj.add(value)
# param_3 = obj.remove()