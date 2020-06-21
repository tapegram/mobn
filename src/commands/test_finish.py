import unittest

from src.commands.finish import finish
from src.domain.git import GitEffect
from src.domain.output import OutputEffect


class TestCommands(unittest.TestCase):
    def test_finish(self):
        results = finish("matcha", "branchName")
        self.assertEqual(
            len(results),
            12
        )

        (
            pushingEverythingOutputEffect,
            addAllEffect,
            commitAllEffect,
            pushAllEffect,
            creatingBranchOutputEffect,
            createBranchEffect,
            pushOriginUpstreamEffect,
            cleaningUpOutputEffect,
            checkoutMasterEffect,
            deleteBranchEffect,
            pullEffect,
            successOutputEffect,
        ) = results

        self.assertIsInstance(pushingEverythingOutputEffect, OutputEffect)
        self.assertEqual(
            pushingEverythingOutputEffect.message,
            "pushing everything..."
        )

        self.assertIsInstance(addAllEffect, GitEffect)
        self.assertEqual(
            addAllEffect.command,
            "git add ."
        )

        self.assertIsInstance(commitAllEffect, GitEffect)
        self.assertEqual(
            commitAllEffect.command,
            "git commit -m \"wip\""
        )

        self.assertIsInstance(pushAllEffect, GitEffect)
        self.assertEqual(
            pushAllEffect.command,
            "git push -u origin matcha"
        )

        self.assertIsInstance(creatingBranchOutputEffect, OutputEffect)
        self.assertEqual(
            creatingBranchOutputEffect.message,
            "putting it all on branchName"
        )

        self.assertIsInstance(createBranchEffect, GitEffect)
        self.assertEqual(
            createBranchEffect.command,
            "git checkout -b branchName"
        )
        self.assertIsInstance(pushOriginUpstreamEffect, GitEffect)
        self.assertEqual(
            pushOriginUpstreamEffect.command,
            "git push -u origin branchName"
        )

        self.assertIsInstance(cleaningUpOutputEffect, OutputEffect)
        self.assertEqual(
            cleaningUpOutputEffect.message,
            "cleaning up..."
        )

        self.assertIsInstance(checkoutMasterEffect, GitEffect)
        self.assertEqual(
            checkoutMasterEffect.command,
            "git checkout master"
        )

        self.assertIsInstance(deleteBranchEffect, GitEffect)
        self.assertEqual(
            deleteBranchEffect.command,
            "git branch -d matcha"
        )

        self.assertIsInstance(pullEffect, GitEffect)
        self.assertEqual(
            pullEffect.command,
            "git pull origin"
        )

        self.assertIsInstance(successOutputEffect, OutputEffect)
        self.assertEqual(
            successOutputEffect.message,
            "ready to open PR!"
        )
