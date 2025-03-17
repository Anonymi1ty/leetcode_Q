# 记一下中位数使用from sortedcontainers import SortedList

"""
中位数是有序整数列表中的中间值。如果列表的大小是偶数，则没有中间值，中位数是两个中间值的平均值。

例如 arr = [2,3,4] 的中位数是 3 。
例如 arr = [2,3] 的中位数是 (2 + 3) / 2 = 2.5 。
实现 MedianFinder 类:

MedianFinder() 初始化 MedianFinder 对象。

void addNum(int num) 将数据流中的整数 num 添加到数据结构中。

double findMedian() 返回到目前为止所有元素的中位数。与实际答案相差 10-5 以内的答案将被接受。

示例 1：

输入
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
输出
[null, null, null, 1.5, null, 2.0]

解释
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // 返回 1.5 ((1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
"""


# 想法：使用平衡二叉搜索树（红黑树，），addNum每次插入一个数。findMedian进行if判断，如果事奇数返回中位数，如果是偶数取得平均值
    # 使用SortedList 是基于 平衡二叉搜索树（如红黑树） 的 自动排序 数据结构
    # 或者使用大根堆和小根堆，大根堆存放较小的一半元素，小根堆存放较大的一半元素也可
from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        # 初始化
        self.data = SortedList()      
        

    def addNum(self, num: int) -> None:
        self.data.add(num)

    def findMedian(self) -> float:
        n = len(self.data)
        if n % 2 == 1:
            return self.data[n // 2]  # 奇数个元素
        else:
            return (self.data[n // 2 - 1] + self.data[n // 2]) / 2  # 偶数个元素
