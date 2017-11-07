##  -----------------------------------------------------------------------------  ##
##  -----------------------------------------------------------------------------  ##
##  ---                     working the networks in python                    ---  ##
##  ---                         by Alexandre Loures                           ---  ##
##  ---               Vicosa, Minas Gerais, Brazil 2017/11/07                 ---  ##
##  -----------------------------------------------------------------------------  ##
##  -----------------------------------------------------------------------------  ##

## testing the computational routine of Professor Daniel


import community

import matplotlib.pyplot as plt

import networkx as nx

import os

os.chdir ('C:\\Users\\Inspiron\\OneDrive\\academic\\research-agenda\\computational-economics')

G = nx.read_pajek ('karate.paj')

degree = nx.degree_centrality (G)

closeness = nx.closeness_centrality (G)

betwennessNodes = nx.betwenness_centrality (G)

betwennessEdges = nx.edge_betwenness_centrality (G)

eigenvector nx.eigenvector_centrality_numpy (G)

Gund = nx.Graph (G)

partition = community.best_partition (Gund)

size = float (len (set (partition.values ())))

pos = nx.spring_layout (Gund)

count = 0.

for com in set (partition.values()) :
    if count == 0:
        theColor = 'r'
    elif count == 1:
        theColor = 'b'
    elif count == 2:
        theColor = 'g'
    elif count == 3:
        theColor = 'y'
    count = count + 1.
    list_nodes = [nodes for nodes in partition.keys ()
                            if partition [nodes] == com]
    nx.draw_networkx_nodes (Gund, pos, list_nodes, node_size = 300,
                            node_color = theColor)

nx.draw_networkx_edges (Gund, pos, alpha = .5)

plt.show ()  ## named network-in-python.pdf graph
