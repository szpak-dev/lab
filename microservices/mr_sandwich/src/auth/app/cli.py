import click
from flask.cli import with_appcontext

from app.user.create_user import CreateUser


@click.command(name='add_user')
@with_appcontext
def add_user():
    """Add new User to the System"""
    CreateUser('cli_user', 'pass')
