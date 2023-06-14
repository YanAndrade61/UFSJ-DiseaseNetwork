from ode import *
import numpy as np
import matplotlib.pyplot as plt

class Regiao:
    """
    Representa uma região em um modelo de simulação.

    Atributos:
    - id (int): O identificador da região.
    - populacoes (list): Lista de populações na região.
    - vizinhos (list): Lista de regiões vizinhas.
    """

    def __init__(self, id: int, populacoes: list, vizinhos: list):
        self.id = id
        self.populacoes = populacoes
        self.vizinhos = vizinhos
        self.hist = {pop.label: [] for pop in populacoes}
        self.steps = 0

    def get_S(self):
        return sum(pop.S for pop in self.populacoes)

    def get_I(self):
        return sum(pop.I for pop in self.populacoes)

    def get_R(self):
        return sum(pop.R for pop in self.populacoes)
    
    def get_SIR(self):
        return sum(pop.S+pop.I+pop.R for pop in self.populacoes)

    def simulate_edo(self):
        
        I_norm = self.get_I()/self.get_SIR()
        for pop in self.populacoes:
            _yk = [pop.S,pop.I,pop.R,I_norm]
            pop.S,pop.I,pop.R,_ = rk4(ode_system,_yk,pop.params)
            self.hist[pop.label].append([pop.S,pop.I,pop.R])
        
        self.steps += 1

    def plot(self):
        fig, ax = plt.subplots(1, len(self.populacoes), squeeze=False)
        time = np.arange(0, self.steps * 0.01, 0.01)

        for i, pop in enumerate(self.populacoes):
            ax[0][i].set(xlabel='time (days)', ylabel='[Y]', title=pop.label)
            ax[0][i].plot(time, np.array(self.hist[pop.label]))
            ax[0][i].legend(['S', 'I', 'R'], loc='best')
            ax[0][i].grid()

        fig.savefig('simulation')
        plt.show()

    def __str__(self):
        string = f'\nid: {self.id}\nvizinhos: {self.vizinhos}'
        string += ''.join(str(pop) for pop in self.populacoes)
        return string