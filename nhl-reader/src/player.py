class Player:
    def __init__(self, name, nationality, team, goals, assists):
        self.name = name
        self.nationality = nationality
        self.team = team
        self.goals = goals
        self.assists = assists
        
    def score(self):
        return self.goals+self.assists

    
    def __str__(self):
        return f"{self.name:20}" + f"{self.team:5}" + f"{str(self.goals):2}" + ' + ' + f"{str(self.assists):2}" + ' = ' + str(self.score())
