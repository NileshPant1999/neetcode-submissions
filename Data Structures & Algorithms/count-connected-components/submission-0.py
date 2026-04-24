from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        visited = set()
        count = 0
    
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        
        def dfs(node):
            if node not in visited:
                visited.add(node)
                for nei in graph[node]:
                    dfs(nei)
                    

        for i in range(n):
            if i not in visited:
                dfs(i)
                count+=1

        return count
