from numpy import genfromtxt
from utils import *
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report

match_result = genfromtxt('match_player_result.csv', delimiter=',', dtype=int, skip_header=1)

train_X = get_attributes('train.csv')
train_Y = get_classes('train.csv')

test_X = get_attributes('test.csv')
test_Y = get_classes('test.csv')

neigh = KNeighborsClassifier(n_neighbors=1)

neigh.fit(train_X, train_Y)
y_pred_benchmark = neigh.predict(train_X)
print(classification_report(train_Y, y_pred_benchmark))

# y_pred_benchmark = tree_benchmark.predict(train_X)
# print(classification_report(train_Y, y_pred_benchmark))
