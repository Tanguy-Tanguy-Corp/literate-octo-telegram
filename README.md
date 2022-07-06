# literate-octo-telegram

Python integration of a scrabble game

## Virtual Environment
### Create the virtual environment
```
$ python -m venv .venv
```
### Activate the virtual environment
```
$ source .venv/bin/activate
```
### Install the requirements
```
$ pip install -r requirements.txt
```

## Test, pytest and coverage
### To run the tests
```
$ pytest (with -v flag for verbose outputs)
```
### To measure the code coverage of the test
```
$ coverage run -m pytest
```
```
$ coverage report
```
output
```
Name                                        Stmts   Miss Branch BrPart  Cover
-----------------------------------------------------------------------------
scrabble_python/__init__.py                     1      0      0      0   100%
scrabble_python/errors/__init__.py              1      0      0      0   100%
scrabble_python/errors/scrabble_errors.py       6      0      6      0   100%
scrabble_python/items/__init__.py               5      0      0      0   100%
scrabble_python/items/board.py                 92      8     60      5    91%
scrabble_python/items/helpers.py               36     13     22      3    55%
scrabble_python/items/player.py                10      0      6      1    94%
scrabble_python/items/purse.py                 30      1     14      0    98%
scrabble_python/items/tile.py                  21      2      4      0    92%
scrabble_python/items/word.py                  30      3     12      1    90%
scrabble_python/scrabble.py                    26      1     12      3    89%
-----------------------------------------------------------------------------
TOTAL                                         258     28    136     13    87%
```
### To generate a HTML report (in ./htmlcov)
```
$ coverage html
```