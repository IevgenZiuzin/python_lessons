import json
import string


class Task(dict):

    def __init__(self, d=None):
        super().__init__(question=None, variants=None, answers=None, right_answered=False, answered=False)
        if type(d) == dict:
            self.update(d)

    def json(self):
        return json.dumps(self)

    def check(self, q):
        self['answered'] = True
        if q in self['answers']:
            self['right_answered'] = True

    def marked_variants(self):
        return dict([(string.ascii_lowercase[i], k) for i, k in enumerate(list(map(lambda x: str(x), self['variants'])))])


def init(q, v, a):
    t = Task({'question': q, 'variants': v, 'answers': a})
    t['variants'] = t.marked_variants()
    return t

