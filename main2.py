import sys
import yaml
import os
import imageio
import osmnx as ox
import numpy as np
from tqdm import tqdm
from src.rede import Rede
from src.populacao import Populacao

if __name__ == '__main__':
    
    with open(sys.argv[1], "r") as f:
            params = yaml.safe_load(f)

    # populacoes = {k: Populacao(**v) for k,v in params['populacao'].items()}    
    populacoes = []
    
    G = ox.graph_from_place(params['config']['place'], network_type="drive")
    S = np.loadtxt('S',delimiter=',')
    I = np.loadtxt('I',delimiter=',')
    aux = {
         'adulto':{'S':S[0],'I':I[0]},
         'idoso':{'S':S[1],'I':I[1]},
         'crianca':{'S':S[2],'I':I[2]}
    }
    for i in range(len(G.nodes)):
        d = {}
        for k,v in params['populacao'].items():
            v['S'] = aux[k]['S'][i]
            v['I'] = aux[k]['I'][i]
            v['R'] = 0
            d[k] = Populacao(**v)
        populacoes.append(d)
    # print(populacoes)    

    rede = Rede(G,populacoes)

    for i in tqdm(range(params['config']['steps'])):
        rede.run_edo()
        rede.move()

    rede.plot_edo()

    # Create gif
    imagens = []
    path = 'gif'
    nome_arquivos = [f'img{c}.png' for c in range(1, len(os.listdir(path))+1)]

    for i in nome_arquivos:
        imagens.append(imageio.imread(os.path.join(path, i)))
        
    imageio.mimsave('params.gif', imagens, duration=0.1)
    

