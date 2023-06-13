from ode import *
import numpy as np

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
        self.hist = {pop.label: list() for pop in populacoes}

    def get_S(self):
        return sum(pop.S for pop in self.populacoes)

    def get_I(self):
        return sum(pop.I for pop in self.populacoes)

    def get_R(self):
        return sum(pop.R for pop in self.populacoes)

    def simulate(self):
        
        I_total = self.get_I()
        for pop in self.populacoes:
            _yk = [pop.S,pop.I,pop.R,I_total]
            pop.S,pop.I,pop.R,_ = rk4(ode_system,_yk,pop.params)
            self.hist[pop.label].append([pop.S,pop.I,pop.R])

    def __str__(self):
        string = f'id: {self.id}\nvizinhos: {self.id}'
        for pop in self.populacoes:
            string += str(pop)
        return string