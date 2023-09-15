from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import commonplayerinfo


def getPlayerStats(player):
    '''
    player - NBA API player object, a present or past NBA player
    Description - Returns a string of per game stats and shooting percentages of a NBA player's most recent season.
    '''

    career_stats = playercareerstats.PlayerCareerStats(player_id=player['id'])
    career_dict = career_stats.get_dict()
    result_sets = career_dict['resultSets']
    stats = result_sets[0]['rowSet']
    # print(result_sets[0]['headers'])   # headers

    most_recent_season = len(stats) - 1
    result_string = "Stats From Player's Most Recent Season:\n\n"
    result_string += 'Points Per Game: '
    result_string += str(round(stats[most_recent_season][26]/stats[most_recent_season][6], 2))
    result_string += '\n'
    if stats[most_recent_season][20] is not None:
        result_string += 'Rebounds Per Game: '
        result_string += str(round(stats[most_recent_season][20]/stats[most_recent_season][6], 2))
        result_string += '\n'
    result_string += 'Assists Per Game: '
    result_string += str(round(stats[most_recent_season][21]/stats[most_recent_season][6], 2))
    result_string += '\n'

    if stats[most_recent_season][23] is not None:
        result_string += 'Blocks Per Game: '
        result_string += str(round(stats[most_recent_season][23]/stats[most_recent_season][6], 2))
        result_string += '\n'
    
    if stats[most_recent_season][22] is not None:
        result_string += 'Steals Per Game: '
        result_string += str(round(stats[most_recent_season][22]/stats[most_recent_season][6], 2))
        result_string += '\n'
    
    result_string += 'Field Goal Percentage: '
    result_string += str(round(stats[most_recent_season][11] * 100, 1))
    result_string += '%'
    result_string += '\n'

    if stats[most_recent_season][14] is not None:
        result_string += 'Three Point Percentage: '
        result_string += str(round(stats[most_recent_season][14] * 100, 1))
        result_string += '%'
        result_string += '\n'    

    result_string += 'Free Throw Percentage: '
    result_string += str(round(stats[most_recent_season][17] * 100, 1))
    result_string += '%'
    result_string += '\n'

    return result_string

