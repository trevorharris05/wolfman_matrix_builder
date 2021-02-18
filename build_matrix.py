#!/home/trevor/venvs/py3.8/bin/python
from pprint import pprint
from typing import List
import clipboard
import pyperclip


def main(data_set_path: str = None):
    if data_set_path is None:
        data_set_path = './temp.csv'

    with open(data_set_path, 'r') as f:
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


if __name__ == "__main__":
    main()
