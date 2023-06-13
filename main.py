from populacao import Populacao

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
adulto = Populacao(**adulto_config)

print(adulto)