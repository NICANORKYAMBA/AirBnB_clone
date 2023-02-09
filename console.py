#!/usr/bin/python3
"""Console of the Airbnb"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Entry point of the interpreter"""

    prompt = "(hbnb) "

    def emptyline(self):
        """Ignores the empty spaces by repeating
        the last command"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """End of file marker"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
