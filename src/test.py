import pickle
from sklearn.metrics import confusion_matrix
import numpy as np
import scipy.io as sio

# Gerar distâncias entre os sinais de controle
# dist = pickle.load(open('../Files/DistControle/dist_N.obj', 'rb'))
# print(dist.shape)
# print(np.amin(dist))
#
# print(dist[:, 15:20])

# Classificar sinais de controle
dist_N = pickle.load(open('../Files/dist_N.obj', 'rb'))
dist_Nd = pickle.load(open('../Files/dist_Nd.obj', 'rb'))
dist_Ed = pickle.load(open('../Files/dist_Ed.obj', 'rb'))
dist_P = pickle.load(open('../Files/dist_p.obj', 'rb'))
print(dist_N.shape)

dist = []
saida_original = ["paralisia", "paralisia", "paralisia", "paralisia", "paralisia",
                  "edema", "edema", "edema", "edema", "edema",
                  "nodulo", "nodulo", "nodulo", "nodulo", "nodulo",
                  "normal", "normal", "normal", "normal", "normal"]
saida_class = []
for i in range(20):
    dist.append(np.amin(dist_P[:, i]))
    dist.append(np.amin(dist_Ed[:, i]))
    dist.append(np.amin(dist_Nd[:, i]))
    dist.append(np.amin(dist_N[:, i]))

    a = dist.index(np.amin(dist))
    print(a)
    if a == 0:
        saida_class.append("paralisia")
    elif a == 1:
        saida_class.append("edema")
    elif a == 2:
        saida_class.append("nodulo")
    elif a == 3:
        saida_class.append("normal")

    dist.clear()

conf = confusion_matrix(saida_original, saida_class, labels=["paralisia", "edema", "nodulo", "normal"])
print(conf)
