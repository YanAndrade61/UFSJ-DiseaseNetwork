from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
from copy import deepcopy
from src.regiao import Regiao
import osmnx as ox
import numpy as np

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
        self.pdf = PdfPages('disease-network.pdf')

    def plot_graph(self, file: str):
        
        color = {'S':'green', 'I':'red', 'R':'yellow'}
        nc = []
        ns = []
        for n in self.G.nodes:
            c,s = self.nodes[n].get_SIR()
            nc.append(color[c])
            ns.append(s/10)
        fig, ax = ox.plot_graph(self.G, node_size=ns, node_color=nc, node_zorder=2, show=False)
        self.pdf.savefig(fig)
        plt.close()

    def plot_edo(self):
        """
        Gera um gráfico da simulação das populações na rede.

        O gráfico mostra a variação dos valores S, I e R ao longo do tempo para cada população.
        """
        fig, ax = plt.subplots(len(self.hist),1, squeeze=False,figsize=(10,7))
        time = np.arange(0, self.steps * 0.01, 0.01)

        for i,label in enumerate(self.hist):
            ax[i][0].set(xlabel='time (days)', ylabel='[Y]', title=label)
            ax[i][0].plot(range(self.steps), np.array(self.hist[label]))
            ax[i][0].legend(['S', 'I', 'R'], loc='best')
            ax[i][0].grid()
        fig.tight_layout(pad=2.0)
        self.pdf.savefig(fig)
        self.pdf.close()

    def move(self):

        movement = [reg.simulate_move() for reg in self.nodes.values()]
        for m in movement:
            for n, pop in list(m.items()):
                for p,sir in list(pop.items()):
                    
                    self.nodes[n].populacoes[p].S += sir['S']
                    self.nodes[n].populacoes[p].I += sir['I']
                    self.nodes[n].populacoes[p].R += sir['R']

    def run_edo(self):

        for reg in self.nodes.values():
            reg.simulate_edo()
        self.steps += 1
        self.plot_graph(f'img/result{self.steps}')
        self.update_hist()

    def update_hist(self):

        vec = {label: np.zeros(3) for label in self.hist}
        for reg in self.nodes.values():
            for label,pop in reg.populacoes.items():
                vec[label][0] += pop.S
                vec[label][1] += pop.I
                vec[label][2] += pop.R

        for label in self.hist:
            self.hist[label].append(vec[label])

    def __str__(self):
        """
        Retorna uma representação em string da rede.

        Returns:
        Uma string representando as regiões da rede.
        """
        return '\n'.join(str(node) for node in self.nodes.values())
