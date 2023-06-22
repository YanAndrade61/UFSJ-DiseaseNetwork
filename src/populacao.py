from src.params import Params
import numpy as np

class Populacao:
    """
    Representa uma população em um modelo de simulação.

    Atributos:
    - label (str): O rótulo da população.
    - params (dict): Os parâmetros da simulação.
    - S (int): O número de indivíduos suscetíveis na população.
    - I (int): O número de indivíduos infectados na população.
    - R (int): O número de indivíduos recuperados na população.
    """

    def __init__(self, label: str, params: dict, S: list, I: list, R: list):
        self.label = label
        self.params = Params(**params)
        self.S = S
        self.I = I
        self.R = R

        # self.S = np.random.randint(S[0],S[1])
        # self.I = np.random.randint(I[0],I[1])
        # self.R = np.random.randint(R[0],R[1])

    def __str__(self) -> str:
        string = f'''\nPopulacao:
    Label: {self.label}
    S: {self.S}
    I: {self.I}
    R: {self.R}
    {self.params}'''
        return string