'''
Created on 06-Oct-2021

@author: Nachiket Deo
'''

from igraph import Graph


class contact_graph:
    
    def __init__(self,vertices,weights,edgeList):
        
        self.vertices = vertices
        self.weights = weights        
        self.graph = Graph(n=vertices,edges = edgeList, edge_attrs = {'weight' : edgeList})
                

        