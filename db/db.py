import json

class DB:
    def __init__(self):
        self.teams = []
        self.tournament = []


    def load(self):

        f_teams = open('Teams.json')
        f_tournament = open('Tournament.json') 
        # returns JSON object as 
        # a dictionary
        self.teams = json.load(f_teams)
        self.tournament = json.load(f_tournament)
        # Closing file
        f_teams.close()
        f_tournament.close()

        return self.teams, self.tournament
    
    def save(self):
        # Serializing json  
        teams = json.dumps(self.teams, indent = 6)
        tournament = json.dumps(self.tournament, indent = 6)
        # Writing to sample.json
        with open("Teams.json", "w") as outfile:
            outfile.write(teams)
        with open("Tournament.json", "w") as outfile:
            outfile.write(tournament)
        return True
    

# json.dump(value, save_file, indent = 6)  
# save_file.close()  