graph = {
    'a': ['c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['a', 'd'],
    'e': ['b', 'c']
}

def find_all_paths(graph, start, end, path = []):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        if node in path:
            newpaths = find_all_paths(graph, node, end, path)
        for newpath in newpaths:
            paths.append(newpath)
    return paths
print(find_all_paths(graph, 'd', 'c'))

