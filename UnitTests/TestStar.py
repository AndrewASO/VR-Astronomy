
import unittest
import pandas as pd
import numpy as np
import sys
import os
from VRAstronomy.Star import Star
from VRAstronomy.test import Test

class TestStar(unittest.TestCase):

    def setUp(self):
        #Create a mock Dataframe of all the required fields
        self.mock_row = pd.Series( {
            'ra': 10.0,
            'dec': 20.0,
            'pmra': 30.0,
            'pmdec': 40.0,
            'mag': 2.5,
            'ci': 0.3,
            'dist': 100.0,
            'proper': 'Test Star',
            'con': 'TES',
        })

    def testStarCreation(self):
        #self.setUp()
        star = Star(self.mock_row)
        #star.testPrint()

        
        #Testing core properties
        self.assertEqual(star.ra, 10.0)
        self.assertEqual(star.dec, 20.0)
        self.assertEqual(star.pmra, 30.0)
        self.assertEqual(star.pmdec, 40.0)
        self.assertEqual(star.mag, 2.5)
        self.assertEqual(star.ci, 0.3)
        
        #Testing optional properties
        self.assertEqual(star.dist, 100.0)
        self.assertEqual(star.proper, 'Test Star')
        self.assertEqual(star.con, 'TES')
        

    def test(self):
        testPrint = Test()
        testPrint.testPrint()


if __name__ == '__main__':
    unittest.main()