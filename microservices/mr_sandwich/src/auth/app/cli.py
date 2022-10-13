import click
from flask.cli import with_appcontext

from user.adapters import user_creator


@click.command(name='add_user')
@with_appcontext
def add_user():
    """Add new User to the System"""
    user_creator.create('cli_user', 'pass')
