## Write Your Own cat Tool

challenge link: [write own cat tool](https://codingchallenges.fyi/challenges/challenge-cat)

UNIX CLI command CAT implementation in python

### Presequitive
- programming language: `Python3`
    
### How to start
1. clone the project
    `git clone https://github.com/sahasrara62/codingchallenges.fyi.git`
2. go into cat_tool project `cd codingchallenges.fyi/cat_tool`
3. Make a virtual env `python3 -m venv venv`
4. activate virtual env `source venv/bin/activate`
5. install requirements `python3 -m pip install .`

### test code 
After installing the package ie `cat_tool`
run the test as

```
py_cat tests_files/test.txt
py_cat tests_files/test.txt -n
py_cat tests_files/test.txt -n -b
py_cat tests_files/test.txt tests_files/text2.txt
cat tests_files/test.txt | py_cat -
cat tests_files/test.txt | py_cat - -n
```

### using only script
1. install required package in the python environment
    `python3 -m pip install -r requirements.txt`
2. run command `python3 unix_cat/pycat.py <filename> <option>`
