import scipy.io as sio
import numpy as np
import pickle
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

mat_contents = sio.loadmat('../data/edema.mat')
cells_Ed = mat_contents['Y_normalizado_E']

mat_contents = sio.loadmat('../data/nodulo.mat')
cells_Nd = mat_contents['Y_normalizado_Nd']

mat_contents = sio.loadmat('../data/normal.mat')
cells_N = mat_contents['Y_normalizado_N']

mat_contents = sio.loadmat('../data/paralisia.mat')
cells_P = mat_contents['Y_normalizado_P']

n_dim = 9

# parametros = []
# phi = []
# for sinal in cells_Ed[0]:
#     phi = np.zeros((len(sinal)-2, n_dim))
#     for i in range(len(sinal)-3):
#         # phi[i, :] = [sinal[i+1], sinal[i]]
#         # phi[i, :] = [sinal[i + 1], sinal[i], sinal[i + 1]*sinal[i + 1],
#         #              sinal[i + 1]*sinal[i], sinal[i]*sinal[i]]
#         phi[i, :] = [sinal[i + 1], sinal[i], sinal[i + 1] * sinal[i + 1],
#                      sinal[i + 1]*sinal[i], sinal[i]*sinal[i], sinal[i + 1]*sinal[i + 1]*sinal[i + 1],
#                      sinal[i + 1]*sinal[i + 1]*sinal[i], sinal[i + 1]*sinal[i]*sinal[i],
#                      sinal[i]*sinal[i]*sinal[i]]
#     phit = phi.conj().transpose()
#
#     a = np.dot(phit, phi)
#     b = np.dot(phit, sinal[2:])
#     a_inv = np.linalg.inv(a)
#     theta = np.dot(a_inv, b)
#     parametros.append(theta)
# # np.savetxt("../MinSqFiles/L2/exemplophiL2", np.array(phi), delimiter=',', fmt='%1.4e')
# pickle.dump(parametros, open('../MinSqFiles/L3/parametroEd.obj', 'wb'))

# Reconstruindo
# parametros = pickle.load(open('../MinSqFiles/L1/parametroEd.obj', 'rb'))
# cells_est = []
# error = []
# for i, sinal in enumerate(cells_Ed[0, 0:1]):
#     p = parametros[i]
#     y_est = np.zeros(len(sinal))
#     for t in range(2, len(sinal)-2):
#         y_est[t] = p[0]*sinal[t-1] + p[1]*sinal[t-2]
#         # y_est[t] = p[0]*sinal[t-1]+ p[1]*sinal[t-2]+ p[2]*sinal[t-1]*sinal[t-1]+ \
#         #         p[3]*sinal[t-1]*sinal[t-2]+p[4]*sinal[t-2]*sinal[t-2]
#         # y_est[t] = p[0]*sinal[t-1]+ p[1]*sinal[t-2]+ p[2]*sinal[t-1]*sinal[t-1]+ \
#         #         p[3]*sinal[t-1]*sinal[t-2]+p[4]*sinal[t-2]*sinal[t-2] +p[5]* sinal[t-1]*sinal[t-1]*sinal[t-1] + \
#         #         p[6]*sinal[t-1]*sinal[t-1]*sinal[t-2]+p[7]*sinal[t-1]*sinal[t-2]*sinal[t-2] + \
#         #         p[8]*sinal[t-2]*sinal[t-2]*sinal[t-2]
#     cells_est.append(y_est.tolist())
#     error.append(mean_squared_error(y_est, cells_Ed[0, i]))

# np.savetxt("../MinSqFiles/L3/errorEdL3", np.array(error), delimiter=',', fmt='%1.4e')

# plt.plot(cells_est[0], 'g--', cells_Ed[0, 0], 'r-')
# plt.xlim(5000, 5700)
# plt.ylim(-0.015, 0.015)
# plt.xlabel("Amostra")
# plt.ylabel("Amplitude")
# plt.legend("Sinal identificado", "Sinal original")
# plt.show()
# fontsize='x-large'
# fig, ax = plt.subplots()
# ax.plot(cells_est[0], 'g--', label='Sinal estimado')
# ax.plot(cells_Ed[0, 0], 'r-', label='Sinal experimental')
# legend = ax.legend(loc='upper right', shadow=True )
# legend.get_frame().set_facecolor('#FFFFFF')
# plt.xlim(5000, 5700)
# plt.ylim(-0.015, 0.015)
# plt.xlabel("Amostra")
# plt.ylabel("Amplitude")
# plt.show()

f = open('../MinSqFiles/L3/errorEdL3', 'r')
f1 = open('../MinSqFiles/L3/errorNdL3', 'r')
f2 = open('../MinSqFiles/L3/errorNL3', 'r')
f3 = open('../MinSqFiles/L3/errorPL3', 'r')
x = []
x1 = []
x2 = []
x3 = []
for y in f.read().split('\n'):
    try:
        x.append(float(y))
    except ValueError:
        print(y)

for y in f1.read().split('\n'):
    try:
        x1.append(float(y))
    except ValueError:
        print(y)

for y in f2.read().split('\n'):
    try:
        x2.append(float(y))
    except ValueError:
        print(y)

for y in f3.read().split('\n'):
    try:
        x3.append(float(y))
    except ValueError:
        print(y)

print(np.mean(x2))
print(np.mean(x3))
print(np.mean(x))
print(np.mean(x1))
