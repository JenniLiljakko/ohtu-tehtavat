

class PlayerStats:

    def __init__(self, reader):
        self.reader = reader
        self.players = self.reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        players=[]
        for player in self.players:
            if player.nationality == nationality:
                players.append(player)

        def order(player):
            return player.score()

        players.sort(key=order, reverse=True)
        return players

    


