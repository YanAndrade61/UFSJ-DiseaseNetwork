from params import Params

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

    def __init__(self, label: str, params: dict, S: int, I: int, R: int):
        self.label = label
        self.params = Params(**params)
        self.S = S
        self.I = I
        self.R = R

    def __str__(self) -> str:
        string = f'Label: {self.label}\nS: {self.S}\nI: {self.I}\nR: {self.R}\n{self.params}'
        return string