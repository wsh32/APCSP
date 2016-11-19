#!/usr/bin/env python

"""story.py: Backend class that runs the magic"""

__author__ = "Wesley Soo-Hoo"
__license__ = "MIT"


class Step:
    def __init__(self, message, choices, outcomes):
        self.message = message
        self.choices = choices
        self.outcomes = outcomes

    def add_outcomes(self, outcomes):
        self.outcomes = outcomes

    def is_end(self):
        return False

    def __is_int(self, i):
        try:
            return int(i)
            return True
        except:
            return False

    def go(self):
        print("\n"+self.message)
        i = 1
        for j in self.choices:
            print(str(i) + ":\t" + j)
            i += 1
        while True:
            choice = input('What do you pick?\n>>\t')
            if not self.__is_int(choice):
                print("That is not a valid choice!")
                continue
            elif int(choice) > len(self.outcomes):
                print("That is not a valid choice!")
                continue
            else:
                self.outcomes[int(choice)-1].go()
                break


class EndStep(Step):
    def __init__(self, message, first_step):
        self.message = message
        self.first_step = first_step

    def is_end(self):
        return True

    def go(self):
        print(self.message)
        print("\nI wonder how differently that could've played out...")
        print("Would you like to play again?")
        print("1: Yes")
        print("2: No")
        if input(">>\t") == '1':
            self.first_step.go()


def read_csv(filename):
    file = open(filename, 'r')
    raw = file.read()
    lines = raw.split("\n")
    cells = []
    for i in lines:
        cells.append(i.split('\t'))
    steps = []
    for i in cells:
        if i[2] == "_END_STEP":
            s = EndStep(i[1], steps[0])
        elif i[4] == "-":
            s = Step(i[1], [i[2], i[3]], [])
        else:
            s = Step(i[1], [i[2], i[3], i[4]], [])
        steps.append(s)
    for i in range(len(steps)):
        if not steps[i].is_end():
            if i[7] == "-":
                steps[i].add_outcomes([steps[int(cells[i][4])], steps[int(cells[i][5])]])
            else:
                steps[i].add_outcomes([steps[int(cells[i][5])], steps[int(cells[i][6])], steps[int(cells[i][7])]])
    return steps
