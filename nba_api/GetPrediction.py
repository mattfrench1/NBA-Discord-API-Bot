from nba_api.stats.endpoints import teamestimatedmetrics
from nba_api.stats.static import teams


def getPrediction():
    '''
    Description - Uses calculations from the seasons before NBA winners from the 2015 finals winners to the 2023 finals
    winners to predict the upcoming champion strictly based on stats from the season before. 
    (Formula to find winner does not take into account the 2020 Lakers and 2022 Warriors due to both teams having major
    roster constructions, (Lakers bringing in superstar Anthony Davis and Warriors finally having Klay/Draymond healthy) as
    these two teams were totally different from the season before they won to the following season.)
    '''

    advanced_team_stats = teamestimatedmetrics.TeamEstimatedMetrics(season='2022-23')

    team_stats_dict = advanced_team_stats.get_dict()
    resultset = team_stats_dict['resultSet']

    stats = {}
    final_teams = []
    preferred_teams = []

    # Add team's off/def/net rating/rank, win rank, reb pct/rank, ast ratio/rank
    for row in resultset['rowSet']:
        stats[row[1]] = row[7], row[21], row[8], row[22], row[9], row[23], row[17], row[14], row[27], row[11], row[24] 

    for row in stats:

        # If offensive rating rank is top 7 or if defensive rating rank is top 6
        if stats[row][1] <= 7 or stats[row][3] <= 6:

            # If net rating rank is top 15
            if stats[row][5] <= 15:

                # If win rank is top 11
                if stats[row][6] <= 11:

                    # If assist ratio rank is top 10
                    if stats[row][10] <= 10:

                        # If rebound percentage rank is top 10
                        if stats[row][8] <= 10:
                            final_teams.append(row)

                            # If rebound percentage rank is 8 or 9 --> majority of championships since 2015
                            # were ranked at either 8 or 9...could be a major factor in determining the finals winner
                            if stats[row][8] == 8 or stats[row][8] == 9:
                                preferred_teams.append(row)

    # If no teams meet the formula's criteria above
    if len(final_teams) == 0:
        return None

    # Generate result string
    teams_string = ''
    for team in final_teams:
        nba_team = teams.find_team_name_by_id(team)
        teams_string += nba_team['full_name']
        teams_string += ', '
    
    favorite = ''
    if len(preferred_teams) > 0:
        for team in preferred_teams:
            nba_team = teams.find_team_name_by_id(team)
            favorite += nba_team['full_name']
            favorite += ', '

    result_string = ''
    result_list = ['Based on my prediction model, the following teams have the best chances to win the upcoming NBA finals:\n',
                   teams_string[:-2], '\n\nThe team that has the best chance of winning is the: ', favorite[:-2]]
    
    if len(preferred_teams) == 0:
        result_list.pop()
        result_list.pop()
    
    for string in result_list:
        result_string += string 
    
    return result_string
                    
