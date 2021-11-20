import statistics
import unittest
from player import Player
from statistics import Statistics

from player_reader_stub import PlayerReaderStub

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.player_reader = PlayerReaderStub()
        self.stats = Statistics(self.player_reader)

    def test_hello_world(self):
        self.assertEqual("Hello world", "Hello world")

    def test_loytyyko_pelaaja(self):
        self.assertEqual(Player("Semenko", "EDM", 4, 12 ).name, self.stats.search("Semenko").name)

    def test_ei_loydy_pelaajaa(self):
        self.assertIsNone(self.stats.search("Smith"))

    def test_team(self):
        self.assertEqual(len(self.stats.team("EDM")), 3)

    def test_top_scorers(self):
        results = self.stats.top_scorers(3)
        self.assertEqual(results[0].name, "Gretzky")
        self.assertEqual(results[1].name, "Lemieux")
        self.assertEqual(results[2].name, "Yzerman")