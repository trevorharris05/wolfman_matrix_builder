import unittest
from unittest import TestCase

from build_matrix import main


class Test(TestCase):
    def test_main(self):
        main()

    def test_alpha_spaces(self):
        main('./test_files/alpha_spaces.csv')

    def test_standard(self):
        main('./test_files/standard.csv')


if __name__ == '__main__':
    unittest.TestCase()
