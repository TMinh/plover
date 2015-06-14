import json
from collections import OrderedDict

class Keymap():
    def __init__(self, assignments):
        self.keymap = OrderedDict(assignments)
        self.assignments = assignments

    def get(self):
        return self.keymap

    def __str__(self):
        return json.dumps(self.assignments)

    def to_dict(self):
        """Return a dictionary from keys to steno keys."""
        result = {}
        for stenoKey, producers in self.keymap.items():
            for key in producers:
                result[key] = stenoKey
        return result

    @staticmethod
    def from_string(string):
        assignments = json.loads(string)
        return Keymap(assignments)

    @staticmethod
    def from_rows(rows):
        """Convert a nested list of strings (e.g. from a ListCtrl) to a keymap."""
        assignments = []
        for row in rows:
            stenoKey = row[0]
            keylist = row[1].strip().split()
            assignments.append([stenoKey, keylist])
        return Keymap(assignments)

    @staticmethod
    def default():
        return Keymap([
            ["S-", ["a","q"]],
            ["B-", ["w"]],
            ["T-", ["s"]],
            ["G-", ["e"]],
            ["D-", ["d"]],
            ["R-", ["r"]],
            ["L-", ["f"]],
            ["A-", ["c"]],
            ["U-", ["v"]],
            ["*" , ["t","g","y","h"]],
            ["-O", ["n"]],
            ["-I", ["m"]],
            ["-R", ["u"]],
            ["-L", ["j"]],
            ["-M", ["i"]],
            ["-B", ["k"]],
            ["-G", ["o"]],
            ["-D", ["l"]],
            ["-S", ["p"]],
            ["-T", [";"]],
            ["-N", ["["]],
            ["-E", ["'"]],
            ["#" , ["1","2","3","4","5","6","7","8","9","0","-","="]]
        ])
