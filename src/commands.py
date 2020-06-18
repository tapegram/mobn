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


def create_pr(branch_name):
    """
    Disclaimer: doesnt actually create a pr yet haha
    """
    return [
        create_branch(branch_name),
        push_origin_upstream(branch_name),

        # todo, create a PR here

        # cleanup
        checkout("master"),
    ]


def new(branch_name):
    return [
        create_branch(branch_name),
    ] + next()


def next():
    return [
        say("Time start!"),
        sleep(10 * 60),
        say('Time up!'),
        add_all(),
        commit_all(),
        push_all(),
        output("pushed to branch!"),
        checkout("master"),
        delete_branch(get_workstream_name()),
    ]


def start(branchName):
    return [
        checkout("master"),
        pull(),
        output("pulling master..."),
        checkout(branchName),
        pull(),
        output("pulling workstream..."),
        next(),
    ]


def done(branchName):
    return [
        add_all(),
        commit_all(),
        push_all(),
        create_pr(branchName),
        delete_branch(get_workstream_name()),
        pull(),
    ]


