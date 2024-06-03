import json

class DB:
    def __init__(self):
        self.teams = []
        self.tournament = []


    def load(self):

        f_tournament = open('db/Tournament.json') 
        # returns JSON object as 
        # a dictionary
        self.tournament = json.load(f_tournament)
        # Closing file
        f_tournament.close()

        return self.tournament
    
    def save(self):
        # Serializing json  
        tournament = json.dumps(self.tournament, indent = 6)
        # Writing to sample.json
        with open("Tournament.json", "w") as outfile:
            outfile.write(tournament)
        return True
    
