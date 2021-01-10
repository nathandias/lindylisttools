import click
import models
from models import Band, session, Session

@click.group()
def cli():
    pass

@cli.resultcallback()
def commit_changes(result, **kwargs):
    global session
    session.commit()

@cli.command()
@click.argument('name', required=True, type=str)
@click.argument('url', required=True, type=str)
def add(name, url):
    """ Add a band record with given name and url """
    global session
    band = Band(name=name, url=url)
    session.add(band)

@cli.command()
def show_all():
    """ Display all band records """
    global session
    bands = session.query(Band).order_by(Band.name).order_by(Band.name)
    for band in bands:
        click.echo(band)

@cli.command()
@click.argument('id', required=True, type=int)
def show(id):
    """ Display record for the band with given id """
    global session
    bands = session.query(Band).filter(Band.id==id)
    for band in bands:
        click.echo(band)

@cli.command()
@click.argument('search_string', required=True, type=str)
def like(search_string):
    """ Displays records of all bands that contain the search string """
    global session
    search_string = f'%{search_string}%'
    bands = session.query(Band).filter(Band.name.like(search_string)).order_by(Band.name)
    for band in bands:
        click.echo(band)
