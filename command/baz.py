#!/usr/bin/python2
# -*- coding: utf-8 -*-
import click

from command import Command


@click.option("-a", "--address", is_flag=True, help="show your address")
@click.option("-s", "--status", help="show your status info")
class Baz(Command):

    def __init__(self, name, **attrs):
        Command.__init__(self, name, **attrs)

    @staticmethod
    def option(func):
        if not hasattr(func, "__click_params__"):
            func.__click_params__ = Baz.__click_params__
        return func

    def invoke(self, ctx):
        click.echo("Baz Command invoked~")
        address = ctx.params.get("address", False)
        status = ctx.params.get("status", None)
        if address:
            click.echo("address is true, show you address info")
        if status is not None:
            click.echo("status is: {}".format(status))

