import numpy as np
import pandas as pd
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import SelectPercentile, f_classif
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.pipeline import make_pipeline, make_union
from tpot.builtins import StackingEstimator
from sklearn.metrics import confusion_matrix

# NOTE: Make sure that the class is labeled 'target' in the data file
tpot_data = pd.read_csv('../data/dfL2.csv', dtype=np.float64)
features = tpot_data.drop('target', axis=1).values
training_features, testing_features, training_target, testing_target = \
            train_test_split(features, tpot_data['target'].values, random_state=42, test_size=0.3)



# Score on the training set was:0.6748447204968945
exported_pipeline = make_pipeline(
    SelectPercentile(score_func=f_classif, percentile=64),
    StackingEstimator(estimator=GaussianNB()),
    ExtraTreesClassifier(bootstrap=False, criterion="entropy", max_features=0.6000000000000001, min_samples_leaf=20, min_samples_split=11, n_estimators=100)
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
