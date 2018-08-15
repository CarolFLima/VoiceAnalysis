import random
import scipy.io as sio
import numpy as np
import pickle
from sklearn.metrics import mean_squared_error

"""
    Distancia entre os sinais utilizados na detecção 
    de patologias da voz
    @author Caroline Lima
"""

# Carregando as celulas .mat como arrays do scipy
mat_contents = sio.loadmat('../data/edema.mat')
cells_E = mat_contents['Y_normalizado_E']

mat_contents = sio.loadmat('../data/nodulo.mat')
cells_Nd = mat_contents['Y_normalizado_Nd']

mat_contents = sio.loadmat('../data/normal.mat')
cells_N = mat_contents['Y_normalizado_N']

mat_contents = sio.loadmat('../data/paralisia.mat')
cells_P = mat_contents['Y_normalizado_P']

# Sinais de controle
tam_amostra = 5
rand_val = random.sample(range(0, len(cells_N[0])-1), tam_amostra)

tam_janela = 12500
janela = []
dist = []
dist1 = np.zeros((10, 5))
dist_jc = np.zeros((52, 5))

for i, amostra1 in enumerate(cells_P[0]):
    inicio_janela = random.sample(range(0, len(amostra1)-tam_janela-1), 10)
    print(type(janela))
    for j in range(10):
        janela = amostra1[inicio_janela[j]:inicio_janela[j]+tam_janela]
        for k, amostra2 in enumerate(cells_N[0, rand_val]):
            dist.clear()
            for inicio in range(0, len(amostra2)-tam_janela, 10):
                padrao = amostra2[inicio:inicio+tam_janela]
                diferenca = janela - amostra2[inicio:inicio + tam_janela]
                # Distancia euclidiana calculada aqui
                dist_euclidiana = np.sqrt(np.sum(np.square(diferenca)))
                dist.append(dist_euclidiana)
            dist1[j, k] = min(dist)
    dist_jc[i, :] = np.amin(dist1, axis=0)

pickle.dump(dist_jc, open('../Files/dist_N_P.obj', 'wb'))
# pickle.dump(janela, open('../Files/janela.obj', 'wb'))
