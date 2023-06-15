from populacao import Populacao
from regiao import Regiao
from rede import Rede
from ode import *
import matplotlib.pyplot as plt
import osmnx as ox


adulto_config = {  
    "label": "adulto",
    "params": {  
        "tx_mortalidade": 0.01,
        "tx_mobilidade": 0.5,
        "tx_infeccao": 0.5,
        "tx_nascimento": 0.01,
        "tx_recuperacao": 0.01},
    "S": 100,
    "I": 80,
    "R": 0,
}

idoso_config = {  
    "label": "idoso",
    "params": {  
        "tx_mortalidade": 0.1,
        "tx_mobilidade": 0.1,
        "tx_infeccao": 0.2,
        "tx_nascimento": 0,
        "tx_recuperacao": 0.01},
    "S": 100,
    "I": 50,
    "R": 0,
}


adulto = Populacao(**adulto_config)
idoso = Populacao(**idoso_config)


d = {adulto.label: adulto}
regiao = Regiao(1,d,[3,2])

G = ox.graph_from_place("São João del Rei, Minas Gerais, Brazil", network_type="drive")

x = Rede(G,d)

for i in range(100):
    x.simulate()
    x.move()
