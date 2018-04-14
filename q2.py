from collections import defaultdict
from pprint import pprint
from functools import reduce
from itertools import combinations
import networkx as nx
from itertools import combinations
from pprint import pprint
import numpy as np
import sys

class variant():
    def __init__(self, pos, allele):
        self.pos = pos
        self.allele = allele

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.pos == other.pos and self.allele == other.allele
        return False

    def __hash__(self):
        return hash((self.pos, self.allele))

    def same_pos(self, other):
        return self.pos == other.pos
        

    def __repr__(self):
        return "variant({}:{})".format(self.pos, self.allele)
    


variants = []
with open("./hic_chr20_90x") as f:
    for line in f:
        line = line.strip().split()[1:]
        curr = [variant(i.split(':')[0], i.split(':')[1]) for i in line]
        variants.append(curr)

sys.stderr.write("{}\n".format(len(variants)))
count = 0

G = nx.graph.Graph()
for var in variants:
    G.add_nodes_from(var)
    count += 1
    for edge in combinations(var,2):
        cc = nx.node_connected_component(G,edge[0])
        cc |= nx.node_connected_component(G,edge[1])
        cc = [x.pos for x in cc]
        if (len(cc) == len(set(cc))):
            G.add_edge(*edge)

    if count % 1000 == 0:
        sys.stderr.write("{}\n".format(count))

a = [len(x) for x in nx.connected_components(G)]
for x in a:
    print(x)



#a = next(nx.connected_components(G))
#a = list(a)
#from collections import defaultdict
#b = defaultdict(int)
#for x in a:
#    b[x.pos] += 1
#[(x,y) for x,y in b.items() if y > 1]
#[i for i,x in enumerate([y.pos for y in a]) if x == '42004629']
#print(a[0], a[44123])
#
#
#
#h_alleles = []
#h_positions = []
#
#haplos = []
#
#while variants:
#    done = False
#    v = variants.pop()
#    p = positions.pop()
#    already = [v in x for x in haplos]
#    inter = [v & x for x in haplos]
#    
#    for i in range(len(haplos)):
#        if inter[i] and not already[i]:
#            haplos.append(v | haplos[i])
#            done = True
#        if done:
#            break
#    
#    if not done:
#        haplos.append(v)
#    
#    
#        
#
