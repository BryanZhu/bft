#!/usr/bin/python2
# -*- coding: utf-8 -*-
import click
from command import *


@click.group()
def z():
    """z subgroup operation command"""


@z.command(name="baz", cls=Baz)
@Baz.option
def baz():
    """baz command info"""
