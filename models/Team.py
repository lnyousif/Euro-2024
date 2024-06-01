class Team:
    def __init__(self, name):
        self.name = name
        self.matches_played = 0
        self.wins = 0
        self.draws = 0
        self.losses = 0
        self.goals_for = 0
        self.goals_against = 0
        self.points = 0

    def goal_difference(self):
        return self.goals_for - self.goals_against

    def record_match(self, goals_for, goals_against):
        self.matches_played += 1
        self.goals_for += goals_for
        self.goals_against += goals_against

        if goals_for > goals_against:
            self.wins += 1
            self.points += 3
        elif goals_for == goals_against:
            self.draws += 1
            self.points += 1
        else:
            self.losses += 1

