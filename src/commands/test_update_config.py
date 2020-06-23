import unittest

from src.command_handler import MOBN_CONFIG_PATH
from src.commands.new import new
from src.commands.update_config import update_config
from src.domain.git import GitEffect


class TestUpdateConfig(unittest.TestCase):
    def test_update_config(self):
        results = update_config("workstream", MOBN_CONFIG_PATH)
        self.assertEqual(
            len(results),
            3
        )

        (
            add,
            commit,
            push
        ) = results

        self.assertIsInstance(add, GitEffect)
        self.assertEqual(
            add.command,
            "git add {}".format(MOBN_CONFIG_PATH)
        )

        self.assertIsInstance(commit, GitEffect)
        self.assertEqual(
            commit.command,
            "git commit {} -m \"updating config\"".format(
                MOBN_CONFIG_PATH
            )
        )

        self.assertIsInstance(push, GitEffect)
        self.assertEqual(
            push.command,
            "git push -u origin workstream"
        )
