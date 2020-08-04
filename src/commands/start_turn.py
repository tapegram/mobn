from src.domain.git import add_all, commit_all, push_origin_upstream, checkout, delete_branch
from src.domain.output import output
from src.domain.say import say
from src.domain.sleep import sleep


def start_turn(workstream):
    return [
        say("The timer has started."),
        output("The timer has started. Let's get mobbing."),
        sleep(600),
        say("Please, save all your work at your earliest convenience."),
        sleep(20),
        say("Your time is up."),
        add_all(),
        commit_all(),
        push_origin_upstream(workstream),
        output("pushed to branch!"),
        checkout("master"),
        delete_branch(workstream),
    ]
