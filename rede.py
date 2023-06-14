from regiao import Regiao


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
        self.nodes = {node: Regiao(node, populacoes, list(G.neighbors(node))) for node in G.nodes}

    def __str__(self):
        """
        Retorna uma representação em string da rede.

        Returns:
        Uma string representando as regiões da rede.
        """
        return '\n'.join(str(node) for node in self.nodes.values())
