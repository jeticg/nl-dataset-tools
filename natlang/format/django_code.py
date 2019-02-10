# -*- coding: utf-8 -*-
# Python version: 3
#
# Django Dataset Code Loader class
# Simon Fraser University
# Ruoyi Wang, Jetic Gū
#
# For loading the code as a sequence of tokens
import json
import os
import sys


class Code:
    def __init__(self, tokens, ty_list):
        self.value = tokens
        self.ty_list = ty_list
        assert len(self.value) == len(self.ty_list)
        self.sketch = []
        self.createSketch()  # writes to self.sketch

    def __iter__(self):
        return iter(self.value)

    def __len__(self):
        return len(self.value)

    def __repr__(self):
        return "<DjangoCode: " + str(self.value) + ">"

    def createSketch(self):
        self.sketch = []
        for tk, ty in zip(self.value, self.ty_list):
            if ty in ('NAME', 'STRING', 'NUMBER'):
                self.sketch.append(ty)
            else:
                self.sketch.append(tk)

    def export(self):
        return " ".join(self.value)


def load(file, linesToLoad=sys.maxsize):
    with open(os.path.expanduser(file)) as f:
        content = [line.strip() for line in f][:linesToLoad]
    result = []
    for line in content:
        entry = json.loads(line)
        result.append(Code(entry['token'], entry['type']))
    return result


if __name__ == '__main__':
    loaded = load(
        '/Users/ruoyi/Projects/PycharmProjects/data_fixer/django_exported/dev.jsonl')
