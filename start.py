from models.Team import Team
from models.Tournament import Tournament
from db.db import DB

tournment = DB().load( )

groups = []  
for team in tournment["teams"]:
    
    new_group = [x for x in groups if x.name == ("Group " + team["group"])]
    if new_group:
        new_group[0].add_team(Team(team["name"]))
    else:
        new_group = Tournament("Group " + team["group"])
        new_group.add_team(Team(team["name"]))
        groups.append(new_group)


groups[0].record_match("Italy", 3, "Spain", 1)  # Team 1 won with 3 goals, Team 2 lost with 1 goal
groups[0].record_match("Albania", 3, "Spain", 1)  # Team 1 won with 3 goals, Team 2 lost with 1 goal

groups[0].display_standings()

# # Create instances of Team
# team1 = Team("Team 1")
# team2 = Team("Team 2")

# # Create an instance of Tournament
# tournament = Tournament("Soccer Tournament")

# # Add teams to the tournament
# tournament.add_team(team1)
# tournament.add_team(team2)

# # Record match results
# tournament.record_match("Team 1", 3, "Team 2", 1)  # Team 1 won with 3 goals, Team 2 lost with 1 goal

# # Display standings
# tournament.display_standings()
# tournament.record_match("Team 1", 3, "Team 2", 1)  # Team 1 won with 3 goals, Team 2 lost with 1 goal
# tournament.record_match("Team 1", 2, "Team 2", 2)  # Draw match, both Team 1 and Team 2 scored 2 goals

# Display standings
# tournament.display_standings()


