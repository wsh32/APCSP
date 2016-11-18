#!/usr/bin/env python

"""hangman.py: Backend class that runs the magic"""

from . import sets

__author__ = "Wesley Soo-Hoo"
__license__ = "MIT"


class hangman:
    def __init__(self, word):
        self.word = word.upper()
        self.shown = ""
        self.guessed = []
        self.step = 0
        for i in word:
            if i != " ":
                self.shown += "-"
            else:
                self.shown += " "

    def trial(self, guess):
        if len(guess) != 1:
            print("Please guess one letter!")
        elif guess.upper() in self.guessed:
            print("You have already guessed that letter!")
        elif guess.upper() in self.word:
            s = list(self.shown)
            for i in range(len(self.word)):
                if self.word[i] == guess.upper():
                    s[i] = guess.upper()
            self.shown = "".join(s)
            self.guessed.append(guess.upper())
            self.guessed.sort()
            return True
        else:
            self.guessed.append(guess.upper())
            self.guessed.sort()
            self.step += 1
            return False

    def print_shown(self):
        print(self.shown)

    def print_hangman(self):
        for i in sets.hangman[self.step]:
            print(i)

    def print_guessed(self):
        if len(self.guessed) == 0:
            print("No Letters Previously Guessed")
        else:
            toprint = "Letters Guessed: "
            for i in self.guessed:
                toprint += i
                toprint += " "
            print(toprint)

    def is_dead(self):
        return self.step == len(sets.hangman) - 1

    def is_won(self):
        return not "-" in self.shown

    def go(self):
        while not self.is_won() and not self.is_dead():
            self.print_shown()
            self.print_hangman()
            self.print_guessed()
            print("What is your guess?")
            guess = input(">> ")
            self.trial(guess)

        self.print_shown()
        self.print_hangman()
        self.print_guessed()
        if self.is_won():
            print("Congratulations! You win!")
        elif self.is_dead():
            print("LOL YOU LOSE")