from utils import *
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

train_X = get_attributes('train_binary.csv')
train_Y = get_classes('train_binary.csv')

test_X = get_attributes('test_binary.csv')
test_Y = get_classes('test_binary.csv')

tree_benchmark = DecisionTreeClassifier(max_leaf_nodes=50, random_state=0)
tree_benchmark.fit(train_X, train_Y)
y_pred_benchmark = tree_benchmark.predict(test_X)

print(classification_report(test_Y, y_pred_benchmark))
print(confusion_matrix(test_Y, y_pred_benchmark))
