import numpy as np
import pandas as pd
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline, make_union
from tpot.builtins import StackingEstimator
from sklearn.metrics import confusion_matrix

# NOTE: Make sure that the class is labeled 'target' in the data file
tpot_data = pd.read_csv('../data/dfL1.csv', dtype=np.float64)
features = tpot_data.drop('target', axis=1).values
training_features, testing_features, training_target, testing_target = \
            train_test_split(features, tpot_data['target'].values, random_state=50, test_size=0.5)

print(len(features))

# exported_pipeline = make_pipeline(
#     StackingEstimator(estimator=ExtraTreesClassifier(bootstrap=True, criterion="entropy", max_features=0.8500000000000001, min_samples_leaf=15, min_samples_split=6, n_estimators=100)),
#     StackingEstimator(estimator=KNeighborsClassifier(n_neighbors=12, p=1, weights="distance")),
#     ExtraTreesClassifier(bootstrap=False, criterion="entropy", max_features=0.7000000000000001, min_samples_leaf=16, min_samples_split=7, n_estimators=100)
# )
#
# exported_pipeline.fit(training_features, training_target)
#
# results = exported_pipeline.predict(testing_features)
#
# print("Res: " + str(results))
# print("Real: " + str(testing_target))
#
# conf = confusion_matrix(testing_target, results, labels=[2., 3., 0., 1.])
#
# print("Conf Test: \n" + str(conf))
#
# # results2 = exported_pipeline.predict(training_features)
# # conf2 = confusion_matrix(training_target, results2)
# # print("Conf Train: \n" + str(conf2))
# # print("Res2: " + str(results2))
