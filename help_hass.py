__author__ = 'Georgi Sinekliev'

import sys
from collections import defaultdict


def bfs(graph, start, end):
    queue = []
    parents = {}
    queue.append(start)
    stop = False
    while queue and not stop:
        node = queue.pop()
        for neighbor in graph[node]:
            parents[neighbor] = node
            queue.append(neighbor)
            if neighbor == end:
                stop = True
                break

    path = []
    if stop:
        parent = end
        while parent != start:
            path.append(parent)
            parent = parents[parent]

        path.append(start)

    print ' '.join(path[::-1])


def main():
    graph = defaultdict(list)  # directed graph presented as list of neighbors

    while True:
        line = sys.stdin.readline()
        if not line.strip():
            break
        start, end = line.split()
        graph[start].append(end)

    bfs(graph, 'H', 'L')


if __name__ == '__main__':
    main()
