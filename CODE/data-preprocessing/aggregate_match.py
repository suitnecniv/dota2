# produce match_player_result.csv

import csv

match_result = []

with open('match.csv', 'rb') as csvfile:
  reader = csv.reader(csvfile, delimiter=',')
  count = 0
  for row in reader:
    # skip header
    count += 1
    if (count == 1):
        continue

    if row[9] == 'True':
      match_result.append('1')
    else:
      match_result.append('0')

match_player_results = [['match_id','team_1_player_1','team_1_player_2','team_1_player_3','team_1_player_4','team_1_player_5','team_2_player_1','team_2_player_2','team_2_player_3','team_2_player_4','team_2_player_5','result']]

with open('players.csv', 'rb') as csvfile:
      reader = csv.reader(csvfile, delimiter=',')

      count = 0

      current_match_id = 0
      last_match_id = 0
      cur_row=[]
      for row in reader:
        # skip header
        count += 1
        if (count == 1):
            continue

        # first record
        if (count == 2):
            last_match_id = row[0]
            cur_row.append(last_match_id)

        current_match_id = row[0]

        # same match
        if (current_match_id == last_match_id):
            cur_row.append(row[2])

        # new match
        else:
            cur_row.append(match_result[int(last_match_id)])
            last_match_id = current_match_id
            # print (cur_row)
            match_player_results.append(cur_row)
            cur_row = []
            cur_row.append(current_match_id)
            cur_row.append(row[2])

with open('match_player_result.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(match_player_results)
