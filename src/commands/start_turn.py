from src.domain.git import add_all, commit_all, push_origin_upstream, checkout, delete_branch
from src.domain.output import output
from src.domain.say import say
from src.domain.sleep import sleep


def start_turn(workstream):
    return [
        say("Time start!"),
        output("Timer started - lets get mobbing!"),
        sleep(600),
        say('Save all your work now!!!'),
        sleep(20),
        say('Time up!'),
        add_all(),
        commit_all(),
        push_origin_upstream(workstream),
        output("pushed to branch!"),
        checkout("master"),
        delete_branch(workstream),
    ]
