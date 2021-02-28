# Nama      : Rizky Anggita S Siregar
# NIM       : 13519132
# Tanggal   : 28 Februari 2021
# Deskripsi : Topological Sort (Decrease and Conquer Algorithm)
# TUCIL 2 STRATEGI ALGORITMA 

import os

class Graph():
    #Directed Acyclic Graph with List Representation
    def __init__(self):
        self.nodes = []
        self.adj_list = {}

    def add_node(self, node):
        #Adding new node
        self.nodes.append(node)
        self.adj_list[node] = []

    def print_adj_in_list(self):
        print("\nIn Node")
        for node in self.nodes:
            print(node, "<-", self.adj_list[node])
    
    def print_adj_out_list(self):
        print("\nOut Node")
        for n in self.nodes:
            temp = []
            for node in self.adj_list:
                if n in self.adj_list[node] and node != n:
                    temp.append(node)
            print(n, "->", temp)

    def add_edge_in(self, u, v):
        self.adj_list[u].append(v)

    def count_degree_in(self, u):
        #Count in-degree for node u
        return len(self.adj_list[u])
    
    def count_degree_out(self,u):
        #Count out-degree for node u
        count = 0
        for node in self.adj_list:
            if u in self.adj_list[node]:
                count += 1
        return count
    
    def del_node_in(self,u):
        # Delete node u from graph
        # Process: delete u from every adjacent of u
        # and delete node u from list of nodes
        for node in self.adj_list:
            if u in self.adj_list[node] and node != u:
                self.adj_list[node].remove(u)
        
        self.nodes.remove(u)
        self.adj_list.pop(u, None)
    
    def topological_sort(self):
        #DAG Topological Sort
        list_sorted = []
        list_of_degin_0 = []
        i = 0
        n_node = len(self.nodes)

        while(len(list_sorted) != n_node):
            list_of_degin_0 = []
            for node in self.nodes:
                degin = self.count_degree_in(node)
                if(degin == 0):
                    list_of_degin_0.append(node)
                    list_sorted.append(node)

            #Didapatkan list node dengan degree-in = 0
            print("\nSemester", i+1, ": ",end=" ")
            for node in list_of_degin_0:
                print(node, end=" ")
                self.del_node_in(node)
            i += 1
            # print()

        print("\n\nTopological Sort: ", list_sorted)


def add_graph_from_txt(graf, file):
    for line in f:
        a = line.rsplit(", ")
        for i in range (len(a)): 
            if (i==0):
                graf.add_node(a[0].rstrip(".\n").split('.')[0])
            else:
                temp = a[i].rstrip(".\n")
                graf.add_edge_in(a[0].rstrip(".\n"), temp)

#------ MAIN PROGRAM ------#

# Input nama file
filename = input("Masukkan nama file: ")
a = os.path.abspath(os.curdir)

if os.name=='nt':
    file_path = os.path.join("..\\test", filename)
else:
    file_path = os.path.join(a, "test", filename)

# Membuat graph dari txt
graf = Graph()
f = open(file_path, "r")
add_graph_from_txt(graf, f)

print("Graph yang diinput: ")
graf.print_adj_in_list()
graf.print_adj_out_list()

# Topological Sort DAG
graf.topological_sort()