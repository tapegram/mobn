import unittest

from src.domain.config import DEFAULT_CONFIG
from src.domain.git import GitEffect
from src.domain.output import OutputEffect
from src.domain.say import VoiceEffect
from src.domain.sleep import SleepEffect
from src.finish import finish
from src.increment_turn import increment_turn
from src.load_workstream import load_workstream
from src.new import new
from src.select_next_mobber import select_next_mobber
from src.set_team import set_team
from src.start_turn import start_turn


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
