def get_help():
    return {
        "mobn new <optional: space delimited list of names>": "create a new mob session on your configured workstream. optional names will be set as the the team members",
        "mobn start": "alias for `mobn new`",
        "mobn continue": "pulls the current workstream onto your local machine and sets a timer",
        "mobn done <new branch name>": "puts all of the worksteam's commits onto a new branch so you can create a PR.",
        "mobn load <branch>": "loads in the branch into the workstream (note that this replaces any changes currently in the workstream)",
        "mobn team <space delimited list of names>": "let mobn know who is working in this mob",
        "mobn shuffle-team": "shuffles the team order",
        "mobn add-member <name>": "adds a new team member",
        "mobn remove-member <name>": "removes a team member",
        "mobn skip": "tells mobbing to skip to the next team member",
        "mobn config": "show me the current config!",
        "mobn hello": "hello, world!",
        "mobn help": "you are here!",
    }
