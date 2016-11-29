#!/usr/bin/env python

"""main.py: This is where the magic happens!"""

import story

__author__ = "Wesley Soo-Hoo, Spencer Hu"
__license__ = "MIT"


if __name__ == '__main__':
    steps = story.read_csv('s.txt')
    current_step = steps[0]
    score = 0

    while True:
        score += current_step.score
        if not current_step.is_end():
            print("\n\nCurrent Score:\t" + str(score) + " points")
            current_step.print_message()
            current_step = current_step.ask_choice()
        else:
            current_step.print_message()
            print("The End! Your final score was:\t" + str(score) + " points")
            if current_step.ask_repeat():
                score = 0
                current_step = steps[0]
            else:
                break
