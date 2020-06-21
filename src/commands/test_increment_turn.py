import unittest

from src.commands.increment_turn import increment_turn
from src.commands.set_team import set_team
from src.domain.config import DEFAULT_CONFIG


class TestIncrementTurn(unittest.TestCase):
    def test_increment_turn_with_team_members(self):
        config = set_team(["Joe", "Sarah"], DEFAULT_CONFIG)
        self.assertEqual(
            increment_turn(config),
            dict(
                turn=1,
                team_members=["Joe", "Sarah"]
            )
        )

    def test_increment_turn_with_no_team_members(self):
        self.assertEqual(
            increment_turn(DEFAULT_CONFIG),
            DEFAULT_CONFIG
        )

    def test_increment_turn_rolls_over(self):
        config = set_team(["Joe", "Sarah"], DEFAULT_CONFIG)
        self.assertEqual(
            increment_turn(increment_turn(config)),
            dict(
                turn=0,
                team_members=["Joe", "Sarah"]
            )
        )
