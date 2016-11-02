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
        except:
            return False

    def go(self):
        print(self.message)
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
    def __init__(self, message):
        self.message = message

    def is_end(self):
        return True

    def go(self):
        print(self.message)
