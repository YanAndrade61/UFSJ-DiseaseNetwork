from populacao import Populacao
from regiao import Regiao
from ode import *

adulto_config = {  
    "label": "adulto",
    "params": {  
        "tx_mortalidade": 0,
        "tx_mobilidade": 0,
        "tx_infeccao": 0.1,
        "tx_nascimento": 0,
        "tx_recuperacao": 0.2},
    "S": 100,
    "I": 100,
    "R": 100,
}

idoso_config = {  
    "label": "idoso",
    "params": {  
        "tx_mortalidade": 0,
        "tx_mobilidade": 0,
        "tx_infeccao": 0.1,
        "tx_nascimento": 0,
        "tx_recuperacao": 0.2},
    "S": 100,
    "I": 100,
    "R": 100,
}

adulto = Populacao(**adulto_config)
idoso = Populacao(**idoso_config)
regiao = Regiao(1,[adulto,idoso],[1,2])

_yk = [adulto.S,adulto.I,adulto.R,100]

print(rk4(ode_system,_yk,adulto.params))