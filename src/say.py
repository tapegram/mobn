from subprocess import Popen, PIPE, STDOUT


def say(phrase):
    process = Popen(['say {}'.format(phrase)], shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE, )
    output, _ = process.communicate()
