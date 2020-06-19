from src.git import (
    create_branch,
    push_origin_upstream,
    checkout,
    add_all,
    commit_all,
    delete_branch,
    pull,
)
from src.output import output
from src.say import say
from src.sleep import sleep


def new(workstream):
    return [
        create_branch(workstream),
    ]


def start_turn(workstream):
    return [
        say("Time start!"),
        output("Timer started - lets get mobbing!"),
        sleep(5),
        say('Time up!'),
        add_all(),
        commit_all(),
        push_origin_upstream(workstream),
        output("pushed to branch!"),
        checkout("master"),
        delete_branch(workstream),
    ]


def load_workstream(branchName):
    return [
        checkout("master"),
        pull(),
        output("pulling master..."),
        checkout(branchName),
        pull(),
        output("pulling workstream..."),
    ]


def finish(workstream, branchName):
    return [
        output("pushing everything..."),
        add_all(),
        commit_all(),
        push_origin_upstream(workstream),

        # Create PR
        output("putting it all on {}".format(branchName)),
        create_branch(branchName),
        push_origin_upstream(branchName),

        # todo, create a PR here

        # cleanup
        output("cleaning up..."),
        checkout("master"),
        delete_branch(workstream),
        pull(),

        output("ready to open PR!"),
    ]


def set_team(team_members, config):
    new_config = config.copy()
    new_config["team_members"] = team_members
    return new_config


def increment_turn(config):
    new_config = config.copy()

    if len(new_config["team_members"]) == 0:
        return new_config

    new_config["turn"] = (new_config.get("turn", 0) + 1) % len(new_config["team_members"])
    return new_config
