#!/usr/bin/python2
# -*- coding: utf-8 -*-
import click


class Command(click.Command):

    def __init__(self, name, **attrs):
        click.Command.__init__(self, name, **attrs)

    @staticmethod
    def option(func):
        if not hasattr(func, "__click_params__"):
            func.__click_params__ = Command.__click_params__
        return func

    def invoke(self, ctx):
        raise click.ClickException("you should implement this Command")
