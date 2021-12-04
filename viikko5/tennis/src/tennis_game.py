class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0
        self.love = 0
        self.fifteen = 1
        self.thirty = 2
        self.forty = 3
        

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def individual_score(self, score):
        if score == self.love:
            return "Love"  
        elif score == self.fifteen:
            return "Fifteen"
        elif score == self.thirty:
            return "Thirty"
        elif score == self.forty:
            return "Forty"
        else: 
            return "Deuce"

    def advantage(self):
        minus_result = self.m_score1 - self. m_score2

        if minus_result == 1:
            return "Advantage player1"
        elif minus_result == -1:
            return "Advantage player2"
        elif minus_result >= 2:
            return "Win for player1"
        else:
            return "Win for player2"
        

    def get_score(self):

        if self.m_score1 == self.m_score2:
            if self.m_score1 > self.forty:
                return self.individual_score(self.m_score1)
            return self.individual_score(self.m_score1)+"-All"
            
        elif self.m_score1 > self.forty or self.m_score2 > self.forty:
            return self.advantage()
        else:
            return self.individual_score(self.m_score1) + "-" + self.individual_score(self.m_score2)

