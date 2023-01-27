import math
import json


class Test(dict):

    def __init__(self, d=None):
        super().__init__(name=None, tasks=[], category=None, mark_range=(1, 12), complete=False)
        if type(d) == dict:
            self.update(d)

    def set_mark_range(self, r):
        self['mark_range'] = r

    def reset(self):
        for i in self['tasks']:
            i.answered = False

    @property
    def complete(self):
        f = True
        for i in self['tasks']:
            if not i.answered:
                f = False
                break
        return f

    @property
    def rperc(self):  # right answers in percent
        return round(len([i for i in self['tasks'] if i['answered']]) / len(self['tasks']) * 100, 2)

    @property
    def rabs(self):  # right answers in absolute
        return len([i for i in self['tasks'] if i['answered']])

    @property
    def mark(self):
        return math.ceil(len([i for i in self['tasks'] if i['answered']]) / len(self['tasks']) * self['mark_range'][1])


def init(d=None):
    return Test(d)
