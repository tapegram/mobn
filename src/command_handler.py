import json

from src.commands.add_to_team import add_to_team
from src.commands.load_branch_into_workstream import load_branch_into_workstream
from src.commands.remove_from_team import remove_from_team
from src.commands.shuffle_order import shuffle_order
from src.commands.update_config import update_config
from src.domain.config import get_workstream_name, get_config, set_config, remove_config
from src.domain.say import say
from src.commands.finish import finish
from src.commands.get_help import get_help
from src.commands.increment_turn import increment_turn
from src.commands.load_workstream import load_workstream
from src.commands.new import new
from src.commands.select_next_mobber import select_next_mobber
from src.commands.set_team import set_team
from src.commands.start_turn import start_turn


MOBN_CONFIG_PATH = "mobn.config"


class NullEffect(object):
    def run(self):
        pass


def runAll(effects):
    for effect in effects:
        effect.run()


def command_handler(command, arguments):
    if command == "new" or command == "start":
        workstream_name = get_workstream_name().run()
        if not workstream_name:
            print("No workstream found! try `export MOBN_WORKSTREAM_NAME=<chosen name>`")
        else:
            config = get_config("mobn.config").run()
            first_mobber = select_next_mobber(config)
            config = increment_turn(config)
            next_mobber = select_next_mobber(config)

            runAll(
                [
                    say("It is {}'s turn".format(first_mobber))
                    if first_mobber else NullEffect()
                ] +
                [set_config(MOBN_CONFIG_PATH, config)] +
                new(workstream_name) +
                start_turn(workstream_name) +
                [
                    say("It is {}'s turn".format(next_mobber))
                    if next_mobber else NullEffect()
                ]
            )

    elif command == "continue":
        workstream_name = get_workstream_name().run()
        if not workstream_name:
            print("No workstream found! try `export MOBN_WORKSTREAM_NAME=<chosen name>`")

        else:
            runAll(load_workstream(workstream_name))

            config = get_config("mobn.config").run()
            config = increment_turn(config)
            set_config(MOBN_CONFIG_PATH, config).run()

            next_mobber = select_next_mobber(config)
            runAll(start_turn(workstream_name))
            if next_mobber:
                say("It is {}'s turn".format(next_mobber)).run()

    elif command == "done":
        workstream_name = get_workstream_name().run()
        if not workstream_name:
            print("No workstream found! try `export MOBN_WORKSTREAM_NAME=<chosen name>`")
        else:
            remove_config(MOBN_CONFIG_PATH).run()
            runAll(finish(workstream_name, arguments[0]))

    elif command == "workstream":
        print(get_workstream_name().run())

    elif command == "help":
        print(json.dumps(get_help(), indent=4))

    elif command == "config":
        config = get_config("mobn.config").run()
        print(json.dumps(config, indent=4))

    elif command == "team":
        workstream_name = get_workstream_name().run()
        if not workstream_name:
            print("No workstream found! try `export MOBN_WORKSTREAM_NAME=<chosen name>`")

        config = get_config("mobn.config").run()
        config = set_team(arguments, config)
        set_config(MOBN_CONFIG_PATH, config).run()
        runAll(update_config(workstream_name, MOBN_CONFIG_PATH))
        print(json.dumps(config, indent=4))

    elif command == "shuffle-team":
        workstream_name = get_workstream_name().run()
        if not workstream_name:
            print("No workstream found! try `export MOBN_WORKSTREAM_NAME=<chosen name>`")

        config = get_config("mobn.config").run()
        config = shuffle_order(config)
        set_config(MOBN_CONFIG_PATH, config).run()
        runAll(update_config(workstream_name, MOBN_CONFIG_PATH))
        print(json.dumps(config, indent=4))

    elif command == "add-member":
        workstream_name = get_workstream_name().run()
        if not workstream_name:
            print("No workstream found! try `export MOBN_WORKSTREAM_NAME=<chosen name>`")

        config = get_config("mobn.config").run()
        config = add_to_team(arguments[0], config)
        set_config(MOBN_CONFIG_PATH, config).run()
        runAll(update_config(workstream_name, MOBN_CONFIG_PATH))
        print(json.dumps(config, indent=4))

    elif command == "remove-member":
        workstream_name = get_workstream_name().run()
        if not workstream_name:
            print("No workstream found! try `export MOBN_WORKSTREAM_NAME=<chosen name>`")

        config = get_config("mobn.config").run()
        config = remove_from_team(arguments[0], config)
        set_config(MOBN_CONFIG_PATH, config).run()
        runAll(update_config(workstream_name, MOBN_CONFIG_PATH))
        print(json.dumps(config, indent=4))

    elif command == "skip":
        workstream_name = get_workstream_name().run()
        if not workstream_name:
            print("No workstream found! try `export MOBN_WORKSTREAM_NAME=<chosen name>`")

        config = get_config("mobn.config").run()
        config = increment_turn(config)
        set_config(MOBN_CONFIG_PATH, config).run()
        runAll(update_config(workstream_name, MOBN_CONFIG_PATH))

        next_mobber = select_next_mobber(config)
        if next_mobber:
            say("It is {}'s turn".format(next_mobber)).run()

        print(json.dumps(config, indent=4))

    elif command == "load":
        workstream_name = get_workstream_name().run()
        if not workstream_name:
            print("No workstream found! try `export MOBN_WORKSTREAM_NAME=<chosen name>`")
        runAll(load_branch_into_workstream(workstream_name, arguments[0]))

    elif command == "hello":
        print("Hello, World")

    else:
        print("I don't understand")
        print(json.dumps(get_help(), indent=4))
