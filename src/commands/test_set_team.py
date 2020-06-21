import unittest

from src.commands.set_team import set_team
from src.domain.config import DEFAULT_CONFIG


class TestCommands(unittest.TestCase):
    def test_set_team(self):
        self.assertEqual(
            set_team(["Joe", "Sarah"], DEFAULT_CONFIG),
            dict(
                turn=0,
                team_members=["Joe", "Sarah"]
            )
        )

    def test_overwrite_set_team(self):
        config = set_team(["Joe", "Sarah"], DEFAULT_CONFIG)
        self.assertEqual(
            set_team(["Emma", "Sheila"], config),
            dict(
                turn=0,
                team_members=["Emma", "Sheila"]
            )
        )
