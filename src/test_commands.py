import unittest

from src.commands import new, next, start, done
from src.git import GitEffect
from src.output import OutputEffect
from src.say import VoiceEffect
from src.sleep import SleepEffect


class TestCommands(unittest.TestCase):

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

    def test_next(self):
        results = next("matcha")
        self.assertEqual(
            len(results),
            9
        )

        (
            sayTimeStartEffect,
            sleepEffect,
            sayTimeUpEffect,
            addAllEffect,
            commitAllEffect,
            pushAllEffect,
            outputEffect,
            checkoutEffect,
            deleteBranchEffect,
        ) = results

        self.assertIsInstance(sayTimeStartEffect, VoiceEffect)
        self.assertEqual(
            sayTimeStartEffect.phrase,
            "Time start!"
        )

        self.assertIsInstance(sleepEffect, SleepEffect)
        self.assertEqual(
            sleepEffect.length,
            600
        )

        self.assertIsInstance(sayTimeUpEffect, VoiceEffect)
        self.assertEqual(
            sayTimeUpEffect.phrase,
            "Time up!"
        )

        self.assertIsInstance(addAllEffect, GitEffect)
        self.assertEqual(
            addAllEffect.command,
            "git add ."
        )

        self.assertIsInstance(commitAllEffect, GitEffect)
        self.assertEqual(
            commitAllEffect.command,
            "git commit -m wip"
        )

        self.assertIsInstance(pushAllEffect, GitEffect)
        self.assertEqual(
            pushAllEffect.command,
            "git push origin"
        )

        self.assertIsInstance(outputEffect, OutputEffect)
        self.assertEqual(
            outputEffect.message,
            "pushed to branch!"
        )

        self.assertIsInstance(checkoutEffect, GitEffect)
        self.assertEqual(
            checkoutEffect.command,
            "git checkout master"
        )

        self.assertIsInstance(deleteBranchEffect, GitEffect)
        self.assertEqual(
            deleteBranchEffect.command,
            "git branch -D matcha"
        )

    def test_start(self):
        results = start("branchName")
        self.assertEqual(
            len(results),
            6
        )

        (
            checkoutMasterEffect,
            pullEffect1,
            pullingMasterOutputEffect,
            checkoutBranchEffect,
            pullEffect2,
            pullingWorkstreamOutputEffect,
        ) = results

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

    def test_done(self):
        results = done("matcha", "branchName")
        self.assertEqual(
            len(results),
            8
        )

        (
            addAllEffect,
            commitAllEffect,
            pushAllEffect,
            createBranchEffect,
            pushOriginUpstreamEffect,
            checkoutMasterEffect,
            deleteBranchEffect,
            pullEffect,
        ) = results

        self.assertIsInstance(addAllEffect, GitEffect)
        self.assertEqual(
            addAllEffect.command,
            "git add ."
        )

        self.assertIsInstance(commitAllEffect, GitEffect)
        self.assertEqual(
            commitAllEffect.command,
            "git commit -m wip"
        )

        self.assertIsInstance(pushAllEffect, GitEffect)
        self.assertEqual(
            pushAllEffect.command,
            "git push origin"
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

        self.assertIsInstance(checkoutMasterEffect, GitEffect)
        self.assertEqual(
            checkoutMasterEffect.command,
            "git checkout master"
        )

        self.assertIsInstance(deleteBranchEffect, GitEffect)
        self.assertEqual(
            deleteBranchEffect.command,
            "git branch -D matcha"
        )

        self.assertIsInstance(pullEffect, GitEffect)
        self.assertEqual(
            pullEffect.command,
            "git pull origin"
        )
