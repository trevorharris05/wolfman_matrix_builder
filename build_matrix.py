#!/home/trevor/venvs/py3.8/bin/python
from pprint import pprint
from typing import List
import clipboard
import pyperclip


if __name__ == "__main__":
    with open('./temp.csv', 'r') as f:
        raw_l: List[str] = f.read().splitlines()


    # Use Case   
    print("You passed in this list: {}".format(raw_l))
    raw_s: str = '{' + ",".join(map(lambda row: '{' + row + '}', raw_l)) + '}'
    print("WolframAlpha matrix: {}".format(raw_s))

    # Nice to have (not working)
    wolf_command = 'row reduce ' + raw_s
    clipboard.copy(wolf_command)
    pyperclip.copy(wolf_command)
    print("Copied to clipboard")
