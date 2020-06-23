import unittest

from src.commands.add_to_team import add_to_team
from src.commands.set_team import set_team
from src.domain.config import DEFAULT_CONFIG


class TestAddToTeam(unittest.TestCase):
    def test_add_to_existing(self):
        config = set_team(
            ["Joe", "Sarah", "James"],
            DEFAULT_CONFIG
        )
        self.assertEqual(
            add_to_team("Bob", config),
            set_team(
                ["Joe", "Sarah", "James", "Bob"],
                DEFAULT_CONFIG
            )
        )

    def test_add_to_tempy(self):
        config = DEFAULT_CONFIG
        self.assertEqual(
            add_to_team("Bob", config),
            set_team(
                ["Bob"],
                DEFAULT_CONFIG
            )
        )
