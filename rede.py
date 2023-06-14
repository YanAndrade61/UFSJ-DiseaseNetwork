from regiao import Regiao

class Rede:
    def __init__(self, G, populacoes):
        self.nodes = {node: Regiao(node,populacoes,list(G.neighbors(node))) for node in G.nodes}

    def __str__(self):
        string = f""
        for n in self.nodes.values():
            string += str(n) + '\n'
        return string    
