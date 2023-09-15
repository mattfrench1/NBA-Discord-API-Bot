from nba_api.stats.endpoints import playerdashptshotdefend
from nba_api.stats.static import players


def generateActivePlayersIds():
    '''
    Description - Returns a list of int ID's for all active NBA players.
    '''

    all_active_players = players.get_active_players()
    active_player_ids = []

    for player in all_active_players:
        active_player_ids.append(player['id'])
        
    return active_player_ids


def getPlayerShootingVsOpp(nba_player_id, nba_team_id):
    '''
    nba_player_id - int, NBA player ID
    nba_team_id - int, NBA team ID
    Description - Returns a string with a given NBA player's shooting percentages differences against given NBA team.
    Values are in comparison to league shooting average against said team. (+7.1% means player shoots 7.4%
    above average shooting against team.) Returns None if NBA player is not currently in the NBA.
    '''

    active_players_list = generateActivePlayersIds()
    if nba_player_id not in active_players_list:
        return None
    
    shot_range = {}
    shooting_stats = playerdashptshotdefend.PlayerDashPtShotDefend(team_id=nba_team_id, player_id=nba_player_id)
    stats_dict = shooting_stats.get_dict()
    result_sets = stats_dict['resultSets']
    # print(result_sets[0]['headers'])  # To grab headers

    if len(result_sets[0]['rowSet']) == 0:
        return 'Error! Player can not have opponent shooting stats against own team!'

    # Go through rowSet and grab overall and 2/3 point percentages
    for row in result_sets[0]['rowSet']:
        if 'Overall' in row:
            shot_range['Overall'] = row
            if shot_range['Overall'][9] is not None:
                shot_range['Overall'][9] = round(shot_range['Overall'][9] * 100, 1)
                if shot_range['Overall'][9] > 0:
                    positive_string = '+'
                    positive_string += str(shot_range['Overall'][9])
                    positive_string += '%'
                    shot_range['Overall'][9] = positive_string
                else:
                    shot_range['Overall'][9] = str(shot_range['Overall'][9])
                    shot_range['Overall'][9] += '%'
            else:
                shot_range['Overall'][9] = 'No shots attempted'

        if '3 Pointers' in row:
            shot_range['3 Pointers'] = row
            if shot_range['3 Pointers'][9] is not None:
                shot_range['3 Pointers'][9] = round(shot_range['3 Pointers'][9] * 100, 1)
                if shot_range['3 Pointers'][9] > 0:
                    positive_string = '+'
                    positive_string += str(shot_range['3 Pointers'][9])
                    positive_string += '%'
                    shot_range['3 Pointers'][9] = positive_string
                else:
                    shot_range['3 Pointers'][9] = str(shot_range['3 Pointers'][9])
                    shot_range['3 Pointers'][9] += '%'
            else:
                shot_range['3 Pointers'][9] = 'No 3 pointers attempted'

        if '2 Pointers' in row:
            shot_range['2 Pointers'] = row
            if shot_range['2 Pointers'][9] is not None:
                shot_range['2 Pointers'][9] = round(shot_range['2 Pointers'][9] * 100, 1)
                if shot_range['2 Pointers'][9] > 0:
                    positive_string = '+'
                    positive_string += str(shot_range['2 Pointers'][9])
                    positive_string += '%'
                    shot_range['2 Pointers'][9] = positive_string
                else:
                    shot_range['2 Pointers'][9] = str(shot_range['2 Pointers'][9])
                    shot_range['2 Pointers'][9] += '%'
            else:
                shot_range['2 Pointers'][9] = 'No 2 pointers attempted'

    # Add results to list and iterate over to create result string
    result_list = ['Overall: ', shot_range['Overall'][9], '\n', '3 Pointers: ', shot_range['3 Pointers'][9],  '\n', '2 Pointers: ', shot_range['2 Pointers'][9]]

    result_string = ''

    for string in result_list:
        result_string += string
    
    return result_string
    