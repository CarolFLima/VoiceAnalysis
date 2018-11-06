import pickle
from sklearn.metrics import confusion_matrix

def gerar_matriz_conf(dist_N, dist_Nd, dist_Ed, dist_P):
    # dist_N = pickle.load(open('../MinSqFiles/L1/dist/distN.obj', 'rb'))
    # dist_Nd = pickle.load(open('../MinSqFiles/L1/dist/distNd.obj', 'rb'))
    # dist_Ed = pickle.load(open('../MinSqFiles/L1/dist/distEd.obj', 'rb'))
    # dist_P = pickle.load(open('../MinSqFiles/L1/dist/distP.obj', 'rb'))

    saida_original = []
    saida_class = []

    for i in range(47):
        saida_original.append("paralisia")
    for i in range(38):
        saida_original.append("edema")
    for i in range(13):
        saida_original.append("nodulo")
    for i in range(48):
        saida_original.append("normal")

    for i in range(len(dist_P)):
        a = dist_P[i].tolist().index(min(dist_P[i]))
        if a < 5:
            saida_class.append("paralisia")
        elif (a > 4) and (a < 10):
            saida_class.append("edema")
        elif (a > 9) and (a < 15):
            saida_class.append("nodulo")
        elif (a > 14) and (a < 20):
            saida_class.append("normal")

    for i in range(len(dist_Ed)):
        a = dist_Ed[i].tolist().index(min(dist_Ed[i]))
        if a < 5:
            saida_class.append("paralisia")
        elif (a > 4) and (a < 10):
            saida_class.append("edema")
        elif (a > 9) and (a < 15):
            saida_class.append("nodulo")
        elif (a > 14) and (a < 20):
            saida_class.append("normal")

    for i in range(len(dist_Nd)):
        a = dist_Nd[i].tolist().index(min(dist_Nd[i]))
        if a < 5:
            saida_class.append("paralisia")
        elif (a > 4) and (a < 10):
            saida_class.append("edema")
        elif (a > 9) and (a < 15):
            saida_class.append("nodulo")
        elif (a > 14) and (a < 20):
            saida_class.append("normal")

    for i in range(len(dist_N)):
        a = dist_N[i].tolist().index(min(dist_N[i]))
        if a < 5:
            saida_class.append("paralisia")
        elif (a > 4) and (a < 10):
            saida_class.append("edema")
        elif (a > 9) and (a < 15):
            saida_class.append("nodulo")
        elif (a > 14) and (a < 20):
            saida_class.append("normal")


    # # conf = confusion_matrix(saida_original, saida_class, labels=["normal", "edema", "nodulo", "paralisia"])
    conf = confusion_matrix(saida_original, saida_class, labels=["normal", "edema", "nodulo", "paralisia"])

    return conf
#
# # dir = "../results/conf_simi.txt"
# # np.savetxt(dir, conf, delimiter=' & ', fmt='%d', newline=' \\\\ \hline\n')
# # with open(dir, 'r') as file:
# #     filedata = file.read()
# # filedata = filedata.replace('.', ',')
# # with open(dir, 'w') as file:
# #     file.write(filedata)
