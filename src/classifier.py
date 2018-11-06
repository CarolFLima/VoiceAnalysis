import numpy as np
import pickle
import random
import logging
from src import test
from tpot import TPOTClassifier
import pandas as pd
from sklearn.model_selection import train_test_split

parP = pickle.load(open('../MinSqFiles/L3/parametroP.obj', 'rb'))
parN = pickle.load(open('../MinSqFiles/L3/parametroN.obj', 'rb'))
parNd = pickle.load(open('../MinSqFiles/L3/parametroNd.obj', 'rb'))
parEd = pickle.load(open('../MinSqFiles/L3/parametroEd.obj', 'rb'))

logging.basicConfig(filename='../MinSqFiles/L3/random.log', level=logging.DEBUG)

################ CLASSIFICACAO COM O TPOT

par1 = []
par2 = []
par3 = []
par4 = []
par5 = []
par6 = []
par7 = []
par8 = []
par9 = []

classe = []

for i in range(len(parNd)):
    par1.append(parNd[i][0])
    par2.append(parNd[i][1])
    par3.append(parNd[i][2])
    par4.append(parNd[i][3])
    par5.append(parNd[i][4])
    par6.append(parNd[i][5])
    par7.append(parNd[i][6])
    par8.append(parNd[i][7])
    par9.append(parNd[i][8])
    classe.append(0)
for i in range(len(parP)):
    par1.append(parP[i][0])
    par2.append(parP[i][1])
    par3.append(parP[i][2])
    par4.append(parP[i][3])
    par5.append(parP[i][4])
    par6.append(parP[i][5])
    par7.append(parP[i][6])
    par8.append(parP[i][7])
    par9.append(parP[i][8])
    classe.append(1)
for i in range(len(parN)):
    par1.append(parN[i][0])
    par2.append(parN[i][1])
    par3.append(parN[i][2])
    par4.append(parN[i][3])
    par5.append(parN[i][4])
    par6.append(parN[i][5])
    par7.append(parN[i][6])
    par8.append(parN[i][7])
    par9.append(parN[i][8])
    classe.append(2)
for i in range(len(parEd)):
    par1.append(parEd[i][0])
    par2.append(parEd[i][1])
    par3.append(parEd[i][2])
    par4.append(parEd[i][3])
    par5.append(parEd[i][4])
    par6.append(parEd[i][5])
    par7.append(parEd[i][6])
    par8.append(parEd[i][7])
    par9.append(parEd[i][8])
    classe.append(3)

print(len(parN))
print(len(parNd))
print(len(parEd))
print(len(parP))
#
# # data = {'par1': par1, 'par2': par2, 'target': classe}
# # data = {'par1': par1, 'par2': par2, 'par3':par3, 'par4':par4, 'par5':par5,'target': classe}
# data = {'par1': par1, 'par2': par2, 'par3':par3, 'par4':par4, 'par5':par5, 'par6':par6, 'par7':par7,
#         'par8':par8, 'par9':par9,'target': classe}
# df = pd.DataFrame(data=data)
#
# # df[['par1', 'par2']] = df[['par1', 'par2']].astype(np.float)
# # df[['par1', 'par2', 'par3', 'par4', 'par5']] = \
# #     df[['par1', 'par2', 'par3', 'par4', 'par5']].astype(np.float)
# df[['par1', 'par2', 'par3', 'par4', 'par5', 'par6', 'par7', 'par8', 'par9']] = \
#     df[['par1', 'par2', 'par3', 'par4', 'par5', 'par6', 'par7', 'par8', 'par9']].astype(np.float)
#
# # df.to_csv("../data/dfL1.csv")
#
# # X_train, X_test, y_train, y_test = \
# #     train_test_split(df[['par1', 'par2', 'par3', 'par4', 'par5', 'par6', 'par7', 'par8', 'par9']].values,
# #                      df[['class']].values, test_size=0.3)
# #
#
#
# # print(df.info())
# #
# # tpot = TPOTClassifier(verbosity=2)
# # tpot.fit(X_train, y_train)
# # print(tpot.score(X_test, y_test))
# # tpot.export('tpot_classif_pipelinel3.py')
#
# ########### CLASSIFICACAO A PARTIR DAS DISTANCIAS
# # rand_val_P = [35, 36, 5, 16, 32]
# # rand_val_Ed = [9, 41, 17, 23, 16]
# # rand_val_Nd = [0, 7, 12, 9, 13]
# # rand_val_N = [11, 45, 47, 15, 37]
#
# # [47, 11, 1, 38]
# # diagonal_maior = [45, 16, 2, 28]
# diagonal_maior = [20, 11, 2, 20]
# diagonal_atual = [0, 0, 0, 0]
# cells_controle = []
#
# for i in range(10000):
#     rand_val_P = random.sample(range(52), 5)
#     rand_val_Ed = random.sample(range(43), 5)
#     rand_val_Nd = random.sample(range(18), 5)
#     rand_val_N = random.sample(range(53), 5)
#
#     # Sinais de controle
#     del cells_controle
#     cells_controle = []
#     for x in rand_val_P:
#         cells_controle.append(parP[x])
#     for x in rand_val_Ed:
#         cells_controle.append(parEd[x])
#     for x in rand_val_Nd:
#         cells_controle.append(parNd[x])
#     for x in rand_val_N:
#         cells_controle.append(parN[x])
#
#     # Sinais teste
#     parP_reduzida = [i for j, i in enumerate(parP) if j not in rand_val_P]
#     parN_reduzida = [i for j, i in enumerate(parN) if j not in rand_val_N]
#     parNd_reduzida = [i for j, i in enumerate(parNd) if j not in rand_val_Nd]
#     parEd_reduzida = [i for j, i in enumerate(parEd) if j not in rand_val_Ed]
#
#     ## Paralisia
#     dist = []
#     dist_P = np.zeros((47, 20))
#     for j, parametro in enumerate(parP_reduzida):
#         dist.clear()
#         for parametro2 in cells_controle:
#             diferenca = np.subtract(parametro[1:], parametro2[1:])
#             d = np.sqrt(np.sum(np.square(diferenca)))
#             dist.append(d)
#         dist_P[j, :] = dist
#
#     ## Normal
#     dist_N = np.zeros((48, 20))
#     for j, parametro in enumerate(parN_reduzida):
#         dist.clear()
#         for parametro2 in cells_controle:
#             diferenca = np.subtract(parametro[1:], parametro2[1:])
#             d = np.sqrt(np.sum(np.square(diferenca)))
#             dist.append(d)
#         dist_N[j, :] = dist
#
#     ## Edema
#     dist_Ed = np.zeros((38, 20))
#     for j, parametro in enumerate(parEd_reduzida):
#         dist.clear()
#         for parametro2 in cells_controle:
#             diferenca = np.subtract(parametro[1:], parametro2[1:])
#             d = np.sqrt(np.sum(np.square(diferenca)))
#             dist.append(d)
#         dist_Ed[j, :] = dist
#
#     ## Nodulo
#     dist_Nd = np.zeros((13, 20))
#     for j, parametro in enumerate(parNd_reduzida):
#         dist.clear()
#         for parametro2 in cells_controle:
#             diferenca = np.subtract(parametro[1:], parametro2[1:])
#             d = np.sqrt(np.sum(np.square(diferenca)))
#             dist.append(d)
#         dist_Nd[j, :] = dist
#
#     conf = test.gerar_matriz_conf(dist_N, dist_Nd, dist_Ed, dist_P)
#     diagonal_atual = [conf[0, 0], conf[1, 1], conf[2, 2], conf[3, 3]]
#     if np.sum(diagonal_atual) > np.sum(diagonal_maior):
#         diagonal_maior = diagonal_atual
#         print(conf)
#         # Salva no .log
#         logging.debug('Esse random P ' + str(rand_val_P))
#         logging.debug('Esse random N ' + str(rand_val_N))
#         logging.debug('Esse random Nd ' + str(rand_val_Nd))
#         logging.debug('Esse random Ed ' + str(rand_val_Ed))
#         logging.debug('Obteve essa matriz\n ' + str(conf))
#         # Salva as variaveis no .obj
#         # pickle.dump(dist_Nd, open('../MinSqFiles/L3/dist/distNd.obj', 'wb'))
#         # pickle.dump(dist_Ed, open('../MinSqFiles/L3/dist/distEd.obj', 'wb'))
#         # pickle.dump(dist_N, open('../MinSqFiles/L3/dist/distN.obj', 'wb'))
#         # pickle.dump(dist_P, open('../MinSqFiles/L3/dist/distP.obj', 'wb'))
