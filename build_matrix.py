#!/usr/bin/env python3
from pprint import pprint
from typing import List
import urllib.parse


def main(data_set_path: str = None):

    debug = False

    if data_set_path is None:
        data_set_path = './temp.csv'

    with open(data_set_path, 'r') as f:
        raw_l: List[str] = f.read().splitlines()

    # Use Case
    print("You passed in this list: {}".format(raw_l))
    raw_s: str = '{' + ",".join(map(lambda row: '{' + row + '}', raw_l)) + '}'
    if debug:   
        print("WolframAlpha matrix: {}".format(raw_s))

    # Build Wolfram command
    wolf_prefixes = ['row reduce {}', 'determinant {}', 'null space {}', 'eigenvalues {}', 'eigen vectors {}',
                     'x\' = {}x']
    wolf_prefix = wolf_prefixes[0]
    wolf_command = wolf_prefix.format(raw_s)
    print("Suggested command: {}".format(wolf_command))

    base_url = 'https://www.wolframalpha.com/input/?i='
    safe_string = base_url + urllib.parse.quote_plus(wolf_command)
    print(f"Go to Wolfram: {safe_string}")


if __name__ == "__main__":
    main()
