import unittest

from src.git import branch


class TestGit(unittest.TestCase):

    def test_branch(self):
        self.assertTrue(False)
        self.assertEqual(
            branch(),
            []
        )
