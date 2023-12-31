import click
import sys


def extract_data(file_data):
    """
    provide the number of bytes, character, words and lines present in the file
    """
    byte_count = char_count = word_count = line_count = 0
    for line in file_data:
        byte_count += len(line)
        word_count += len(line.split())
        char_count += len(line.decode())
        line_count += 1

    return byte_count, char_count, word_count, line_count


@click.command()
@click.argument("files", nargs=-1, type=click.Path(exists=True))
@click.option(
    "-l",
    "--lines",
    "count_lines",
    is_flag=True,
    help="The number of lines in each input file is written to the standard output.",
)
@click.option(
    "-w",
    "--words",
    "count_words",
    is_flag=True,
    help="The number of words in each input file is written to the standard output.",
)
@click.option(
    "-m",
    "--characters",
    "count_characters",
    is_flag=True,
    help="The number of characters in each input file is written to the standard output.  If the current locale does not support multibyte characters, this is equivalent to the -c option.  This will cancel out any prior usage of the -c option.",
)
@click.option(
    "-c",
    "--bytes",
    "count_bytes",
    is_flag=True,
    help="The number of bytes in each input file is written to the standard output.  This will cancel out any prior usage of the -m option.",
)
def word_count(files, count_lines, count_words, count_characters, count_bytes):
    if count_characters:
        pass
    elif not (count_lines or count_words or count_bytes):
        count_bytes = count_lines = count_words = True

    if not files:
        filename = ""
        files = ["-"]

    for file in files:
        filename = file
        if file == "-":
            data = sys.stdin.buffer
            result = extract_data(file_data=data)
        else:
            with open(file, "rb") as f:
                result = extract_data(file_data=f)

        byte_count, char_count, word_count, line_count = result

        
        if not (count_bytes or count_characters or count_lines or count_words):
            result = f"{line_count}\t{word_count}\t{byte_count}\n"
        else:
            result = f"""{line_count if count_lines else ''}\t{word_count if count_words else ''}\t{byte_count if count_bytes else ''}\t{char_count if count_characters else ''}\t{filename}\n""".strip()
        click.echo(result)


if __name__ == "__main__":
    word_count()
