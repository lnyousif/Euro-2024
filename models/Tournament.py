class Tournament:
    def __init__(self, name):
        self.name = name
        self.teams = []

    def add_team(self, team):
        self.teams.append(team)

    def record_match(self, team1_name, team1_goals, team2_name, team2_goals):
        team1 = next((team for team in self.teams if team.name == team1_name), None)
        team2 = next((team for team in self.teams if team.name == team2_name), None)

        if team1 and team2:
            team1.record_match(team1_goals, team2_goals)
            team2.record_match(team2_goals, team1_goals)

    def display_standings(self):
        standings = sorted(self.teams, key=lambda team: (-team.points, -team.goal_difference(), -team.goals_for))
        for i, team in enumerate(standings, start=1):
            print(f"{i}. {team.name}, {team.points} pts, {team.goal_difference()} GD")