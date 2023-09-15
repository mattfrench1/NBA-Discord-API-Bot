import FindPlayerAwards
import GetCareerStats


def getPlayerComparison(first_player, second_player):
    '''
    first_player - NBA API player object, a present or past NBA player
    second_player - NBA API player object, a present or past NBA player
    Description - Returns a string of a comparison between the two NBA player's awards and career stats.
    '''

    # Get player awards
    player_1_awards = FindPlayerAwards.getPlayerAwards(first_player['id'], True)
    player_2_awards = FindPlayerAwards.getPlayerAwards(second_player['id'], True)
    
    awards_list = []

    # Compare awards
    for award in player_1_awards:
        if player_1_awards[award] is not None:
            if player_2_awards[award] is not None:
                if player_1_awards[award] > player_2_awards[award]:
                    awards_list.append((first_player['full_name'] + ' has ' + str(player_1_awards[award] - player_2_awards[award]) + ' more ' + award + '\n'))
                elif player_2_awards[award] > player_1_awards[award]:
                    awards_list.append((second_player['full_name'] + ' has '+ str(player_2_awards[award] - player_1_awards[award])+ ' more '+ award + '\n'))
                else:
                    awards_list.append((first_player['full_name'] + ' and '+ second_player['full_name']+ ' both have '+ str(player_1_awards[award])+ ' ' + award + '\n'))
            else:
                awards_list.append((first_player['full_name']+ ' has '+ str(player_1_awards[award]) + ' more '+ award + '\n'))
        elif player_2_awards[award] is not None:
            awards_list.append((second_player['full_name']+ ' has '+ str(player_2_awards[award])+ ' more '+ award + '\n'))
    
    career_stats_list = []
    
    # Get player career stats
    player_1_career_stats = GetCareerStats.getCareerStats(first_player['id'], True)
    player_2_career_stats = GetCareerStats.getCareerStats(second_player['id'], True)

    # Compare career stats
    for stat in player_1_career_stats:
        if player_1_career_stats[stat] > player_2_career_stats[stat]:
            career_stats_list.append((first_player['full_name']+ ' has '+ str(round(player_1_career_stats[stat] - player_2_career_stats[stat], 2))+ ' more '+ stat + '\n'))
        elif player_2_career_stats[stat] > player_1_career_stats[stat]:
            career_stats_list.append((second_player['full_name']+ ' has '+ str(round(player_2_career_stats[stat] - player_1_career_stats[stat], 2))+ ' more '+ stat + '\n'))
        else:
            career_stats_list.append((first_player['full_name']+ ' and '+ second_player['full_name']+ ' both have '+ str(player_1_career_stats[stat]) + ' ' + stat + '\n'))

    # Generate result string
    result_string = 'Awards:\n'

    for string in awards_list:
        result_string += string 

    result_string += '\nCareer Stats:\n'

    for string in career_stats_list:
        result_string += string
    
    return result_string

