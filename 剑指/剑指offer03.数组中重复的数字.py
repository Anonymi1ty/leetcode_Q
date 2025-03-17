# 找出数组中重复的数字，并随意返回一个
# 1. 使用set集合，遍历数组，如果元素不在集合中，则加入集合，否则返回该元素
# 2. 因此，可遍历数组并通过交换操作，使元素的 索引 与 值 一一对应，而当第二次遇到数字 x 时，一定有 documents[x]=x ，此时即可得到一组重复数字。
class Solution:
    def findRepeatDocument(self, documents: List[int]) -> int:
        visited = set()
        for i in documents:
            if i not in visited:
                visited.add(i)
            else:
                return i
        # 这里return的意思是如果没有重复的数字，则返回-1
        return

class Solution:
    def findRepeatDocument(self, documents: List[int]) -> int:
        i = 0
        while i < len(documents):
            if documents[i] == i:
                i += 1
                continue
            # documents[documents[i]]的意思是将documents[i]的值作为索引，找到对应的值（例如：documents[2] = 3）
            if documents[documents[i]] == documents[i]: return documents[i]
            # 如果documents[documents[i]]和documents[i]不相等，则交换两者的值
            documents[documents[i]], documents[i] = documents[i], documents[documents[i]]
        return
