from populacao import Populacao
from regiao import Regiao

adulto_config = {  
    "label": "adulto",
    "params": {  
        "tx_mortalidade": 0,
        "tx_mobilidade": 0,
        "tx_infeccao": 0,
        "tx_nascimento": 0,
        "tx_recuperacao": 0},
    "S": 100,
    "I": 100,
    "R": 100,
}

idoso_config = {  
    "label": "adulto",
    "params": {  
        "tx_mortalidade": 0,
        "tx_mobilidade": 0,
        "tx_infeccao": 0,
        "tx_nascimento": 0,
        "tx_recuperacao": 0},
    "S": 100,
    "I": 100,
    "R": 100,
}

adulto = Populacao(**adulto_config)
idoso = Populacao(**idoso_config)
regiao = Regiao(1,[adulto,idoso],[1,2])

print(regiao)