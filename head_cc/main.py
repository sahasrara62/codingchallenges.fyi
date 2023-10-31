import click
import sys

def read_stdin():
    try:
        while True:
            line = sys.stdin.readline()
            if not line:
                break
            click.echo(line, nl=False)
    except KeyboardInterrupt:
        pass


def print_file(filename, n, c):
    try:
        if filename == '-':
            read_stdin()
        else:
            with open(filename, 'r') as file:
                if c is not None:
                    content = file.read(c)
                    click.echo(content, nl=False)
                else:
                    if n is None:
                        n = 10  # first 10 line of file will be shown if no file provided
                    for _ in range(n):
                        line = file.readline()
                        if not line:
                            break
                        click.echo(line, nl=False)
    except FileNotFoundError:
        click.echo(f"Error: {filename} not found", err=True)

@click.command()
@click.option('-n', type=int, help='Show the first N lines of the file.')
@click.option('-c', type=int, help='Show the first N bytes of the file.')
@click.argument('files', nargs=-1)
def main(n, c, files):
    if not files:
        print_file('-', n, c)
    else:
        for filename in files:
            if len(files) > 1:
                click.echo(f"==> {filename} <==")
            print_file(filename, n, c)


if __name__ == '__main__':
    main()
