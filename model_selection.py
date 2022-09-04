from feature_engineering import feature_engineering

from collections import Iterable
data = feature_engineering()
print(data.head())
from pycaret.classification import *
training = setup(data = data, target = 'lung_cancer', log_experiment = True)

print(training)
best = compare_models(cross_validation=True)
print(best)
