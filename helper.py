from constants import TEAMS, PLAYERS

#####################
# CLEANING FUNCTION #
#####################

def clean_experience(str):
    """ clean experience player data to return bolean """
    if str == "YES":
        return True
    else:
        return False

def clean_height(str):
    """ clean height player data to return a float number """
    height = str.split()[0]
    return float(height)

def clean_guardians(str):
    """ clean guardians name of player data to return a list of names """
    return str.split(" and ")

def clean_player(player):
    """ This function is to clean player data  """

    player_dict = {}
    player_dict["name"] = player['name']
    player_dict["experience"] = clean_experience(player["experience"])
    player_dict["height"] = clean_height(player["height"])
    player_dict["guardians"] = clean_guardians(player["guardians"])

    return player_dict

def clean_player_list():
    """ This function is to clean all player data in PLAYERS """

    clean_players = []

    for player in PLAYERS:
        clean_players.append(clean_player(player))
    return clean_players


#######################
# DISPLAYING FUNCTION #
#######################


def display_menu_option():
    """ this function is to display menu option in the beginning """
    print("\n---- MENU ----\n")
    print("Here are your choices:")
    print("1) Display Team Stats")
    print("2) Quit\n")

def display_team_option(team_names):
    """ this function is to display team names """

    print("\nTeams : ")
    for i, name in enumerate(team_names):
        print(f"{i+1}) {name}")

def display_total_players(num_player, num_exp_player, num_not_exp_player):
    """ this function is to display total players, number of experience and inexperience players """

    print(f"Total_players: {num_player}")
    print(f"> Experience players : {num_exp_player}")
    print(f"> Inexperience players : {num_not_exp_player}")

def display_player_name(team):
    """ this function is to display player name in the team """

    print("\nPlayers on Team:")
    print(f"> {', '.join(team)}")

def display_height(avg_height):
    """ this function is to display average player height in the team"""

    print(f"\nTeam Average Height (inches) : {avg_height:.2f}")

def display_guardians(guardian_list):
    """ this function is to display player guadian names """

    print("\nPlayer Guardians :")
    print(f"> {', '.join(guardian_list)}")

def display_stats(team, team_str, num_player,
                  num_exp_player, num_not_exp_player,
                  avg_height, guardian_list):
    """
    This function is to display team statistics
    """

    print("\n" + team_str)
    print("-" * len(team_str))

    # print total players
    display_total_players(num_player, num_exp_player, num_not_exp_player)

    # print players name
    display_player_name(team)

    # print average player height
    display_height(avg_height)

    # print put player guardian names
    display_guardians(guardian_list)


#######################
# MISC FUNCTION       #
#######################

def get_input(min_val, max_val):
    """ This function is to get input from user, and check the input for int and within range """

    while True:
        option = input("\nEnter an option > ")
        try:
            option = int(option)
            if (option < min_val) or (option > max_val):
                print("Try again, your number is out of range.")
                continue
        except ValueError:
            print("The value entered was not a number, try again.")
        else:
            return option

def get_experience_players(player_list):
    """ this function is to get a list of experience player name in player_list (cleaned PLAYERS) """

    return [player['name']  for player in player_list  if player['experience']]

def get_not_experience_players(player_list):
    """ this function is to get a list of inexperience player name in player_list (cleaned PLAYERS) """

    return [player['name']  for player in player_list  if not player['experience']]

def balance_players(players):
    """
    this function is to balance and divide list of players into 3 team
    It returns a list of player list, 3 teams x n players
    """

    n = int(len(players) / 3)
    bal_players = [players[i:i + n] for i in range(0, len(players), n)]
    return bal_players

def create_team(exp_players, not_exp_players):
    """
    This function is to crete a balance team within experience and inexperience team
    It returns a list of player list, 3 teams x n players
    """

    # get a list of player names : experience and inexperience
    bal_exp_players = balance_players(exp_players)
    bal_not_exp_players = balance_players(not_exp_players)

    #create an empty list to store a list of player list
    teams = []

    for i in range(len(bal_exp_players)):
        team = bal_exp_players[i] + bal_not_exp_players[i]
        teams.append(team)

    return teams

def get_height_list(name_list, player_list):
    """
    This function is to get the list of player height
    INPUT :
        name_list : list of player name
        player_list : list of clean PLAYER
    RETURN:
        a list of player height given a player name_list
    """

    return [player['height'] for player in player_list if player["name"] in name_list]

def average(lst):
    """ This function to calculate average of given list """
    return sum(lst) / len(lst)

def get_num_exp_players(name_list, player_list):
    """
    This function calculate number of experience players in the team
    INPUT :
        name_list : list of player name
        player_list : list of clean PLAYER
    RETURN:
        int, number of experience player given the player name_list
    """

    exp_arr = [int(player["experience"]) for player in player_list if player['name'] in name_list]
    return sum(exp_arr)

def get_guardians(name_list, player_list):
    """
    This function is to get the list of player guardians name
    INPUT :
        name_list : list of player name
        player_list : list of clean PLAYER
    RETURN:
        a list of player guardian name given a player name_list
    """

    return [guardian for player in player_list for guardian in player["guardians"] if player["name"] in name_list]

def get_team_stats(team, team_str, clean_players):
    """
    INPUT :
        team : list of player names
        team_str : a string to display name of the team
        clean_players : list of cleaned PLAYERS
    RETURN : tuples
        team : list of player names
        team_str : a string
        num_player : int, number of player in the team
        num_exp_player : int, number of experience player in the team
        num_not_exp_player: int, number of inexperience player in the team
        avg_height : float, average height players
        guardian_list : list of player guardians
    """

    num_player = len(team)
    num_exp_player = get_num_exp_players(team, clean_players)
    num_not_exp_player = num_player - num_exp_player

    height_list = get_height_list(team, clean_players)
    avg_height = average(height_list)
    guardian_list = get_guardians(team, clean_players)

    return team, team_str, num_player, num_exp_player, num_not_exp_player, avg_height, guardian_list
