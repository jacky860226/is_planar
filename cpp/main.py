import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import networkx as nx
from is_planar import is_planar

if __name__ == '__main__':
    g = nx.Graph()
    n,m = map(int, input().split())
    for i in range(m):
        u,v = map(int, input().split())
        g.add_edge(u,v)
    if (is_planar(g)):
        print("YES")
    else:
        print("NO")