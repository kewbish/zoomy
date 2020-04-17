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
            print("Error: No arguments.\nUsage: zoomy [args]")
            return
        if argv[1] == 'add' or argv[1] == 'a':
            self.add()
        elif argv[1] == 'delete' or argv[1] == 'd':
            self.delete()
        elif argv[1] == 'list' or argv[1] == 'l':
            self.list_all()
        elif argv[1]:
            self.open()

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
            with open(self.p, 'w') as x:
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
                with open(self.p, 'w') as x:
                    self.zm.write(x)
            except PermissionError:
                print("Error: Couldn't write to file.")
        else:
            print("Error: meeting does not exist.")

    def open(self):
        joiner = '^' if name == "nt" else '\\'
        opener = 'start' if name == "nt" else 'xdg-open'
        conf = self.meetings.get(argv[1])
        if ',' in conf:
            conf = conf.split(",", 1)
            t = True
        system(f"{opener} zoommtg://zoom.us/join?confno={conf}" if t
               else f"{opener} zoommtg://zoom.us/join?confno={conf[0]}"
               f"{joiner}&pwd={conf[1]}")

    def list_all(self):
        print("You have the following saved meetings:")
        for x in self.meetings:
            conf = self.meetings.get(x).split(",", 1)
            s = f"{x}: Conference number - {conf[0]}"
            if len(conf) > 1:
                s += f", password - {conf[1]}"
            print(s)


def zoomy():
    z = Zoomy()
    z.runner()


if __name__ == "__main__":
    zoomy()
