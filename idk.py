from random import *
s = randint(1,7)
if s == 7:
    e = randint(1,13)
else:
    e = randint(1,22)

class Picker:
    def __init__(self, series, episode):
        self.series = series
        self.episode = episode
    def choose(series, episode):
        print("You are watching S%dE%d" %(series, episode))

Picker.choose(s,e)