import argparse
import matplotlib.pyplot as plt
from utils.query import get_world_cup_overview

def print_win_country(most_win_country):
    print("\n=======================================")
    print("Countries which won:")
    print(most_win_country)
    countries = most_win_country["Winner"].tolist()
    win_times = most_win_country["WinTimes"].tolist()
    plt.barh(countries, win_times)
    plt.savefig("chart/win_countries.png")
    plt.close()

def print_goals_player(most_goals_player):
    print("\n=======================================")
    print("Players who has most goals (top 10):")
    print(most_goals_player)
    players = most_goals_player["Player_Name"].tolist()
    for i, player in enumerate(players):
        players[i] = player.split(' ', 1)[0]
    goals = most_goals_player["goals"].tolist()
    plt.barh(players, goals)
    plt.savefig("chart/most_goal_players.png")
    plt.close()
    
def print_hardest_player(most_attended_player):
    print("\n=======================================")
    print("Hardest player who attends most of matches (top 10):")
    print(most_attended_player)
    hard_players = most_attended_player["Player_Name"].tolist()
    for i, hard_player in enumerate(hard_players):
        hard_players[i] = hard_player.split(' ', 1)[0]
    attended_times = most_attended_player["AttendedTimes"].tolist()
    plt.barh(hard_players, attended_times)
    plt.savefig("chart/hardest_players.png")
    plt.close()


def main(parser):
    database = "spring-ember-370820.fifa_world_cup"
    most_goals_country, most_win_country, most_goals_player, most_attended_player = get_world_cup_overview(database)
    print("\n=======================================")
    print("Coutries which have most goals")
    print(most_goals_country)
    print_win_country(most_win_country)
    print_goals_player(most_goals_player)
    print_hardest_player(most_attended_player)
    print("=======================================")
    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p", help="player name", type=str
    )
    parser.add_argument(
        "-y", help="year of world cup", type=int
    )
    main(parser)