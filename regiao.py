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

    def get_S(self):
        return sum(pop.S for pop in self.populacoes)

    def get_I(self):
        return sum(pop.I for pop in self.populacoes)

    def get_R(self):
        return sum(pop.R for pop in self.populacoes)
