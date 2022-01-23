#!/usr/bin/python2
# -*- coding: utf-8 -*-
import click

from command import Command


class Bar(Command):

    def __init__(self, name, **attrs):
        Command.__init__(self, name, **attrs)

    @staticmethod
    def option(func):
        if not hasattr(func, "__click_params__"):
            func.__click_params__ = Bar.__click_params__
        return func

    def invoke(self, ctx):
        click.echo("Bar Command invoked~")
