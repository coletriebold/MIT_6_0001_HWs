#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 09:35:39 2020

@author: coletriebold
"""
from ps2 import load_map, get_best_path
from graph import Digraph, Node, WeightedEdge

    
digraph = load_map("mit_map.txt")
digraph = Digraph()
na = Node('a')
nb = Node('b')
nc = Node('c')

digraph.add_node(na)
digraph.add_node(nb)
digraph.add_node(nc)

e1 = WeightedEdge(na, nb, 15, 10)
e2 = WeightedEdge(na, nc, 14, 6)
e3 = WeightedEdge(nb, nc, 3, 1)

digraph.add_edge(e1)
digraph.add_edge(e2)
digraph.add_edge(e3)

start = na
end = nc
max_dist_outdoors = 100
path = []
best_dist = 9999
best_path = []
the_best_path = get_best_path(digraph, start, end, path, max_dist_outdoors, best_dist, best_path)
print(the_best_path)