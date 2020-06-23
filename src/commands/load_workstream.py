from src.domain.git import checkout, pull, stash, delete_branch
from src.domain.output import output


def load_workstream(workstream):
    return [
        stash(),
        checkout("master"),
        pull(),
        output("pulling master..."),
        delete_branch(workstream, force=True),
        checkout(workstream),
        pull(),
        output("pulling workstream..."),
    ]
