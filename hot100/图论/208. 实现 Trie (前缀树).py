"""
请你实现 Trie 类：

Trie() 初始化前缀树对象。
void insert(String word) 向前缀树中插入字符串 word 。
boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。
 

示例：

输入
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
输出
[null, null, true, false, true, null, true]

"""

# 思路：
    # 定义当前节点的所有子节点映射表，key 为字符，value 为 TrieNode
    
from typing import Dict

class TrieNode:
    def __init__(self):
        # children：当前节点的所有子节点映射表，key 为字符，value 为 TrieNode
        self.children: Dict[str, "TrieNode"] = {}
        # is_end：是否有单词在此节点结束（即：插入过以这里为末尾的完整单词）
        self.is_end: bool = False


class Trie:
    def __init__(self):
        """
        初始化前缀树：
        根节点不存放任何字符，仅作为所有字符串的共同起点。
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        向前缀树中插入字符串 word。
        逐字符向下走/创建节点；最后把末尾节点的 is_end 置为 True。
        """
        node = self.root
        for ch in word:
            # 若不存在 ch 对应的子节点，则创建
            if ch not in node.children:
                # 如果当前节点的 children 里，没有 ch 这个字符对应的子节点，就新建一个 TrieNode，挂在 children 的字典里。
                node.children[ch] = TrieNode()
            # 指针下移到 ch 子节点
            node = node.children[ch]
        # 整个 word 插入完成，把末尾节点标记为“单词结束”
        node.is_end = True

    def search(self, word: str) -> bool:
        """
        检索完整单词 word 是否存在。
        规则：必须逐字符匹配到路径，且最后一个节点 is_end 为 True 才算存在。
        """
        node = self.root
        for ch in word:
            if ch not in node.children:  # 中途缺节点 => 不存在
                return False
            node = node.children[ch]
        # 只有当末尾节点被标记为“单词结束”，才代表插入过完整的 word
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        """
        判断是否存在以 prefix 作为前缀的已插入单词。
        规则：只要能沿着 prefix 的字符一路走到底，就返回 True；
             不需要末尾 is_end 为 True（因为只检查前缀）。
        """
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True
