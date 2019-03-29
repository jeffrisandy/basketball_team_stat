from constants import TEAMS, PLAYERS
from helper import *

def start():
    while True:
        print("\nBASKETBALL TEAM STATS TOOL")
        display_menu_option()

        # get input from user, there are only 2 options
        menu_option = get_input(1, 2)

        if menu_option == 2:
            break
        else:
            # display team option
            display_team_option(team_names)

            # get input from user : there are 3 teams to choose
            selected_team = get_input(1, 3)

            # get selected team player name list
            team_index = selected_team - 1
            team = teams[team_index]

            # get selected team name
            team_name = team_names[team_index]
            team_str = f"Team: {team_name} Stats"

            # get team stats
            stats = get_team_stats(team, clean_players)

            # display team stats
            display_stats(team_str, *stats)

            input("\n\nPress ENTER to continue...\n")


if __name__ == '__main__':
    # team names
    team_names = TEAMS.copy()

    # clean PLAYER
    clean_players = clean_player_list()

    # get the experience & inexperience player names
    exp_players =  get_experience_players(clean_players)
    not_exp_players = get_not_experience_players(clean_players)

    # create teams with balance within experience and inexperience player
    teams = create_team(exp_players, not_exp_players)

    start()
