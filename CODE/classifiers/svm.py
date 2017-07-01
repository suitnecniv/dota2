from utils import *
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

train_X = get_attributes('train_binary.csv')
train_Y = get_classes('train_binary.csv')

test_X = get_attributes('test_binary.csv')
test_Y = get_classes('test_binary.csv')

clf = SVC()

clf.fit(train_X, train_Y)
y_pred_benchmark = clf.predict(test_X)

print(classification_report(test_Y, y_pred_benchmark))
print(confusion_matrix(test_Y, y_pred_benchmark))
