def dfs(graph, start, visited):
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def find_dead_ends(graph):

    dead_ends = []
    visited = set()
    for node in graph:
        if node not in visited:
            dfs(graph, node, visited)
    
    for node in graph:
        if len(graph[node]) == 1:
            dead_ends.append((node, graph[node][0]))
    
    return dead_ends

def main():

    with open("input.txt", "r") as f:
        n, m = map(int, f.readline().strip().split())
        graph = {}
        for _ in range(m):
            v, w = map(int, f.readline().strip().split())
            graph.setdefault(v, []).append(w)
            graph.setdefault(w, []).append(v)  

    dead_ends = find_dead_ends(graph)

    num_signs = len(dead_ends)
    print(num_signs)
    for dead_end in dead_ends:
        print(f"{dead_end[0]} {dead_end[1]}")

if __name__ == "__main__":
    main()
