import unittest

from src.commands.new import new
from src.domain.git import GitEffect


class TestNew(unittest.TestCase):
    def test_new(self):
        results = new("branchName")
        self.assertEqual(
            len(results),
            1
        )

        create_branch_effect = results[0]
        self.assertIsInstance(create_branch_effect, GitEffect)
        self.assertEqual(
            create_branch_effect.command,
            "git checkout -b branchName"
        )
