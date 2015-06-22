from collections import deque

def bfs_visited(ugraph, start_node):
    q = deque([]);
    visited = {start_node};
    q.append(start_node)
    while len(q) != 0:
        j = q.popleft()
        for h in ugraph[j]:
            if h not in visited:
                visited.add(h)
                q.append(h)
    return visited

def cc_visited(ugraph):
    res = []
    keys = ugraph.keys()
    while len(keys) != 0:
        start = keys[0]
        cc = bfs_visited(ugraph,start)
        res.append(cc)
        for i in cc:
            if i in keys:
                keys.remove(i)
    return res

def largest_cc_size(ugraph):
    connected_components= cc_visited(ugraph)
    res = 0
    for i in connected_components:
        if len(i) > res:
            res = len(i)
    return res


EX_GRAPH1 = {0:set([1,4,5]),1:set([2,6]),2:set([3]),3:set([0]),4:set([1]),5:set([2]),6:set([]),7:set([8]),8:set([])}
print largest_cc_size(EX_GRAPH1)
