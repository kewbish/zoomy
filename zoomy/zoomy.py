from configparser import ConfigParser
from os import name
from pathlib import Path
from sys import argv


class Zoomy():
    def __init__(self):
        self.zm = ConfigParser()
        P = Path(__file__)
        self.p = P.parent.joinpath('config.zmy')
        self.zm.read(self.p)
        self.meetings = self.zm._sections["Meetings"]
        if argv[0] == 'add' or argv[0] == 'a':
            self.add()
        elif argv[0] == 'delete' or argv[0] == 'd':
            self.delete()
        else:
            self.run()

    def add(self):
        if len(argv) < 4:
            print(
                "Error: Please enter the correct amount of arguments.\nUsage: zoomy add [name] [confno]")
            return
        try:
            formatted_meet = f"{argv[2]},{argv[3]}"
        except IndexError:
            formatted_meet = f"{argv[2]}"
        self.zm.set("Meetings", argv[1], formatted_meet)
        try:
            with open(self.p, 'w') as x:
                self.zm.write(x)
        except PermissionError:
            print("Error: Couldn't write to file.")
