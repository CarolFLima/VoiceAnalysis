import random
import scipy.io as sio
import numpy as np
import pickle


"""
    Distancia entre os sinais utilizados na detecção 
    de patologias da voz
    @author Caroline Lima
"""
mat_contents = sio.loadmat('../data/edema.mat')
cells_E = mat_contents['Y_normalizado_E']

mat_contents = sio.loadmat('../data/nodulo.mat')
cells_Nd = mat_contents['Y_normalizado_Nd']

mat_contents = sio.loadmat('../data/normal.mat')
cells_N = mat_contents['Y_normalizado_N']

mat_contents = sio.loadmat('../data/paralisia.mat')
cells_P = mat_contents['Y_normalizado_P']

# Sinais de controle
control_sample_size = 5
rand_val = random.sample(range(0, len(cells_N[0])-1),  control_sample_size)

print(rand_val)
tam_janela = 2000

dist = []
dist_N_Nd = []
for sample1 in cells_N[0, rand_val]:
    for i, sample2 in enumerate(cells_Nd[0]):
        for j in range(0, len(sample1)-tam_janela, tam_janela):
            for k in range(0, len(sample2)-tam_janela, tam_janela):
                dist.append(np.square(np.subtract(sample1[j:j + tam_janela],sample2[k:k + tam_janela])).mean())
            dist_N_Nd.append(min(dist))
            dist.clear()

print(len(dist_N_Nd))
print("Media %f" % np.mean(dist_N_Nd))
pickle.dump(dist_N_Nd, open('../Files/dist_N_Nd.obj', 'wb'))


dist_N_E = []
for sample1 in cells_N[0, rand_val]:
    for i, sample2 in enumerate(cells_E[0]):
        for j in range(0, len(sample1)-tam_janela, tam_janela):
            for k in range(0, len(sample2)-tam_janela, tam_janela):
                dist.append(np.square(np.subtract(sample1[j:j + tam_janela],sample2[k:k + tam_janela])).mean())
            dist_N_E.append(min(dist))
            dist.clear()

print(len(dist_N_E))
print("Media %f" % np.mean(dist_N_E))
pickle.dump(dist_N_E, open('../Files/dist_N_E.obj', 'wb'))

dist_N_N = []
for sample1 in cells_N[0, rand_val]:
    for i, sample2 in enumerate(cells_N[0]):
        if not (i in rand_val):
            for j in range(0, len(sample1)-tam_janela, tam_janela):
                for k in range(0, len(sample2)-tam_janela, tam_janela):
                    dist.append(np.square(np.subtract(sample1[j:j + tam_janela],sample2[k:k + tam_janela])).mean())
                dist_N_N.append(min(dist))
                dist.clear()

print(len(dist_N_N))
print("Media %f" % np.mean(dist_N_N))
pickle.dump(dist_N_N, open('../Files/dist_N_N.obj', 'wb'))

dist_N_P = []
for sample1 in cells_N[0, rand_val]:
    for i, sample2 in enumerate(cells_P[0]):
        if not (i in rand_val):
            for j in range(0, len(sample1)-tam_janela, tam_janela):
                for k in range(0, len(sample2)-tam_janela, tam_janela):
                    dist.append(np.square(np.subtract(sample1[j:j + tam_janela],sample2[k:k + tam_janela])).mean())
                dist_N_P.append(min(dist))
                dist.clear()

print(len(dist_N_P))
print("Media %f" % np.mean(dist_N_P))
pickle.dump(dist_N_P, open('../Files/dist_N_P.obj', 'wb'))