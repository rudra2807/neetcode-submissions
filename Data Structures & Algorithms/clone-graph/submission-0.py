"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hashmap = {}
        def dfs(node):
            
            if node in hashmap:
                return hashmap[node]
            
            tmp = Node(node.val)
            hashmap[node] = tmp

            for n in node.neighbors:
                tmp.neighbors.append(dfs(n))
            return tmp
        
        return dfs(node) if node else None