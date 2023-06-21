import sys
import yaml
import osmnx as ox
from tqdm import tqdm
from src.rede import Rede
from src.populacao import Populacao

if __name__ == '__main__':
    
    with open(sys.argv[1], "r") as f:
            params = yaml.safe_load(f)

    populacoes = {k: Populacao(**v) for k,v in params['populacao'].items()}    
    
    G = ox.graph_from_place(params['config']['place'], network_type="drive")

    rede = Rede(G,populacoes)

    for i in tqdm(range(params['config']['steps'])):
        rede.run_edo()
        rede.move()

    rede.plot_edo()