class Params:
    """
    Representa um conjunto de parâmetros no modelo de simulação.

    Atributos:
    - tx_mortalidade (float): A taxa de mortalidade do indivíduo.
    - tx_mobilidade (float): A taxa de mobilidade do indivíduo.
    - tx_infeccao (float): A taxa de infecção do indivíduo.
    - tx_nascimento (float): A taxa de nascimento do indivíduo.
    - tx_recuperacao (float): A taxa de recuperação do indivíduo.
    """

    def __init__(self, tx_mortalidade, tx_mobilidade, tx_infeccao, tx_nascimento, tx_recuperacao):
        self.tx_mortalidade = tx_mortalidade
        self.tx_mobilidade = tx_mobilidade
        self.tx_infeccao = tx_infeccao
        self.tx_nascimento = tx_nascimento
        self.tx_recuperacao = tx_recuperacao

    def __str__(self):
        string = f'''Params:
        Mortalidade: {self.tx_mortalidade}
        Mobilidade: {self.tx_mobilidade}
        Infeccao: {self.tx_infeccao}
        Nascimento: {self.tx_nascimento}
        Recuperacao: {self.tx_recuperacao}'''
        return string