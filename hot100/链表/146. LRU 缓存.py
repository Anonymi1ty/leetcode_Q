"""
请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
实现 LRUCache 类：
LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。

输入
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出
[null, null, null, 1, null, -1, null, -1, 3, 4]

解释
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4
"""

# 思路：
    # 1. 使用双向链表和哈希表实现 LRU 缓存
    # 2. 哈希表用于快速查找缓存中的元素，双向链表用于维护元素的使用顺序
    # 3. 当访问元素时，将其移动到链表的头部，表示它是最近使用的
    # 4. 当缓存满时，删除链表尾部的元素，表示它是最久未使用的
        # 哈希表的 key 是元素的键，value 是链表节点
    
from typing import List, Optional


from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        # OrderedDict 会按插入顺序维护键
        # 我们约定：最“旧”的键在最左侧（first），最“新”的键在最右侧（last）
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # 访问过后，将它移到最右侧（变成最新）
        self.cache.move_to_end(key, last=True)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # 已存在的话，先移到最右侧再更新值
            self.cache.move_to_end(key, last=True)
        self.cache[key] = value
        # 如果超出容量，就 pop 出最左侧（最久未使用）
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)