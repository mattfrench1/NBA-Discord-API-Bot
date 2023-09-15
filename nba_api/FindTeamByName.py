from nba_api.stats.static import teams


def getTeam(team_name):
    '''
    team_name - string, NBA team's name
    Description - Returns a NBA API team object. Return None if team_name is not valid.
    '''
    
    team = teams.find_teams_by_full_name(team_name)

    # Return just the NBA team object from the list
    if len(team) == 1:
        return team[0]
    
    return None