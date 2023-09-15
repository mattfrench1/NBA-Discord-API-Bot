from nba_api.stats.static import players


def getPlayer(full_name):
    '''
    full_name - string, NBA player's first and last name
    Description - Returns a NBA player object from the NBA API, or return None if full_name is not a 
    valid NBA player name.
    '''
    
    player = players.find_players_by_full_name(full_name)

    # Above method returns a dictionary inside a list, we just want to return the dictionary
    if len(player) == 1:
        return player[0] 
    return None

