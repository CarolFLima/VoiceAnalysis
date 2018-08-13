import pickle
from sklearn.metrics import confusion_matrix
import numpy as np

dist = pickle.load(open('../Files/dist_Nd_P.obj', 'rb'))
janela = pickle.load(open('../Files/janela.obj', 'rb'))
print(type(dist))
print(dist.shape)

#conf = confusion_matrix([1, 2, 3, 4, 5], [1, 2, 1, 4, 5])
#print(conf)
