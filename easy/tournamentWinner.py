# O(n) time | O(k) space k = #teams
def update_score(team, score, scores):
	if team not in scores.keys():
		scores[team] = 0
	scores[team] += score

def tournamentWinner(competitions, results):
	team_score = {'best':0}
	tourment_winner = ''
	for i,comp in enumerate(competitions):
		result = results[i]
		home, away = comp
		
		won_team = home if result == 1 else away
		update_score(won_team, 3, team_score)
		
		if team_score[won_team] >= team_score['best']:
				team_score['best'] = team_score[won_team]
				tourment_winner = won_team
		
	print(team_score)
    return tourment_winner
