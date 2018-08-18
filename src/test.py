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

# saida_original = ["paralisia", "paralisia", "paralisia", "paralisia", "paralisia",
#                   "edema", "edema", "edema", "edema", "edema",
#                   "nodulo", "nodulo", "nodulo", "nodulo", "nodulo",
#                   "normal", "normal", "normal", "normal", "normal"]

saida_original = []
saida_class = []

for i in range(len(dist_P[:, 0])):
    saida_original.append("paralisia")
for i in range(len(dist_Ed[:, 0])):
    saida_original.append("edema")
for i in range(len(dist_Nd[:, 0])):
    saida_original.append("nodulo")
for i in range(len(dist_N[:, 0])):
    saida_original.append("normal")

for i in range(len(dist_P[:, 0])):
    a = dist_P[i, :].tolist().index(np.amin(dist_P[i, :]))
    if a < 5:
        saida_class.append("paralisia")
    elif (a > 4) and (a < 9):
        saida_class.append("edema")
    elif (a > 9) and (a < 15):
        saida_class.append("nodulo")
    elif (a > 14) and (a < 20):
        saida_class.append("normal")

for i in range(len(dist_Ed[:, 0])):
    a = dist_Ed[i, :].tolist().index(np.amin(dist_Ed[i, :]))
    if a < 5:
        saida_class.append("paralisia")
    elif (a > 4) and (a < 9):
        saida_class.append("edema")
    elif (a > 9) and (a < 15):
        saida_class.append("nodulo")
    elif (a > 14) and (a < 20):
        saida_class.append("normal")

for i in range(len(dist_Nd[:, 0])):
    a = dist_Nd[i, :].tolist().index(np.amin(dist_Nd[i, :]))
    if a < 5:
        saida_class.append("paralisia")
    elif (a > 4) and (a < 9):
        saida_class.append("edema")
    elif (a > 9) and (a < 15):
        saida_class.append("nodulo")
    elif (a > 14) and (a < 20):
        saida_class.append("normal")

for i in range(len(dist_N[:, 0])):
    a = dist_N[i, :].tolist().index(np.amin(dist_N[i, :]))
    if a < 5:
        saida_class.append("paralisia")
    elif (a > 4) and (a < 9):
        saida_class.append("edema")
    elif (a > 9) and (a < 15):
        saida_class.append("nodulo")
    elif (a > 14) and (a < 20):
        saida_class.append("normal")

conf = confusion_matrix(saida_original, saida_class, labels=["normal", "edema", "nodulo", "paralisia"])
print(conf)
