import random
import scipy.io as sio
import numpy as np
import pickle
"""
    Calcula a distancia entre os sinais do grupo de controle
"""

mat_contents = sio.loadmat('../data/edema.mat')
cells_Ed = mat_contents['Y_normalizado_E']

mat_contents = sio.loadmat('../data/nodulo.mat')
cells_Nd = mat_contents['Y_normalizado_Nd']

mat_contents = sio.loadmat('../data/normal.mat')
cells_N = mat_contents['Y_normalizado_N']

mat_contents = sio.loadmat('../data/paralisia.mat')
cells_P = mat_contents['Y_normalizado_P']

rand_val_P = [35, 36, 5, 16, 32]
rand_val_Ed = [9, 41, 17, 23, 16]
rand_val_Nd = [0, 7, 12, 9, 13]
rand_val_N = [11, 45, 47, 15, 37]

tam_janela = 12500
tam_amostra = 5
janela = []
dist = []
dist1 = np.zeros((10, tam_amostra*4))
dist_jc = np.zeros((tam_amostra, tam_amostra*4))

# Sinais de controle
cells_controle = []
for x in cells_P[0, rand_val_P]:
    cells_controle.append(x)
for x in cells_Ed[0, rand_val_Ed]:
    cells_controle.append(x)
for x in cells_Nd[0, rand_val_Nd]:
    cells_controle.append(x)
for x in cells_N[0, rand_val_N]:
    cells_controle.append(x)

# Convolução
for i, amostra1 in enumerate(cells_Nd[0, rand_val_Nd]):
    inicio_janela = random.sample(range(0, len(amostra1)-tam_janela-1), 10)
    for j in range(10):
        janela = amostra1[inicio_janela[j]:inicio_janela[j]+tam_janela]
        for k, amostra2 in enumerate(cells_controle):
            dist.clear()
            for inicio in range(0, len(amostra2)-tam_janela):
                padrao = amostra2[inicio:inicio+tam_janela]
                diferenca = janela - amostra2[inicio:inicio + tam_janela]
                # Distancia euclidiana calculada aqui
                dist_euclidiana = np.sqrt(np.sum(np.square(diferenca)))
                dist.append(dist_euclidiana)
            dist1[j, k] = min(dist)
    dist_jc[i, :] = np.amin(dist1, axis=0)

pickle.dump(dist_jc, open('../Files/DistControle/dist_Nd.obj', 'wb'))
