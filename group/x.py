#!/usr/bin/python2
# -*- coding: utf-8 -*-
import click
from command import *


@click.group()
def x():
    """x subgroup operation command"""


@x.command(name="foo", cls=Foo)
def foo():
    """foo command info"""
