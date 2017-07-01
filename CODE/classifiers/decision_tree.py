from numpy import genfromtxt

match_result = genfromtxt('match_player_result.csv', delimiter=',', dtype=int, skip_header=1)
