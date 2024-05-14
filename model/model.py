import networkx as nx

from database.DAO import DAO

class Model:

    def __init__(self):
        self.vertici=[]
        self.grafo = nx.Graph()
        self.idmap ={}


    def creagrafo(self,anno):
        self.grafo.clear()
        self.vertici=DAO.vertici(anno)
        self.grafo.add_nodes_from(self.vertici)
        for i in self.vertici:
            self.idmap[i.CCode]=i

        archi =DAO.archi(anno)
        for i in archi:
            self.grafo.add_edge(self.idmap[i.state1no],self.idmap[i.state2no])

    def getconnesse(self):
        n = nx.number_connected_components(self.grafo)
        conn = nx.connected_components(self.grafo)
        return n


    def elencostati(self):
        result=[]
        for i in self.grafo.nodes:
            result.append((i,self.grafo.degree[i]))
        return result

    def getnodi(self):
        return len(self.grafo.nodes)

    def getarchi(self):
        return len(self.grafo.edges)

    def raggiungibili(self,v):
        lista = nx.dfs_tree(self.grafo,self.idmap[v])
        lista.remove_node(self.idmap[v])
        return lista.nodes