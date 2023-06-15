from regiao import Regiao
from copy import deepcopy
import osmnx as ox

class Rede:
    """
    Representa uma rede de regiões interconectadas.

    Atributos:
    - nodes (dict): Dicionário contendo as regiões da rede.
    """

    def __init__(self, G, populacoes):
        """
        Inicializa a rede com base em um grafo e uma lista de populações.

        Args:
        - G: O grafo que representa a rede de regiões.
        - populacoes: A lista de populações a serem atribuídas às regiões.
        """
        self.nodes = {node: Regiao(node, deepcopy(populacoes), list(G.neighbors(node))) for node in G.nodes}
        self.G = G
        self.steps = 0
        self.hist = {pop: [] for pop in populacoes}
        
    def plot(self, file: str):
        
        color = {'S':'green', 'I':'red', 'R':'yellow'}
        nc = []
        ns = []
        for n in self.G.nodes:
            c,s = self.nodes[n].get_SIR()
            print(n,self.nodes[n].get_S(),self.nodes[n].get_I(),self.nodes[n].get_R())
            nc.append(color[c])
            ns.append(s/10)
        fig, ax = ox.plot_graph(self.G, node_size=ns, node_color=nc, node_zorder=2, show=False)
        fig.savefig(file)

    def move(self):

        movement = [reg.simulate_move() for reg in self.nodes.values()]
        for m in movement:
            for n, pop in list(m.items()):
                for p,sir in list(pop.items()):
                    
                    self.nodes[n].populacoes[p].S += sir['S']
                    self.nodes[n].populacoes[p].I += sir['I']
                    self.nodes[n].populacoes[p].R += sir['R']

    def simulate(self):

        for reg in self.nodes.values():
            reg.simulate_edo()
        self.steps += 1
        self.plot(f'img/result{self.steps}')

    def __str__(self):
        """
        Retorna uma representação em string da rede.

        Returns:
        Uma string representando as regiões da rede.
        """
        return '\n'.join(str(node) for node in self.nodes.values())
