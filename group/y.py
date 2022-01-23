#!/usr/bin/python2
# -*- coding: utf-8 -*-
import click
from command import *


@click.group()
def y():
    """y subgroup operation command"""


@y.command(name="bar", cls=Bar)
def bar():
    """bar command info"""
