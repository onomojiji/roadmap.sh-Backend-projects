import click

from main import *

# create click group
@click.group()
def cli():
    pass

# create click command to add task
@cli.command()
@click.argument('category')
@click.argument('description')
@click.argument('amount', type=float)
def add(category, description, amount):
    add_espense(category, description, amount)

@cli.command()
@click.argument('task_id', type=int)
@click.argument('new_description')
def update(task_id, new_description):
    update_espense_description(task_id, new_description)

@cli.command()
@click.argument('task_id', type=int)
def delete(task_id):
    delete_espense(task_id)

@cli.command()
def list():
    print_espenses_list()

@cli.command()
def summary():
    summary_espenses_amount()

@cli.command()
@click.argument('month', type=int)
@click.argument('year', type=int)
def summary_month(month, year):
    summary_espenses_amount_for_month(month, year)

@cli.command()
@click.argument("year", type=int)
@click.argument("month", type=int)
@click.argument("amount", type=float)
def add_budget(year, month, amount):
    add_budget_for_month(amount, month, year)


if __name__ == '__main__':
    cli()