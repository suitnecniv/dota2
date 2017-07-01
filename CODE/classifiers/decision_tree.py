from numpy import genfromtxt
from utils import *
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report

match_result = genfromtxt('match_player_result.csv', delimiter=',', dtype=int, skip_header=1)

train_X = get_attributes('train.csv')
train_Y = get_classes('train.csv')

test_X = get_attributes('test.csv')
test_Y = get_classes('test.csv')

tree_benchmark = DecisionTreeClassifier(max_leaf_nodes=100, random_state=0)
tree_benchmark.fit(train_X, train_Y)
y_pred_benchmark = tree_benchmark.predict(test_X)
print (y_pred_benchmark)
print(classification_report(test_Y, y_pred_benchmark))

# y_pred_benchmark = tree_benchmark.predict(train_X)
# print(classification_report(train_Y, y_pred_benchmark))