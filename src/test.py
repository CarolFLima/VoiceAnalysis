import pickle

dist = pickle.load(open('dist_N_Nd.obj', 'rb'))

a = [i for i in dist if (i<2e-05)]
print(len(a))
