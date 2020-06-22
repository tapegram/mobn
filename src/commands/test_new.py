import unittest

from src.commands.new import new
from src.domain.git import GitEffect


class TestNew(unittest.TestCase):
    def test_new(self):
        results = new("branchName")
        self.assertEqual(
            len(results),
            5
        )

        (
            checkoutMaster,
            pull,
            deleteExistingWorkstream,
            deleteRemoteWorkstream,
            createNewWorkstream,
        ) = results

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
        self.assertIsInstance(deleteExistingWorkstream, GitEffect)
        self.assertEqual(
            deleteExistingWorkstream.command,
            "git branch -D branchName"
        )

        self.assertIsInstance(deleteRemoteWorkstream, GitEffect)
        self.assertEqual(
            deleteRemoteWorkstream.command,
            "git push origin :branchName"
        )

        self.assertIsInstance(createNewWorkstream, GitEffect)
        self.assertEqual(
            createNewWorkstream.command,
            "git checkout -b branchName"
        )
