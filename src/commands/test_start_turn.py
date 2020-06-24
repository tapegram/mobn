import unittest

from src.commands.start_turn import start_turn
from src.domain.git import GitEffect
from src.domain.output import OutputEffect
from src.domain.say import VoiceEffect
from src.domain.sleep import SleepEffect


class TestCommands(unittest.TestCase):
    def test_start_turn(self):
        results = start_turn("matcha")
        self.assertEqual(
            len(results),
            12
        )

        (
            sayTimeStartEffect,
            timerStartOuputEffect,
            sleepEffect,
            saySaveYourWorEffect,
            sleepEffect2,
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

        self.assertIsInstance(saySaveYourWorEffect, VoiceEffect)
        self.assertEqual(
            saySaveYourWorEffect.phrase,
            "Save all your work now!!!"
        )

        self.assertIsInstance(sleepEffect2, SleepEffect)
        self.assertEqual(
            sleepEffect2.length,
            20
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
            "git commit --no-verify -m \"wip\""
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
