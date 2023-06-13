from populacao import Populacao
from regiao import Regiao
from ode import *
import matplotlib.pyplot as plt

adulto_config = {  
    "label": "adulto",
    "params": {  
        "tx_mortalidade": 0.1,
        "tx_mobilidade": 0,
        "tx_infeccao": 0.1,
        "tx_nascimento": 0.1,
        "tx_recuperacao": 0.2},
    "S": 100,
    "I": 100,
    "R": 100,
}

idoso_config = {  
    "label": "idoso",
    "params": {  
        "tx_mortalidade": 0.1,
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

time = 10

for i in range(time):
    regiao.simulate()
print(regiao.hist)


fig, ax = plt.subplots()
ax.set(xlabel='time (days)', ylabel='[Y]', title='adulto')
ax.plot(range(time), regiao.hist['adulto'])
plt.legend(['S','I','R'], loc='best')
ax.grid()
fig.savefig('simulation')
plt.show()