

'''
This is the object class for Star to be used for StarCatalog. It'll have the base values that're needed from calculations from the star csv
that's providing all of the non-calculated values. Then the Star object will go through StarCalculations.py to get the position for the star
in azimuth & altitude within a list, then the calculated visual size and color. This'll be stored in the Star Obj for later retrieval. There's a 
function for just returning the calculated values for ease of access as a list and there's 2 functions for setting a specified value or returning
one. In the future, there might be additional values added as backups for anything planned in the future. Will look at the time and see if there's
a huge difference in the time when storing the additional values or if it would be negligible.
All of the variables that aren't calculated will be from the epoch & equinox 2000.0
'''

import pandas as pd

class Star:

    '''
    The Object is initialized with a dataframe row that's specified to the one Star being grabbed. For quick access of specific stars, there's
    the identification values of id & proper. ID would be more nuanced if you needed a specific star, Proper would be for a well-known name of a 
    star. Con would be used for constellation and there are plans to use it in the future to enable/disable constellations, so all of the stars
    would be grouped up into it that're in the same Con. 
    Initial variables will be used for calculations in StarCalculations.
    Visual variables are variables that would be needed for visual details like the star's color or luminosity.
    Fallback variables would be variables used for other calculations or if some of the calculations wouldn't work if one of the variables
    are blank and are necessary
    Calculated Variables are variables that have been calculated from StarCalculations.
    '''
    def __init__(self, df_row):

        #Initial variables required for calculations
        self.ra = float(df_row['ra'])                                               #Right Ascension
        self.dec = float(df_row['dec'])                                             #Declination
        self.pmra = float(df_row['pmra'])                                           #Proper Motion Right Ascension
        self.pmdec = float(df_row['pmdec'])                                         #Proper Motion Declination 
        self.dist = float(df_row['dist'])                                           #Distance

        #Visual Variables
        self.mag = float(df_row['mag'])                                             #Apparent Visual Magnitude
        self.ci = float(df_row['ci'])                                               #Color Index

        #Identification Variables
        self.id = int(df_row.get("id")) if pd.notna(df_row.get("id")) else None     #Database Primary Key
        self.proper = str(df_row['proper'])                                         #Proper Name
        self.con = str(df_row['con'])                                               #Constellation

        #Fallback Variables

        #Calculated Variables
        self.calc_ci = None
        self.calc_pos = None    #This might be broken up into azimuth & altitude or both could be combined into 1 array for star's pos
        self.calc_size = None
        self.calc_luminosity = None

    def testPrint(self):
        print("This is a test print")
        #self.con = str(df_row['con']) if pd.notna(df_row['con']) and df_row['con'] != ''else None

    def setVar(self, var, val):
        pass

    def returnVar(self, var):
        pass

    '''
    Returns calculated values of 
    - Star Positioning as Azimuth & Altitude
    - Star's visual color to the human eye
    - Star's visual size in the sky
    - Star's visual luminosity after taking into account the atmosphere and distance from Earth
    '''
    def returnCalcVars(self):
        return [self.calc_pos, self.calc_ci, self.calc_luminosity, self.calc_size]