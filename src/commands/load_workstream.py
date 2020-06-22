from src.domain.git import checkout, pull, stash
from src.domain.output import output


def load_workstream(workstream):
    return [
        stash(),
        checkout("master"),
        pull(),
        output("pulling master..."),
        checkout(workstream),
        pull(),
        output("pulling workstream..."),
    ]
