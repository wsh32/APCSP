#!/usr/bin/env python

"""main.py: This is where the magic happens!"""

import story

__author__ = "Wesley Soo-Hoo, Spencer Hu"
__license__ = "MIT"

if __name__ == '__main__':
    i = story.read_csv('s.txt')
    i[0].go()
