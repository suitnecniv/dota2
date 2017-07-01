import csv

with open('match.csv', 'rb') as csvfile:

with open('players.csv', 'rb') as csvfile:
  reader = csv.reader(csvfile, delimiter=',')

  count = 0

  current_match_id = 0
  last_match_id = 0
  no_of_players_in_match = 0
  for row in reader:
    # skip header
    count += 1
    if (count == 1):
        continue

    # first record
    if (count == 2):
        last_match_id = row[0]
        print ('\nmatch id: ' + last_match_id + ' |')

    current_match_id = row[0]


    # same match
    if (current_match_id == last_match_id):
        no_of_players_in_match += 1
        # print (row[2] + ',')

    # new match
    else:
        if not no_of_players_in_match == 10:
            print (no_of_players_in_match)
            print (last_match_id)
        last_match_id = current_match_id
        no_of_players_in_match = 1
        # print ('\nmatch id: ' + current_match_id + ' |')
        # print (row[2] + ',')

    # if count == 100:
    #     break
