# splot match_player_result.csv into test and train data.
# 1/3 test.csv
# 2/3 train.csv
# record are selected randomly

import csv
import random

test = []
train = []

test_train_determinant = [True]*20000 + [False]*30000
# test_train_determinant[i] === True meaning row i in data belong to training set

random.shuffle(test_train_determinant)

with open('match_result_binary_format.csv', 'rb') as csvfile:
  reader = csv.reader(csvfile, delimiter=',')
  count = -2

  for row in reader:
    # skip header
    count += 1
    if (count == -1):
        continue

    if test_train_determinant[count]:
      train.append(row)
    else:
      test.append(row)

with open('test_binary.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(test)

with open('train_binary.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(train)
