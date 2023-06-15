from populacao import Populacao
from regiao import Regiao
from rede import Rede
from ode import *
import matplotlib.pyplot as plt
import osmnx as ox


adulto_config = {  
    "label": "adulto",
    "params": {  
        "tx_mortalidade": 0.1,
        "tx_mobilidade": 0.5,
        "tx_infeccao": 0.2,
        "tx_nascimento": 0.,
        "tx_recuperacao": 0.1},
    "S": 100,
    "I": 100,
    "R": 100,
}

idoso_config = {  
    "label": "idoso",
    "params": {  
        "tx_mortalidade": 0.1,
        "tx_mobilidade": 0.1,
        "tx_infeccao": 0.1,
        "tx_nascimento": 0,
        "tx_recuperacao": 0.2},
    "S": 100,
    "I": 100,
    "R": 100,
}

adulto = Populacao(**adulto_config)
idoso = Populacao(**idoso_config)
regiao = Regiao(1,[adulto,idoso],[3,2])

time = 100

# for i in range(time):
#     regiao.simulate_edo()

print(regiao.simulate_move())

# regiao.plot()

# G = ox.graph_from_place("São João del Rei, Minas Gerais, Brazil", network_type="drive")


# print(Rede(G,[adulto,idoso]))