import csv

def get_attributes(path_to_data):
    attributes = []
    with open(path_to_data, 'rb') as csvfile:
      reader = csv.reader(csvfile, delimiter=',')
      for row in reader:
          row_attribute = [int(x) for x in row[1:225]]
          attributes.append(row_attribute)
    return attributes


def get_classes(path_to_data, header=False):
    classes = []
    with open(path_to_data, 'rb') as csvfile:
      reader = csv.reader(csvfile, delimiter=',')
      if header:
          next(reader, None)
      for row in reader:
          classes.append(int(row[225]))
    return classes
