from collections import defaultdict

def validPath(n: int, edges: [[int]], start: int, end: int) -> bool:
    if len(edges) < 1:
        return False

    graph = defaultdict(list)
    for i in range(len(edges)):
        graph[edges[i][0]].append(edges[i][1])
        graph[edges[i][1]].append(edges[i][0])
    stack, visited = [graph[start]], [False] * n
    visited[start] = True

    while stack and not all(visited):
        nodes = stack.pop()
        for node in nodes:
            if node == end:
                return True
            if not visited[node] and node < len(graph):
                stack.append(graph[node])
            visited[node] = True
    return False

if __name__ == "__main__":
    res = validPath(3, [[0,1],[1,2],[2,0]], 0, 2)
    res