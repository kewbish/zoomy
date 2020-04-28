from configparser import ConfigParser
from os import name, system, path as pth
from sys import argv


class Zoomy():
    def __init__(self):
        self.zm = ConfigParser()
        self.p = pth.join(pth.dirname(__file__), 'config.zmy')
        if not pth.isfile(self.p):
            with open(self.p, 'w') as x:
                x.write('[Meetings]')
        self.zm.read(self.p)
        self.meetings = dict(self.zm._sections["Meetings"])

    def runner(self):
        if len(argv) == 1:
            self.help()
            return
        if argv[1] in ('add', 'a'):
            self.add()
        elif argv[1] in ('delete', 'd'):
            self.delete()
        elif argv[1] in ('list', 'l'):
            self.list_all()
        elif argv[1] in ('path', 'p'):
            self.path()
        elif argv[1] in ('--help', '--h'):
            self.help()
        elif argv[1]:
            self.open()

    def help(self):
        print("\nWelcome to Zoomy - a Zoom utility for the terminal.")
        print("Commands:\n- zmy [add/a] [alias] [confno] [*pwd]")
        print("- zmy [delete/d] [alias]")
        print("- zmy [list/l]")
        print("- zmy [path/p]")
        print("- zmy [--help/--h]")
        print("Created by Kewbish - https://github.com/kewbish/zoomy")

    def add(self):
        if len(argv) < 4:
            print(
                "Error: Please enter the correct amount of arguments.\n"
                + "Usage: zmy [add/a] [name] [confno] [*pwd]")
            return
        if argv[2] in ['add', 'a', 'delete', 'd', 'list', 'l', 'path', 'p',
                       '--help', '--h']:
            print("Error: Invalid name, alias cannot be made.")
            return
        try:
            formatted_meet = f"{argv[3]},{argv[4]}"
        except IndexError:
            formatted_meet = f"{argv[3]}"
        self.zm.set('Meetings', argv[2], formatted_meet)
        try:
            with open(self.p, 'w') as x:
                self.zm.write(x)
        except PermissionError:
            print("Error: Couldn't write to file.")

    def delete(self):
        if len(argv) < 3:
            print(
                "Error: Please enter the correct amount of arguments.\n"
                + "Usage: zmy [delete/d] [name]")
            return
        if self.zm.has_option("Meetings", argv[2]):
            try:
                self.zm.remove_option("Meetings", argv[2])
                with open(self.p, 'w') as x:
                    self.zm.write(x)
            except PermissionError:
                print("Error: Couldn't write to file.")
        else:
            print("Error: Meeting does not exist.\nRun zmy add [alias] "
                  "[confno] [*pwd] first, then `zmy [alias]`")

    def open(self):
        joiner = '^' if name == "nt" else '\\'
        opener = 'start' if name == "nt" else 'xdg-open'
        if self.zm.has_option("Meetings", argv[1]):
            conf = self.meetings.get(argv[1])
            t = True
            if ',' in conf:
                conf = conf.split(",", 1)
                t = False
            system(f"{opener} zoommtg://zoom.us/join?confno={conf}" if t
                   else f"{opener} zoommtg://zoom.us/join?confno={conf[0]}"
                   f"{joiner}&pwd={conf[1]}")
        else:
            print("Error: Meeting does not exist.\nRun zmy add [alias] "
                  "[confno] [*pwd] first, then `zmy [alias]`")

    def list_all(self):
        print("You have the following saved meetings:")
        for x in self.meetings:
            conf = self.meetings.get(x).split(",", 1)
            s = f"{x}: Conference number - {conf[0]}"
            if len(conf) > 1:
                s += f", password - {conf[1]}"
            print(s)

    def path(self):
        print(f"The path to your .zmy file is {self.p}.")


def zoomy():
    z = Zoomy()
    z.runner()


if __name__ == "__main__":
    zoomy()
