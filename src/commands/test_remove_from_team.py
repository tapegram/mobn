import unittest

from src.commands.remove_from_team import remove_from_team
from src.commands.set_team import set_team
from src.domain.config import DEFAULT_CONFIG


class TestRemoveFromTeam(unittest.TestCase):
    def test_remove_not_in_team(self):
        config = set_team(
            ["Joe", "Sarah", "James"],
            DEFAULT_CONFIG
        )
        self.assertEqual(
            remove_from_team("Bob", config),
            config
        )

    def test_remove_from_team(self):
        config = set_team(
            ["Joe", "Sarah", "James"],
            DEFAULT_CONFIG
        )
        self.assertEqual(
            remove_from_team("Sarah", config),
            set_team(
                ["Joe", "James"],
                DEFAULT_CONFIG
            )
        )

    def test_remove_from_tempty(self):
        config = DEFAULT_CONFIG
        self.assertEqual(
            remove_from_team("Bob", config),
            DEFAULT_CONFIG
        )
