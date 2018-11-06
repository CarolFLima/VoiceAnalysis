import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.feature_selection import VarianceThreshold
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix

# NOTE: Make sure that the class is labeled 'target' in the data file
tpot_data = pd.read_csv('../data/dfL3.csv', dtype=np.float64)
features = tpot_data.drop('target', axis=1).values
training_features, testing_features, training_target, testing_target = \
            train_test_split(features, tpot_data['target'].values, random_state=42, test_size=0.5)

# Score on the training set was:0.7599802371541502
exported_pipeline = make_pipeline(
    PCA(iterated_power=3, svd_solver="randomized"),
    VarianceThreshold(threshold=0.001),
    StandardScaler(),
    PCA(iterated_power=2, svd_solver="randomized"),
    LinearSVC(C=0.5, dual=False, loss="squared_hinge", penalty="l1", tol=0.001)
)

exported_pipeline.fit(training_features, training_target)
results = exported_pipeline.predict(testing_features)

print("Res: " + str(results))
print("Real: " + str(testing_target))

conf = confusion_matrix(testing_target, results, labels=[2., 3., 0., 1.])

print("Conf Test: \n" + str(conf))

results2 = exported_pipeline.predict(training_features)
conf2 = confusion_matrix(training_target, results2)
print("Conf Train: \n" + str(conf2))
# print("Res2: " + str(results2))
