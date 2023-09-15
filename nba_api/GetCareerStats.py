from nba_api.stats.endpoints import playercareerstats


def getCareerStats(player_id, stats_dict):
    '''
    player_id - int, NBA player's ID number
    stats_dict - boolean, indicates whether to return a dictionary or string
    Description - Generates career totals in points, assists, rebounds, blocks, and steals and per game totals. 
    Also generates total games, minutes, and years played in the NBA. If stats_dict is True, a dictionary of these
    values gets returned and if False, a string of these values gets returned.
    '''
    
    career_stats = playercareerstats.PlayerCareerStats(player_id)
    career_stats_dict = career_stats.get_dict()
    career_stats_result_sets = career_stats_dict['resultSets']
    results_dict = {}

    total_points = 0
    total_assists = 0
    total_rebounds = 0
    total_blocks = 0
    total_steals = 0
    total_games = 0
    total_minutes = 0
    years = 0

    for row in career_stats_result_sets[0]['rowSet']:
        total_points += row[26]
        total_assists += row[21]
        total_rebounds += row[20]
        total_blocks += row[23]
        total_steals += row[22]
        total_games += row[6]
        total_minutes += row[8]
        years += 1
    
    results_dict['Points'] = total_points
    results_dict['Assists'] = total_assists
    results_dict['Rebounds'] = total_rebounds
    results_dict['Blocks'] = total_blocks
    results_dict['Steals'] = total_steals
    results_dict['Games'] = total_games
    results_dict['Minutes'] = total_minutes
    results_dict['Years'] = years 
    results_dict['PPG'] = round(total_points / total_games, 2)
    results_dict['APG'] = round(total_assists / total_games, 2)
    results_dict['RPG'] = round(total_rebounds / total_games, 2)
    results_dict['BPG'] = round(total_blocks / total_games, 2)
    results_dict['SPG'] = round(total_steals / total_games, 2)

    if stats_dict is True:
        return results_dict
    
    result_string = ''

    for key in results_dict:
        result_string += key
        result_string += ': '
        result_string += str(results_dict[key])
        result_string += '\n'

    return result_string