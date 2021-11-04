import statistics
import unittest
from statistics import Statistics

from player_reader_stub import PlayerReaderStub

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.stats = Statistics(PlayerReaderStub())

    def test_hello_world(self):
        self.assertEqual("Hello world", "Hello world")

    def test_