## [Write Your Own wc Tool](https://codingchallenges.fyi/challenges/challenge-wc)
This challenge is to build your own version of the Unix command line tool wc!

The Unix command line tools are a great metaphor for good software engineering and they follow the Unix Philosophies of:

Writing simple parts connected by clean interfaces - each tool does just one thing and provides a simple CLI that handles text input from either files or file streams.
Design programs to be connected to other programs - each tool can be easily connected to other tools to create incredibly powerful compositions

More challenge info : [challenge link](https://codingchallenges.fyi/challenges/challenge-wc)

Presequtive: Python

cli library tool used: [click](https://palletsprojects.com/p/click/)
#### setup
1. python version used: 3.11.5
2. follow below steps:
   1. clone repo: `git clone <repo link>`
   2. `cd WORD_COUNT`
   3. make a virtual environment: `python3 -m venv venv`
   4. activate virtualenvironment: `source venv/bin/activate`
   5. install require packages `python3 -m pip install --editable .`
   
### feature
this tool provide the word count, line count, byte count and character count.

command-line argument used for these above are
1. word count: `-w` or `--words`
2. line count: `-l` or `--lines`
3. character count: `-m` or `--characters`
4. byte count: `-c` or `--bytes`

### How to use
1. complete the setup
2. run command `py_wc < -l | -m | -c | -w> <file1> <file2> <file2>` 
3. with stdin `cat filename | py_wc <-l | -m | -c | -w>`
   
Note : `py_wc` is named as command to run this project