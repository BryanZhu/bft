#!/usr/bin/python2
# -*- coding: utf-8 -*-
import click

from command import Command


class Foo(Command):

    def __init__(self, name, **attrs):
        Command.__init__(self, name, **attrs)

    @staticmethod
    def option(func):
        if not hasattr(func, "__click_params__"):
            func.__click_params__ = Foo.__click_params__
        return func

    def invoke(self, ctx):
        click.echo("Foo Command invoked~")
