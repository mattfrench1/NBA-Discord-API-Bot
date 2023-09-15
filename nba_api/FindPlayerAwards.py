from nba_api.stats.static import players
from nba_api.stats.endpoints import playerawards
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import commonplayerinfo
import AllNbaWinners


def getAdjective(num):
    '''
    num - string
    Description - Returns adjective string for given number. Returns num if num is not 1, 2, or 3.
    '''

    if num == '1':
        return 'First Team'
    elif num == '2':
        return 'Second Team'
    elif num == '3':
        return 'Third Team'
    else:
        return num
    

def getPlayerAwards(player_id, dict_results):
    '''
    player_id - int, NBA player's ID number
    dict_results - boolean, True value returns the dictionary and False value returns the string result
    Descriptions - Calculates the given player's career awards and returns either a dictionary of 
    the result or a string with all the awards. None gets returned for players with no awards.
    '''

    descriptions = ['NBA Most Valuable Player', 'NBA Finals Most Valuable Player', 'All-NBA', 
                    'All-Defensive Team', 'All-Rookie Team', 'NBA All-Star Most Valuable Player',
    'NBA Rookie of the Year', 'Olympic Bronze Medal', 'Olympic Gold Medal', 'Olympic Silver Medal', 
    'NBA Player of the Week', 'NBA Player of the Month', 'NBA Rookie of the Month']

    player_awards = playerawards.PlayerAwards(player_id)
    award_dict = player_awards.get_dict()
    awards_list = award_dict['resultSets']
    awards = awards_list[0]['rowSet']

    results_dictionary = {'NBA Championships': [], 'NBA Most Valuable Player': 0, 'NBA Finals Most Valuable Player': 0,
                          'First Team All-NBA': 0, 'Second Team All-NBA': 0, 'Third Team All-NBA': 0, 'First Team All-Defensive Team': 0,
                          'Second Team All-Defensive Team': 0, 'Third Team All-Defensive Team': 0, 'NBA Rookie of the Year': 0, 
                          'First Team All-Rookie Team': 0, 'Second Team All-Rookie Team': 0, 'Third Team All-Rookie Team': 0,
                          'NBA All-Star Most Valuable Player': 0, 'Olympic Gold Medal': 0, 'Olympic Silver Medal': 0, 'Olympic Bronze Medal': 0,
                          'NBA Player of the Month': 0, 'NBA Player of the Week': 0, 'NBA Rookie of the Month': 0 }

    career_stats = playercareerstats.PlayerCareerStats(player_id=player_id)
    career_dict = career_stats.get_dict()

    # Only add specified awards
    for row in awards:
        if row[4] in descriptions:
            if row[5] is not None:
                adj = getAdjective(row[5])
                if adj+ ' '+ row[4] in results_dictionary:
                    results_dictionary[adj + ' '+ row[4]] += 1
            else:
                if row[4] in results_dictionary:
                    results_dictionary[row[4]] += 1

    # Set empty awards to None
    for key in results_dictionary:
        if results_dictionary[key] == 0:
            results_dictionary[key] = None
    
    # Grab results from API request
    result_set = career_dict['resultSets']
    results = result_set[0]['rowSet']

    # Check each year player played in to see how many championships player has
    for row in results:
        if row[3] != 0:
            if AllNbaWinners.isTeamWinYear(row[3], row[1]) is True:
                results_dictionary['NBA Championships'].append(row[1])
    
    if len(results_dictionary['NBA Championships']) == 0:
        results_dictionary['NBA Championships'] = None
    else:
        results_dictionary['NBA Championships'] = len(results_dictionary['NBA Championships'])

    if dict_results is True:
        return results_dictionary

    result_string = ''
    none_counter = 0

    # Build string to return
    for key in results_dictionary:
        if results_dictionary[key] is not None:
            results_dictionary[key] = str(results_dictionary[key])
            string = ''
            string += key
            string += ' - '
            string += results_dictionary[key]
            string += '\n'
            result_string += string
        else:
            none_counter += 1 

    # If player has no awards, return None
    if none_counter == 20:
        return None
    
    return result_string

    

