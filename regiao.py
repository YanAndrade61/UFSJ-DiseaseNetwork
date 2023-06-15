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

    def __init__(self, id: int, populacoes: dict, vizinhos: list):
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
        self.hist = {pop: [] for pop in populacoes}
        self.steps = 0

    def get_S(self):
        """
        Retorna a soma dos valores S de todas as populações na região.

        Returns:
        A soma dos valores S de todas as populações.
        """
        return sum(pop.S for pop in self.populacoes.values())

    def get_I(self):
        """
        Retorna a soma dos valores I de todas as populações na região.

        Returns:
        A soma dos valores I de todas as populações.
        """
        return sum(pop.I for pop in self.populacoes.values())

    def get_R(self):
        """
        Retorna a soma dos valores R de todas as populações na região.

        Returns:
        A soma dos valores R de todas as populações.
        """
        return sum(pop.R for pop in self.populacoes.values())
    
    def get_SIR(self):
        """
        Retorna a soma dos valores S + I + R de todas as populações na região
        e qual porção representa a maior parte da população.

        Returns:
        tuple: Uma tupla contendo a categoria ('S', 'I' ou 'R') que representa a
        maior parte da população e a soma dos valores S + I + R de todas as populações.
        """
        S = self.get_S()
        I = self.get_I()
        R = self.get_R()

        max_category = max(('S', S), ('I', I), ('R', R), key=lambda x: x[1])
        total = S + I + R

        return max_category[0], total

        

    def simulate_edo(self):
        """
        Realiza uma simulação usando o método de resolução de equações diferenciais (EDO).

        A função de simulação atualiza os valores S, I e R para cada população na região
        com base nos parâmetros e nas equações diferenciais definidas no módulo 'ode'.

        O resultado da simulação é armazenado no atributo 'hist' da região.
        """
        I_norm = self.get_I() / self.get_SIR()[1]
        for pop in self.populacoes.values():
            _yk = [pop.S, pop.I, pop.R, I_norm]
            pop.S, pop.I, pop.R, _ = rk4(ode_system, _yk, pop.params)
            self.hist[pop.label].append([pop.S, pop.I, pop.R])

        self.steps += 1
    
    def simulate_move(self):
        """
        Simula os movimentos dos indivíduos entre as regiões vizinhas.

        Retorna um dicionário que representa os movimentos dos indivíduos entre
        as regiões vizinhas. A estrutura do dicionário é a seguinte:

        Retorns:
        move (dict): Dicionário que representa os movimentos dos indivíduos entre
            as regiões vizinhas.
        """
        move = {}
        for pop in self.populacoes.values():
            
            dest = np.random.choice(self.vizinhos)
            prop = round(pop.params.tx_mobilidade/3,2)
            move.setdefault(dest, {}).setdefault(pop.label, {})
            move[dest][pop.label] = {'S':int(pop.S*prop), 'I': int(pop.I*prop), 'R':int(pop.R*prop)}
            pop.S -= int(pop.S*prop)
            pop.I -= int(pop.I*prop)
            pop.R -= int(pop.R*prop)

        return move

    def plot(self):
        """
        Gera um gráfico da simulação das populações na região.

        O gráfico mostra a variação dos valores S, I e R ao longo do tempo para cada população.
        """
        fig, ax = plt.subplots(1, len(self.populacoes), squeeze=False)
        time = np.arange(0, self.steps * 0.01, 0.01)

        for i, pop in enumerate(self.populacoes.values()):
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
        string += ''.join(str(pop) for pop in self.populacoes.values())
        return string
