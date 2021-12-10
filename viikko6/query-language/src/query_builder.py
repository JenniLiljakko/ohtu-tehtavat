from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or

class QueryBuilder:

    def __init__(self, pino=All()) -> None:
        self.pino = pino

    def playsIn(self, team):
        return QueryBuilder(And(self.pino, PlaysIn(team)))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self.pino, HasAtLeast(value, attr)))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self.pino, HasFewerThan(value, attr)))

    def build(self):
        return self.pino

