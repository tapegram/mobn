import unittest

from src.commands import new, start_turn, load_workstream, finish
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

    def test_start_turn(self):
        results = start_turn("matcha")
        self.assertEqual(
            len(results),
            10
        )

        (
            sayTimeStartEffect,
            timerStartOuputEffect,
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

        self.assertIsInstance(timerStartOuputEffect, OutputEffect)
        self.assertEqual(
            timerStartOuputEffect.message,
            "Timer started - lets get mobbing!"
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
            "git commit -m \"wip\""
        )

        self.assertIsInstance(pushAllEffect, GitEffect)
        self.assertEqual(
            pushAllEffect.command,
            "git push -u origin matcha"
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
            "git branch -d matcha"
        )

    def test_start(self):
        results = load_workstream("branchName")
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
