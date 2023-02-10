#!/usr/bin/python3
"""Console of the Airbnb"""
import cmd
from datetime import datetime
from shlex import split
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Entry point of the interpreter"""

    prompt = "(hbnb) "

    def my_errors(self, line, num_of_args):
        """Displays error messages to user
        Args:
            line(any): gets user input using command line
            num_of_args(int): number of input arguments
        Description:
            Displays output to the use based on
            the input commands.
        """
        classes = ["BaseModel"]

        msg = ["** class name missing **",
               "** class doesn't exist **",
               "** instance id missing **",
               "** no instance found **",
               "** attribute name missing **",
               "** value missing **"]

        if not line:
            print(msg[0])
            return 1
        args = line.split()
        if num_of_args >= 1 and args[0] not in classes:
            print(msg[1])
            return 1
        elif num_of_args == 1:
            return 0
        if num_of_args >= 2 and len(args) < 2:
            print(msg[2])
            return 1
        d = storage.all()

        for i in range(len(args)):
            if args[i][0] == '"':
                args[i] = args[i].replace('"', "")
        key = args[0] + '.' + args[1]
        if num_of_args >= 2 and key not in d:
            print(msg[3])
            return 1
        elif num_of_args == 2:
            return 0
        if num_of_args >= 4 and len(args) < 3:
            print(msg[4])
            return 1
        if num_of_args >= 4 and len(args) < 4:
            print(msg[5])
            return 1
        return 0

    def emptyline(self):
        """Ignores empty spaces"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program at end of file"""
        return True

    def do_create(self, line):
        """Creates a new instance of @cls_name class,
        and prints the new instance's ID.
        Args:
            line(args): Arguments to enter with command: <class name>
            Example: 'create User'
        """
        if (self.my_errors(line, 1) == 1):
            return
        args = line.split(" ")

        """
        args[0] contains class name, create new instance
        of that class updates 'updated_at' attribute,
        and saves into JSON file
        """
        obj = eval(args[0])()
        obj.save()

        print(obj.id)

    def do_show(self, line):
        """Prints a string representation of an instance.
        Args:
            line(line): to enter with command <class name> <id>
            Example: 'show BaseModel 4544-1010-6768'
        """
        if (self.my_errors(line, 2) == 1):
            return
        args = line.split()
        my_dict = storage.all()
        if args[1][0] == '"':
            args[1] = args[1].replace('"', "")
        key = args[0] + '.' + args[1]
        print(my_dict[key])

    def do_destroy(self, line):
        """Deletes an instance of a certain class.
        Args:
            line(args): to enter with command: <class name> <id>
            Example: 'destroy BaseModel 5756-6887-46464'
        """
        if (self.my_errors(line, 2) == 1):
            return
        args = line.split()
        my_dict = storage.all()
        if args[1][0] == '"':
            args[1] = args[1].replace('"', "")
        key = args[0] + '.' + args[1]
        del my_dict[key]
        storage.save()

    def do_all(self, line):
        """Shows all instances, or instances of a certain class
        Args:
            line(args): enter with command (optional): <class name>
            Example: 'all' OR 'all User'
        """
        my_dict = storage.all()
        if not line:
            print([str(x) for x in my_dict.values()])
            return
        args = line.split()
        if (self.my_errors(line, 1) == 1):
            return
        print([str(val) for val in my_dict.values()
               if val.__class__.__name__ == args[0]])

    def do_update(self, line):
        """Updates an instance based on the class name
        and id by adding or updating an attribute
        Args:
            line(args): receives the commands:
            <class name> <id> <attribute name> "<attribute value>"
            Example: 'update BaseModel 4545-5656-5656
                        first_name "Betty"'
        """
        if (self.my_errors(line, 4) == 1):
            return
        args = line.split()
        my_dict = storage.all()
        
        for i in range(len(args[1:]) + 1):
            if args[i][0] == '"':
                args[i] = args[i].replace('"', "")
        key = args[0] + '.' + args[1]
        attr_key = args[2]
        attr_value = args[3]
        
        try:
            if attr_value.isdigit():
                attr_value = int(attr_value)
            elif float(attr_value):
                attr_value = float(attr_value)
        except ValueError:
            pass
        class_attr = type(my_dict[key]).__dict__
        
        if attr_key in class_attr.keys():
            try:
                attr_value = type(class_attr[attr_key])(attr_value)
            except Exception:
                print("Entered wrong value type")
                return
        setattr(my_dict[key], attr_key, attr_value)
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
