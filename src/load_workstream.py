from src.domain.git import checkout, pull
from src.domain.output import output


def load_workstream(branchName):
    return [
        checkout("master"),
        pull(),
        output("pulling master..."),
        checkout(branchName),
        pull(),
        output("pulling workstream..."),
    ]
