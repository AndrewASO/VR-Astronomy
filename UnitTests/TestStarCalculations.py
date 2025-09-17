
'''
Testing star calculations 
'''

import unittest
import pandas as pd
import numpy as np
from VRAstronomy.Star import Star
from VRAstronomy.StarCalculations import StarCalculations

class TestStarCalculations(unittest.TestCase):

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

        self.star = Star(self.mock_row)
        self.starCalculator = StarCalculations()    #Why not just initiate this with star ? Going to be doing that later then 
        #directly grabbing the data from the stars to be used in star calculations so there's not as many redundant lines of code
        #to grab the variables from the star then putting it into starcalculations, so only the StarCalculations functions will need
        #to be called without any extra work

    def testCalculationPos(self):
        pass

    def testCalculateSize(self):
        pass

    def testCalculateColor(self):
        #starCalculator = StarCalculations()
        self.color = self.starCalculator.calculateColor( self.star.ci )
        self.assertEqual( self.color, (1.0, 1.0, 0.8) )



if __name__ == '__main__':
    unittest.main()