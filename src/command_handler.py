import json
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


def command_handler(command, *arguments):
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
                    say("It is {}s turn".format(first_mobber))
                    if first_mobber else NullEffect()
                ] +
                [set_config(MOBN_CONFIG_PATH, config)] +
                new(workstream_name) +
                start_turn(workstream_name) +
                [
                    say("It is {}s turn".format(next_mobber))
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
                say("It is {}s turn".format(next_mobber)).run()

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
        config = get_config("mobn.config").run()
        config = set_team(arguments, config)
        set_config(MOBN_CONFIG_PATH, config).run()
        print(json.dumps(config, indent=4))

    elif command == "skip":
        config = get_config("mobn.config").run()
        config = increment_turn(config)
        set_config(MOBN_CONFIG_PATH, config).run()

        next_mobber = select_next_mobber(config)
        if next_mobber:
            say("It is {}s turn".format(next_mobber)).run()

        print(json.dumps(config, indent=4))

    elif command == "hello":
        print("Hello, World")

    else:
        print("I don't understand")
        print(json.dumps(get_help(), indent=4))
