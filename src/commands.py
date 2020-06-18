import time

from src.config import get_workstream_name
from src.git import (
    create_branch,
    push_origin_upstream,
    checkout,
    add_all,
    commit_all,
    push_all,
    delete_branch,
    pull,
)
from src.say import say


def create_pr(branch_name):
    """
    Disclaimer: doesnt actually create a pr yet haha
    """
    create_branch(branch_name)
    push_origin_upstream(branch_name)

    # todo, create a PR here

    # cleanup
    checkout("master")

def new(branch_name):
    create_branch(branch_name)
    next()

def next():
    say("Time start!")
    time.sleep(10 * 60)
    say('Time up!')
    add_all()
    commit_all()
    push_all()
    print("pushed to branch!")
    checkout("master")
    delete_branch(get_workstream_name())

def start(branchName):
    checkout("master")
    pull()
    print("pulling master...")
    checkout(branchName)
    pull()
    print("pulling workstream...")
    next()

def done(branchName):
    add_all()
    commit_all()
    push_all()
    create_pr(branchName)
    delete_branch(get_workstream_name())
    pull()


