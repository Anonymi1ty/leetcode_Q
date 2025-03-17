#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 需要记录NULL，这样才可以任意使用遍历顺序恢复树结构
import queue
class Codec:

    def serialize(self, root):
        # 使用#_记录空节点
        if root is None:
            return "#_"
        # 非空节点使用value+_记录，先序遍历导出字符串（根左右）
        return str(root.val) + "_" + self.serialize(root.left) + self.serialize(root.right)
    
    # 准备一个队列，将字符串分割后放入队列（先进先出，方便后续使用）
    def recover_by_str(self, data):
        # 准备一个list存放分割后的字符串
        list_ = data.split("_")
        q = queue.Queue()
        # 根据_恢复原来的value
        for i in list_:
            # 入栈
            q.put(i)
        return q

    def deserialize(self, data):
        # 如果传入的是字符串而不是队列，则先进行字符串的分割转换
        if isinstance(data, str):
            data = self.recover_by_str(data)
        
        # 从队列中取出一个元素
        val = data.get()
        # 如果为空，返回None
        if val == "#":
            return None
        # 根据根左右的顺序恢复树结构,int是为了将字符串转化为数字
        # 先建立根节点
        root = TreeNode(int(val))
        root.left = self.deserialize(data)
        root.right = self.deserialize(data)
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

