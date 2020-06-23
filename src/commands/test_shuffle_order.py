import unittest

from src.commands.set_team import set_team
from src.commands.shuffle_order import shuffle_order
from src.domain.config import DEFAULT_CONFIG


class TestShuffleOrder(unittest.TestCase):
    def test_shuffle_order(self):
        shuffled = shuffle_order(
            set_team(
                ["Joe", "Sarah", "James"],
                DEFAULT_CONFIG
            )
        )
        self.assertIn("Joe", shuffled["team_members"])
        self.assertIn("Sarah", shuffled["team_members"])
        self.assertIn("James", shuffled["team_members"])

    def test_shuffle_empty(self):
        config = DEFAULT_CONFIG
        self.assertEqual(
            shuffle_order(config),
            DEFAULT_CONFIG
        )
