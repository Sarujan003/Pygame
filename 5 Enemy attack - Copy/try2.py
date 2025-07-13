"""Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Explanation: The given graph is shown above.
Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.
Example 2:

Input: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
Output: [4]
Explanation:
Only node 4 is a terminal node, and every path starting at node 4 leads to node 4.
"""
edges = [[0,1],[1,2],[3,4]]
conn_components = 0
n = 5
matrix = [[0 for i in range(n)] for i in range(n)]

for edge in edges:
    matrix[edge[0]][edge[1]] = 1
    matrix[edge[1]][edge[0]] = 1
visited = [False] * n

def dfs(node):
            visited[node] = True
            for nei in range(n):
                if matrix[node][nei]==1 and not visited[nei]:
                    dfs(nei)

for node in range(n):
            if not visited[node]:
                dfs(node)
                conn_components += 1

print(conn_components)