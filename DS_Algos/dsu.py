def make_set(v):
    parent[v] = v

def find_set(v):
    if v == parent[v]:
        return v
    
    parent[v] = find_set(parent[v])

    return parent[v]

def find_set_iter(v):
    v_ans = v

    while v_ans != parent[v_ans]:
        v_ans = parent[v_ans]

    while v != parent[v]:
        v_copy = v
        v = parent[v]
        parent[v_copy] = v_ans
    
    return v_ans

def union_sets_rank(u, v):
    u_root = find_set(u)
    v_root = find_set(v)

    if u_root == v_root:
        return
    
    if rank[u_root] < rank[v_root]:
        parent[u_root] = v_root
    elif rank[u_root] > rank[v_root]:
        parent[v_root] = u_root
    else:
        parent[v_root] = u_root
        rank[u_root] = rank[v_root] + 1

def union_sets_size(u, v):
    u_root = find_set(u)
    v_root = find_set(v)

    if u_root == v_root:
        return
    
    if size[u_root] < size[v_root]:
        parent[u_root] = v_root
        size[v_root] += size[u_root]
    else:
        parent[v_root] = u_root
        size[u_root] += v_root
