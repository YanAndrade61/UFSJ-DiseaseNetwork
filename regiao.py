from ode import rk4
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
        """
        Inicializa uma região com um identificador, uma lista de populações e uma lista de regiões vizinhas.

        Args:
        - id (int): O identificador da região.
        - populacoes (list): Lista de populações na região.
        - vizinhos (list): Lista de regiões vizinhas.
        """
        self.id = id
        self.populacoes = populacoes
        self.vizinhos = vizinhos
        self.hist = {pop.label: [] for pop in populacoes}
        self.steps = 0

    def get_S(self):
        """
        Retorna a soma dos valores S de todas as populações na região.

        Returns:
        A soma dos valores S de todas as populações.
        """
        return sum(pop.S for pop in self.populacoes)

    def get_I(self):
        """
        Retorna a soma dos valores I de todas as populações na região.

        Returns:
        A soma dos valores I de todas as populações.
        """
        return sum(pop.I for pop in self.populacoes)

    def get_R(self):
        """
        Retorna a soma dos valores R de todas as populações na região.

        Returns:
        A soma dos valores R de todas as populações.
        """
        return sum(pop.R for pop in self.populacoes)
    
    def get_SIR(self):
        """
        Retorna a soma dos valores S + I + R de todas as populações na região.

        Returns:
        A soma dos valores S + I + R de todas as populações.
        """
        return sum(pop.S + pop.I + pop.R for pop in self.populacoes)

    def simulate_edo(self):
        """
        Realiza uma simulação usando o método de resolução de equações diferenciais (EDO).

        A função de simulação atualiza os valores S, I e R para cada população na região
        com base nos parâmetros e nas equações diferenciais definidas no módulo 'ode'.

        O resultado da simulação é armazenado no atributo 'hist' da região.
        """
        I_norm = self.get_I() / self.get_SIR()
        for pop in self.populacoes:
            _yk = [pop.S, pop.I, pop.R, I_norm]
            pop.S, pop.I, pop.R, _ = rk4(ode_system, _yk, pop.params)
            self.hist[pop.label].append([pop.S, pop.I, pop.R])

        self.steps += 1

    def plot(self):
        """
        Gera um gráfico da simulação das populações na região.

        O gráfico mostra a variação dos valores S, I e R ao longo do tempo para cada população.
        """
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
                """
        Retorna uma representação em string da região.

        Returns:
        Uma string representando a região.
        """
        string = f'\nid: {self.id}\nvizinhos: {self.vizinhos}'
        string += ''.join(str(pop) for pop in self.populacoes)
        return string
