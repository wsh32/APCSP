#!/usr/bin/env python

"""story.py: Backend class that runs the magic"""

__author__ = "Wesley Soo-Hoo"
__license__ = "MIT"


class Step:
    def __init__(self, message, score, choices, outcomes):
        self.message = message
        self.score = score
        self.choices = choices
        self.outcomes = outcomes

    def add_outcomes(self, outcomes):
        self.outcomes = outcomes

    def is_end(self):
        return False

    @staticmethod
    def __is_int(i):
        try:
            return int(i)
            return True
        except:
            return False

    def print_message(self):
        print("\n" + self.message)

    def ask_choice(self):
        i = 1
        for j in self.choices:
            print(str(i) + ":\t" + j)
            i += 1
        while True:
            choice = input('\nWhat do you pick?\n>>\t')
            if not self.__is_int(choice):
                print("That is not a valid choice!")
                continue
            elif int(choice) > len(self.outcomes) or int(choice) <= 0:
                print("That is not a valid choice!")
                continue
            else:
                return self.outcomes[int(choice) - 1]

    '''Depreciated'''
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
            elif int(choice) > len(self.outcomes) or int(choice) <= 0:
                print("That is not a valid choice!")
                continue
            else:
                self.outcomes[int(choice)-1].go()
                break


class EndStep(Step):
    def __init__(self, message, first_step, score):
        self.message = message
        self.first_step = first_step
        self.score = score

    def is_end(self):
        return True

    def print_message(self):
        print("\n" + self.message)

    def ask_repeat(self):
        while True:
            print("\nI wonder how differently that could've played out...")
            print("Would you like to play again?")
            print("1: Yes")
            print("2: No")
            return input(">>\t") == "1"

    '''Depreciated'''
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
            s = EndStep(i[1], steps[0], int(i[8]))
        elif i[4] == "-":
            s = Step(i[1], int(i[8]), [i[2], i[3]], [])
        else:
            s = Step(i[1], int(i[8]), [i[2], i[3], i[4]], [])
        steps.append(s)
    for i in range(len(steps)):
        if not steps[i].is_end():
            if cells[i][7] == "-":
                if int(cells[i][5]) > len(steps)-1:
                    print(int(cells[i][5]))
                if int(cells[i][6]) > len(steps)-1:
                    print(int(cells[i][6]))
                steps[i].add_outcomes([steps[int(cells[i][5])], steps[int(cells[i][6])]])
            else:
                steps[i].add_outcomes([steps[int(cells[i][5])], steps[int(cells[i][6])], steps[int(cells[i][7])]])
    return steps
