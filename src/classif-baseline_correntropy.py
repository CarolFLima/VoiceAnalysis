import random
import scipy.io as sio
import numpy as np
import pickle

"""
    Distancia entre os sinais utilizados na detecção 
    de patologias da voz
    @author Caroline Lima
"""

# Carregando as celulas .mat como arrays do scipy
mat_contents = sio.loadmat('../data/edema.mat')
cells_Ed = mat_contents['Y_normalizado_E']

mat_contents = sio.loadmat('../data/nodulo.mat')
cells_Nd = mat_contents['Y_normalizado_Nd']

mat_contents = sio.loadmat('../data/normal.mat')
cells_N = mat_contents['Y_normalizado_N']

mat_contents = sio.loadmat('../data/paralisia.mat')
cells_P = mat_contents['Y_normalizado_P']

#Configuração da conrrentropia
sigma = 1

# Sinais de controle
tam_amostra = 5
TAM_P = 52
TAM_N = 53
TAM_ND = 18
TAM_ED = 43

rand_val_P = [35, 36, 5, 16, 32]
rand_val_Ed = [9, 41, 17, 23, 16]
rand_val_Nd = [0, 7, 12, 9, 13]
rand_val_N = [11, 45, 47, 15, 37]

tam_janela = 12500
janela = []
similar = []
simi1 = np.zeros((10, tam_amostra*4))
simi_jc = np.zeros((TAM_N-tam_amostra, tam_amostra*4))

# Juntar todos os sinais de controle em um array
cells_controle = []
for x in cells_P[0, rand_val_P]:
    cells_controle.append(x)
for x in cells_Ed[0, rand_val_Ed]:
    cells_controle.append(x)
for x in cells_Nd[0, rand_val_Nd]:
    cells_controle.append(x)
for x in cells_N[0, rand_val_N]:
    cells_controle.append(x)

# Remover sinais de controle das matrizes originais
testes_P = np.delete(cells_P[0], rand_val_P)
testes_Ed = np.delete(cells_Ed[0], rand_val_Ed)
testes_Nd = np.delete(cells_Nd[0], rand_val_Nd)
testes_N = np.delete(cells_N[0], rand_val_N)

for i, amostra1 in enumerate(testes_N):
    print(i)
    inicio_janela = random.sample(range(0, len(amostra1)-tam_janela-1), 10)
    for j in range(10):
        janela = amostra1[inicio_janela[j]:inicio_janela[j]+tam_janela]
        for k, amostra2 in enumerate(cells_controle):
            similar.clear()
            for inicio in range(0, len(amostra2)-tam_janela):
                padrao = amostra2[inicio:inicio+tam_janela]
                diferenca = janela - amostra2[inicio:inicio + tam_janela]
                # Correntropia calculada aqui
                correntropia = (1/(np.sqrt(2*np.pi)*sigma*tam_janela))*np.sum(np.exp(-np.square(diferenca)/(2*np.square(sigma))))
                similar.append(correntropia)
            simi1[j, k] = max(similar)
    simi_jc[i, :] = np.amax(simi1, axis=0)

pickle.dump(simi_jc, open('../Files/simi_NS1.obj', 'wb'))
# pickle.dump(janela, open('../Files/janela.obj', 'wb'))
