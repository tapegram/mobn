import unittest

from src.commands.finish import finish
from src.commands.load_branch_into_workstream import load_branch_into_workstream
from src.domain.git import GitEffect
from src.domain.output import OutputEffect


class TestLoadBranchIntoWorkstream(unittest.TestCase):
    def test_load_branch_into_workstream(self):
        effects = load_branch_into_workstream("matcha", "branchName")
        self.assertEqual(
            len(effects),
            7
        )

        (
            checkoutMaster,
            pull,
            deleteWorkstream,
            checkoutBranch,
            createNewWorkStream,
            pushUpstream,
            output,
        ) = effects

        self.assertIsInstance(checkoutMaster, GitEffect)
        self.assertEqual(
            checkoutMaster.command,
            "git checkout master"
        )

        self.assertIsInstance(pull, GitEffect)
        self.assertEqual(
            pull.command,
            "git pull origin"
        )

        self.assertIsInstance(deleteWorkstream, GitEffect)
        self.assertEqual(
            deleteWorkstream.command,
            "git branch -D matcha"
        )

        self.assertIsInstance(checkoutBranch, GitEffect)
        self.assertEqual(
            checkoutBranch.command,
            "git checkout branchName"
        )

        self.assertIsInstance(createNewWorkStream, GitEffect)
        self.assertEqual(
            createNewWorkStream.command,
            "git checkout -b matcha"
        )

        self.assertIsInstance(pushUpstream, GitEffect)
        self.assertEqual(
            pushUpstream.command,
            "git push -u origin matcha"
        )

        self.assertIsInstance(output, OutputEffect)
        self.assertEqual(
            output.message,
            "branch branchName loaded onto workstream"
        )
