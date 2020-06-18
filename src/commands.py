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
from src.output import output
from src.say import say
from src.sleep import sleep


def new(branch_name):
    return [
        create_branch(branch_name),
    ]


def next(workstream):
    return [
        say("Time start!"),
        sleep(10 * 60),
        say('Time up!'),
        add_all(),
        commit_all(),
        push_all(),
        output("pushed to branch!"),
        checkout("master"),
        delete_branch(workstream),
    ]


def start(branchName):
    return [
        checkout("master"),
        pull(),
        output("pulling master..."),
        checkout(branchName),
        pull(),
        output("pulling workstream..."),
    ]


def done(worksteam, branchName):
    return [
        add_all(),
        commit_all(),
        push_all(),
        # Create PR
        create_branch(branchName),
        push_origin_upstream(branchName),

        # todo, create a PR here

        # cleanup
        checkout("master"),
        delete_branch(worksteam),
        pull(),
    ]
