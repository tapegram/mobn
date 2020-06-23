import unittest

from src.commands.load_workstream import load_workstream
from src.domain.git import GitEffect
from src.domain.output import OutputEffect


class TestLoadWorkstream(unittest.TestCase):
    def test_load_workstream(self):
        results = load_workstream("branchName")
        self.assertEqual(
            len(results),
            8
        )

        (
            stash,
            checkoutMasterEffect,
            pullEffect1,
            pullingMasterOutputEffect,
            deleteBranch,
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

        self.assertIsInstance(deleteBranch, GitEffect)
        self.assertEqual(
            deleteBranch.command,
            "git branch -D branchName"
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
