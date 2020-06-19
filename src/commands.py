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
        sleep(600),
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


def get_help():
    return {
        "mobn new": "create a new mob session on your configured workstream",
        "mobn start": "alias for `mobn new`",
        "mobn continue":"pulls the current workstream onto your local machine and sets a timer",
        "mobn done <new branch name>":"puts all of the worksteam's commits onto a new branch so you can create a PR.",
        "mobn team <space delimited list of names>":"let mobn know who is working in this mob",
        "mobn skip":"tells mobbing to skip to the next team member",
        "mobn config":"show me the current config!",
        "mobn hello":"hello, world!",
        "mobn help":"you are here!",
    }


def select_next_mobber(config):
    team = config["team_members"]
    next_mobber = None
    if team:
        next_mobber = team[config["turn"]]
    return next_mobber
