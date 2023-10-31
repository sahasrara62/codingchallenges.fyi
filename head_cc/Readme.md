# Write Your Own head

This challenge is to build your own version of the Unix command line tool head.
It’s a great challenge for beginners and those new to the Unix command line tools.

The Unix command line tools are a great metaphor for good software engineering and they follow the Unix Philosophies of:

- Writing simple parts connected by clean interfaces - each tool does just one thing and provides a simple CLI that handles text input from either files or file streams.
- Design programs to be connected to other programs - each tool can be easily connected to other tools to create incredibly powerful compositions.

### challenge link : [challenge head](https://codingchallenges.fyi/challenges/challenge-head/)

### Presequitive : `python3, git`

### SETUP instructions

- clone repo
- in `head_cc` directory create a virtual environment using command `python3 -m venv venv`
- activate virtual env : `source venv/bin/activate`
- install the package `python3 setup.py install`

### RUN

- once setup is done one can use ```cchead``` command to behave like unix `head` command
- example
  - to read from stdin `cchead`:

    ```
    ❯ cchead
    Enter input (Ctrl-D to end input):
    line1
    line1
    line2
    line2
    line3
    line3
    ```
  - command `cchead main.py` will show first 10 line of file by  default

    ```
    import click
    import sys

    def read_stdin():
        try:
            while True:
                line = sys.stdin.readline()
                if not line:
                    break
                click.echo(line, nl=False)


    ```
  - command `cchead -c 10 main.py`, will show first 10 bytes

    `import cli%`
  - command ```cchead main.py setup.py Readme.md```

    ```
    ❯ cchead main.py setup.py Readme.md
    ==> main.py <==
    import click
    import sys

    def read_stdin():
        try:
            while True:
                line = sys.stdin.readline()
                if not line:
                    break
                click.echo(line, nl=False)
    ==> setup.py <==
    from setuptools import setup

    setup(
        author="prashant",
        author_email="uchiha.rana62@gmail.com",
        description="""A cli tool written in python which mimic linux/unix command head behaviour.
        more info visit: https://codingchallenges.fyi/challenges/challenge-wc
        """,
        version="0.0.1",
        name="head_cc",
    ==> Readme.md <==
    # Write Your Own head

    This challenge is to build your own version of the Unix command line tool head.
    It’s a great challenge for beginners and those new to the Unix command line tools.

    The Unix command line tools are a great metaphor for good software engineering and they follow the Unix Philosophies of:

    - Writing simple parts connected by clean interfaces - each tool does just one thing and provides a simple CLI that handles text input from either files or file streams.
    - Design programs to be connected to other programs - each tool can be easily connected to other tools to create incredibly powerful compositions.

    ```
