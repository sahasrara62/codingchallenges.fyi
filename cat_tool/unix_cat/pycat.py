import click
import sys
import os


def extract_data(files):
    for file in files:
        if file == "-":
            stdin_data = sys.stdin.buffer.read().decode().split("\n")
            for line in stdin_data:
                yield line
        else:
            try:
                if not os.path.isfile(file):
                    raise click.Abort(f"Error: No such File {file} exists")
            except click.Abort as e:
                click.echo(e)
                continue
            with open(file, mode='r') as f:
                for line in f:
                    yield line


@click.command()
@click.argument("files", nargs=-1, type=click.STRING)
@click.option(
    "-n",
    "number",
    is_flag=True,
    help="number all output lines",
)
@click.option(
    "-b",
    "number_nonblank",
    is_flag=True,
    help="number nonempty output lines, overrides -n",
)
def py_cat(files, number, number_nonblank):
    data = extract_data(files)
    if number_nonblank:
        number = True
    index = 1
    for line in data:
        index_val = str(index)
        if number_nonblank :
            if not len(line.strip()) == 0:
                index+=1
            else:
                index_val = ''
        else:
            index +=1
        string  = f"{'    ' + index_val+' ' if number else ''}{line.rstrip()}"

        click.echo(string)


if __name__ == "__main__":
    py_cat()
