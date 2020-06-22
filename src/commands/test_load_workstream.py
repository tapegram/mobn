import unittest

from src.commands.load_workstream import load_workstream
from src.domain.git import GitEffect
from src.domain.output import OutputEffect


class TestLoadWorkstream(unittest.TestCase):
    def test_load_workstream(self):
        results = load_workstream("branchName")
        self.assertEqual(
            len(results),
            7
        )

        (
            stash,
            checkoutMasterEffect,
            pullEffect1,
            pullingMasterOutputEffect,
            checkoutBranchEffect,
            pullEffect2,
            pullingWorkstreamOutputEffect,
        ) = results

        self.assertIsInstance(stash, GitEffect)
        self.assertEqual(
            stash.command,
            "git stash --include-untracked"
        )

        self.assertIsInstance(checkoutMasterEffect, GitEffect)
        self.assertEqual(
            checkoutMasterEffect.command,
            "git checkout master"
        )

        self.assertIsInstance(pullEffect1, GitEffect)
        self.assertEqual(
            pullEffect1.command,
            "git pull origin"
        )

        self.assertIsInstance(pullingMasterOutputEffect, OutputEffect)
        self.assertEqual(
            pullingMasterOutputEffect.message,
            "pulling master..."
        )

        self.assertIsInstance(checkoutBranchEffect, GitEffect)
        self.assertEqual(
            checkoutBranchEffect.command,
            "git checkout branchName"
        )

        self.assertIsInstance(pullingWorkstreamOutputEffect, OutputEffect)
        self.assertEqual(
            pullingWorkstreamOutputEffect.message,
            "pulling workstream..."
        )
