from google.cloud import bigquery

MOST_GOALS_COUNTRY_SQL = """
        SELECT * FROM {database}.WorldCups
        WHERE GoalsScored = (SELECT max(GoalsScored) FROM {database}.WorldCups)   
    """ 
MOST_WIN_COUNTRY_SQL = """
        Select Winner, COUNT(Winner) as WinTimes from {database}.WorldCups
        Group by Winner
        ORDER BY WinTimes DESC
    """
MOST_GOALS_PLAYER_SQL = """
        SELECT * FROM(
            SELECT Player_Name, ((length(Event) - length(replace(Event,'G','')))/length('G')) as goals
            FROM {database}.WorldCupPlayers
            GROUP BY Player_Name, Event
            )
        WHERE goals is not null
        ORDER BY goals DESC
        LIMIT 10
        ;
    """
MOST_ATTENDED_PLAYER_SQL = """
        SELECT Player_Name, COUNT(MatchID) AS AttendedTimes 
        FROM {database}.WorldCupPlayers
        GROUP BY Player_Name
        ORDER BY AttendedTimes DESC
        LIMIT 10
    """

# get world cup overview data from database
def get_world_cup_overview(database):
    print("=========connecting to BigQuery=========")
    client = bigquery.Client(project="spring-ember-370820")
    print("=========BigQuery connected!=========")
    
    print("=========Loading data from " + database + "=========")
    most_goals_cntry_sql = MOST_GOALS_COUNTRY_SQL.format(database = database)
    most_goals_cntry = client.query(most_goals_cntry_sql).to_dataframe()
    most_win_cntry_sql = MOST_WIN_COUNTRY_SQL.format(database = database)
    most_win_cntry = client.query(most_win_cntry_sql).to_dataframe()
    most_goals_player_sql = MOST_GOALS_PLAYER_SQL.format(database = database)
    most_goals_player = client.query(most_goals_player_sql).to_dataframe()
    most_attended_sql = MOST_ATTENDED_PLAYER_SQL.format(database = database)
    most_attened_player = client.query(most_attended_sql).to_dataframe() #.values.flatten().tolist()
    print("=========Data loaded=========")
    
    return most_goals_cntry, most_win_cntry, most_goals_player, most_attened_player
    

if __name__ == "__main__":
    print("This is a query module!")