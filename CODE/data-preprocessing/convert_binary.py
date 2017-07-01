# convert team hero data to binary vector
# based on the fact that hero id ranges from 1 to 112

MAX_ID = 112
import csv

binary_match_data = []
with open('match_player_result.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader, None)
    for row in reader:
        match_data = [row[0]] + [0]*MAX_ID*2 + [row[11]]
        for pos in range(1,6):
            hero_id = int(row[pos])
            match_data[hero_id] = 1
        for pos in range(6,12):
            hero_id = int(row[pos])
            match_data[hero_id + MAX_ID] = 1
        binary_match_data.append(match_data)

with open('match_result_binary_format.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(binary_match_data)
