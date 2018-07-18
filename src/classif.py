import random
import scipy.io as sio
import numpy as np

"""
    Baseline entre os sinais utilizados na detecção 
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
control_sample_size = 4
rand_val = random.sample(range(0, len(cells_N[0])-1),  control_sample_size)


def mse(a, b):
    if len(a) < len(b):
        return np.square(np.subtract(a, b[:len(a)])).mean()
    else:
        return np.square(np.subtract(a[:len(b)], b)).mean()


mse_values_N_N = []
mse_values_N_P = []
mse_values_N_Nd = []
mse_values_N_E = []
for sample in cells_N[0, rand_val]:
    # Normal vs Normal
    for N in cells_N[0]:
        mse_values_N_N.append(mse(sample, N))
    # Normal vs Paralisia
    for P in cells_P[0]:
        mse_values_N_P.append(mse(sample, P))
    # Normal vs Nodulo
    for Nd in cells_Nd[0]:
        mse_values_N_Nd.append(mse(sample, Nd))
    # Normal vs Edema
    for E in cells_E[0]:
        mse_values_N_E.append(mse(sample, E))

mse_values_N_N[:] = (value for value in mse_values_N_N if value != 0)
print("Valores N-N:\n {}".format(mse_values_N_N))
print("Média N-N:\n {}, Max: {}, Min: {}".format(np.mean(mse_values_N_N), max(mse_values_N_N), min(mse_values_N_N)))
print("Valores N-P:\n {}".format(mse_values_N_P))
print("Média N-P:\n {}, Max: {}, Min: {}".format(np.mean(mse_values_N_P), max(mse_values_N_P), min(mse_values_N_P)))
print("Valores N-Nd:\n {}".format(mse_values_N_Nd))
print("Média N-Nd:\n {}, Max: {}, Min: {}".format(np.mean(mse_values_N_Nd), max(mse_values_N_Nd), min(mse_values_N_Nd)))
print("Valores N-E:\n {}".format(mse_values_N_E))
print("Média N-E:\n {}, Max: {}, Min: {}".format(np.mean(mse_values_N_E), max(mse_values_N_E), min(mse_values_N_E)))
