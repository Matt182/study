"""
Connected components and graph resilience
"""
from collections import deque

def bfs_visited(ugraph, start_node):
    """

    :param ugraph: undirected graph for example: {0:set([1,2]),1:set([]),2:set([])}
    :param start_node: int
    :return:travel thrue nodes
    """
    que = deque([]);
    visited = {start_node};
    que.append(start_node)
    while len(que) != 0:
        node = que.popleft()
        for neighbour in ugraph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                que.append(neighbour)
    return visited

def cc_visited(ugraph):
    """

    :param ugraph: undirected graph for example: {0:set([1,2]),1:set([]),2:set([])}
    :return:all connected components
    """
    res = []
    keys = ugraph.keys()
    while len(keys) != 0:
        start = keys[0]
        ccom = bfs_visited(ugraph,start)
        res.append(ccom)
        for node in ccom:
            if node in keys:
                keys.remove(node)
    return res

def largest_cc_size(ugraph):
    """

    :param ugraph:
    :return:
    """
    connected_components= cc_visited(ugraph)
    res = 0
    for concomp in connected_components:
        if len(concomp) > res:
            res = len(concomp)
    return res



def compute_resilience(ugraph, attack_order):
    """

    :param ugraph:
    :param attack_order:
    :return:
    """
    res =[]
    res.append(largest_cc_size(ugraph))
    for node in attack_order:
        ugraph.pop(node)
        for ver in ugraph.keys():
            if node in ugraph[ver]:
                ugraph[ver].remove(node)
        res.append(largest_cc_size(ugraph))
    return res

