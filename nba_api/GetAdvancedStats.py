from nba_api.stats.endpoints import playerestimatedmetrics
from nba_api.stats.endpoints import playercareerstats


def getAdvancedStats(nba_player_id):
    '''
    nba_player_id - int, NBA player's ID
    Description - Returns a string of given NBA player's advanced stats from their most recent season.
    '''

    career_stats = playercareerstats.PlayerCareerStats(player_id=nba_player_id)
    career_dict = career_stats.get_dict()
    result_sets = career_dict['resultSets']
    stats = result_sets[0]['rowSet']
    # print(result_sets[0]['headers'])   # get headers

    most_recent_season = len(stats) - 1
    season_string = stats[most_recent_season][1]

    # Advanced stats did not start until the 1996-97 season
    if season_string[:-3] < '1996':
        return None

    advanced_stats = playerestimatedmetrics.PlayerEstimatedMetrics(season=stats[most_recent_season][1])
    advanced_dict = advanced_stats.get_dict()
    result_set = advanced_dict['resultSet']

    # print(result_set['headers'])   # headers
    player = []

    # Grab the player
    for row in result_set['rowSet']:
        if nba_player_id in row:
            player.append(row)
            break 
    
    result_list = ['Advanced Stats for ', player[0][1], ' through ', str(player[0][2]), ' games during the ', season_string, ' season: \n\n', 
                  'Offensive Rating: ', str(player[0][7]), '\n', 'Defensive Rating: ', str(player[0][8]), '\n', 'Net Rating: ', str(player[0][9]), 
                  '\n', 'Usage Percentage: ', str(player[0][15]), '\n', 'Pace: ', str(player[0][16]), '\n']

    # Generate result string
    result_string = ''
    for string in result_list:
        result_string += string

    return result_string


