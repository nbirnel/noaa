from .context import noaa

import unittest

class EndOfDataTest(unittest.TestCase):

    def test_end_of_data(self):
        assert True(noaa.end_of_data({}))



