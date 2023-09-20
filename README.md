usage: VersionNameGenerator [-h] [-s START_LETTER] [-f FILES [FILES ...]]

Generate a version name from provided files.

optional arguments:
  -h, --help            show this help message and exit
  -s START_LETTER, --start-letter START_LETTER
                        Letter first word should start with. If too many letters only use the first
  -f FILES [FILES ...], --files FILES [FILES ...]
                        File with words to use in generating name. Can be used several times, picking random word from each file in order specified.

Example: ./main.py -s s --file example-words/verbs.txt example-words/animals.txt