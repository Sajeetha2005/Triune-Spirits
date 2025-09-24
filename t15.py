from typing import List, Dict

def enumerate_paths(file_path: str, start: str, end: str) -> List[List[str]]:

    graph: Dict[str, List[str]] = {}
    with open(file_path, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) != 2:
                continue
            u, v = parts
            graph.setdefault(u, []).append(v)
            graph.setdefault(v, []).append(u)  
    all_paths = []
    def dfs(node, path, visited):
        path.append(node)
        visited.add(node)

        if node == end:
            all_paths.append(path.copy())
        else:
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    dfs(neighbor, path, visited)
        path.pop()
        visited.remove(node)
    dfs(start, [], set())
    return all_paths
if __name__ == "__main__":
    paths = enumerate_paths("edges.txt", "A", "E")
    print("All paths from A to E:")
    for p in paths:
        print(" -> ".join(p))
