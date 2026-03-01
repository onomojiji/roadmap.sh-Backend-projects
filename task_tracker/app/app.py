import click

from main import *

# create click group
@click.group()
def cli():
    pass

# create click command to add task
@cli.command()
@click.argument('description')
def add(description):
    add_task(description)

@cli.command()
@click.argument('task_id', type=int)
@click.argument('new_description')
def update(task_id, new_description):
    update_task(task_id, new_description)

@cli.command()
@click.argument('task_id', type=int)
def delete(task_id):
    delete_task(task_id)

@cli.command()
@click.argument('task_id', type=int)
@click.argument('new_status')
def change_status(task_id, new_status):
    change_task_status(task_id, new_status)

@cli.command()
@click.argument('status', required=False)
def list(status):
    tasks = list_tasks(status)

if __name__ == '__main__':
    cli()