from configparser import ConfigParser
from os import name
from pathlib import Path
from sys import argv


class Zoomy():
    def __init__(self):
        self.zm = ConfigParser()
        P = Path(__file__)
        self.p = P.parent.joinpath('config.zmy')
        del P
        self.zm.read(self.p)
        self.meetings = dict(self.zm._sections["Meetings"])

    def runner(self):
        if argv[1] == 'add' or argv[1] == 'a':
            self.add()
        elif argv[1] == 'delete' or argv[1] == 'd':
            self.delete()
        else:
            self.help()

    def add(self):
        if len(argv) < 4:
            print(
                "Error: Please enter the correct amount of arguments.\n"
                + "Usage: zoomy add [name] [confno]")
            return
        try:
            formatted_meet = f"{argv[3]},{argv[4]}"
        except IndexError:
            formatted_meet = f"{argv[3]}"
        self.zm.set('Meetings', argv[2], formatted_meet)
        try:
            with open(self.p, 'w+') as x:
                self.zm.write(x)
        except PermissionError:
            print("Error: Couldn't write to file.")

    def delete(self):
        if len(argv) < 3:
            print(
                "Error: Please enter the correct amount of arguments.\n"
                + "Usage: zoomy delete [name]")
            return
        if self.zm.has_option("Meetings", argv[2]):
            try:
                self.zm.remove_option("Meetings", argv[2])
                with open(self.p, 'w+') as x:
                    self.zm.write(x)
            except PermissionError:
                print("Error: Couldn't write to file.")
        else:
            print("Error: meeting does not exist.")


def zoomy():
    z = Zoomy()
    z.runner()


if __name__ == "__main__":
    zoomy()
