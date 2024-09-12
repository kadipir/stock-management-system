#!/usr/bin/python3
"""define the stock system console"""
import cmd
import re
from models.__init__ import storage
from shlex import split


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(',') for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(',') for i in lexer]
            retl.append(brackets.group())
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(',') for i in lexer]
        retl.append(curly_braces.group())
        return retl


class Stock(cmd.Cmd):
    """defines the stock command interpreter
    Attributes:
    prompt (str): the command prompt.
    """
    prompt = "(stock)"
    _classes_ = {}
    def emptyline(self):
        """do nothing upon receiving an empty line."""
        pass


    def default(self, arg):
        """default behaviour for cd module when input is invalid"""
        argdict = {"all" : self.do_all,
                "show" : self.do_show,
                "destroy" : self.do_destroy,
                "count" : self.do_count,
                "update" : self.do_update
                }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]],arg[match.span()[1]:]]
            match = re.serach(r"\((,*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]],match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(arg[0],command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return false


    def do_quit(self, arg):
        """quit command to exit the progarm"""
        return True


    def do_EOF(self,arg):
        """EOF signal to exit the program"""
        print("")
        return True


    def do_create(self,arg):
        """usage: create <class>
        Create a new class instance and prints its id.
        """
        argl = parse(arg)
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in Stock.__classes:
            printprint("** class does not exist **")
        else:
            print(eval(argl[0]()).id)
            storage.save


    def do_show(self,arg):
        """usage: show <class> or <class>.show(<id>)
        dispaly the string representation of a class instance of a given id.
        """
        argl = parse(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** Classs name missing **" )
        elif arg[0] not in Stock.__classes:
            print("** class does not exist **")
        elif len(argl) == 1:
            print("** instance id is missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict.keys:
            print("** no instance id **")
        else:
            print(objdict["{}.{}".format(argl[0], argl[1])])

    
    def do_destroy(self,arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id.
        """
        argl = parse(arg)
        if len(argl) == 0:
            print("** Classs name missing **" )
        elif arg[0] not in Stock.__classes:
            print("** class does not exist **")
        elif len(argl) == 1:
            print("** instance id is missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict.keys:
            print("** no instance id **")
        else:
            del objdict["{}.{}".format(argl[0], argl[1])]
            storage.save
    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Display string represenation of all instances of a given class.
        if no class is specified, displays all instantiated objects."""
        argl = parse(arg)
        if len(argl) > 0 and argl[0] not in Stock.__classes:
            print("** class soes not exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(argl) > 0 and arg[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(argl) == 0:
                    objl.append(obj.__str__())
            print(objl)


    def do_count(self,arg):
        """Usage: count <class> or <class>.count()
        retrieve the number of instances of agiven class."""
        argl = parse(arg)
        count = 0
        for obj in storage.all().values():
                if argl[0] == obj.__class__.__name__:
                    count += 1
        print(count)


if __name__ == "__main__":
    Stock().cmdloop()
