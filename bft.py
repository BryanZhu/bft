#!/usr/bin/python2
# -*- coding: utf-8 -*-
import os.path

import click
from group import *


@click.group()
def bft():
    """build your fast tool"""


def load_sub_groups():
    _bft_dir = os.path.dirname(os.path.abspath(__file__))
    _group_dir = os.path.join(_bft_dir, "group")
    sub_groups = []
    for filename in os.listdir(_group_dir):
        if filename.endswith(".py") and filename != "__init__.py":
            sub_groups.append(filename[:-3])
    for group in sub_groups:
        bft.add_command(eval(group))


load_sub_groups()

if __name__ == "__main__":
    bft()
