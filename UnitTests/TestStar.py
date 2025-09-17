
'''
This will test the Star class creation and assure that everything is running correctly during its initial creation.
'''

import unittest
import pandas as pd
import numpy as np
from VRAstronomy.Star import Star

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
            'id': 1                 #Optional and might not be needed later on, was only here for testing 
            #if this line of code worked || self.id = int(df_row.get("id")) if pd.notna(df_row.get("id")) else None 
        })

    def testStarCreation(self):
        star = Star(self.mock_row)
        
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


if __name__ == '__main__':
    unittest.main()