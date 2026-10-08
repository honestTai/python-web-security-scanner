import argparse
import os
import sys

if sys.version_info < (3, 7):
    sys.stdout.write("Sorry, dirsearch requires Python 3.7 or higher\n")
    sys.exit(1)

from lib.core.argument_parser import ArgumentParser
from lib.controller.controller import Controller
from lib.output.verbose_output import CLIOutput
from lib.output.silent_output import PrintOutput


class Program(object):
    def __init__(self, url):
        self.script_path = os.path.dirname(os.path.realpath(__file__))

        self.arguments = ArgumentParser(self.script_path, url)

        if self.arguments.quiet:
            self.output = PrintOutput(self.arguments.color)
        else:
            self.output = CLIOutput(self.arguments.color)

        self.controller = Controller(self.script_path, self.arguments, self.output)
        self.result = self.controller.result




if __name__ == "__main__":
    arguments = sys.argv[1:]
    print(arguments[1])
    main = Program(arguments[1])
    print(main.result)