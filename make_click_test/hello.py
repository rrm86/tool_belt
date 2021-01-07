import click

@click.command(help='This is just a hello app.')
@click.option('--name', prompt="I need your name", help='Need Name')
@click.option('--color', prompt="I need your color", help="This is your color")
def hello(name, color):

    if name == "Thor":
        click.echo('Thor your are always red')
        click.echo(click.style(f'Hello World {name}', fg="red"))
    else:
        pass

if __name__ == "__main__":
    hello()