import unittest

from src.commands.increment_turn import increment_turn
from src.commands.select_next_mobber import select_next_mobber
from src.commands.set_team import set_team
from src.domain.config import DEFAULT_CONFIG


class TestSelectNextMobber(unittest.TestCase):

    def test_select_next_mobber(self):
        config = set_team(["Joe", "Sarah"], DEFAULT_CONFIG)
        self.assertEqual(
            select_next_mobber(config),
            "Joe"
        )
        self.assertEqual(
            select_next_mobber(
                increment_turn(config)
            ),
            "Sarah"
        )
        self.assertEqual(
            select_next_mobber(
                increment_turn(
                    increment_turn(config)
                )
            ),
            "Joe"
        )

    def test_select_next_mobber_with_empty_team(self):
        self.assertIsNone(
            select_next_mobber(DEFAULT_CONFIG)
        )
