

#Object class for Star


class Star:

    #Should be initiated with a DF ? Or just a row taken from the DF when grabbing the data from 
    def __init__(self, df_row):

        #All variables that would be extracted from the csv given would be for epoch & equinox 2000.0

        #Initial variables required for calculations
        self.ra = float(df_row['ra'])           #Right Ascension
        self.dec = float(df_row['dec'])         #Declination
        self.pmra = float(df_row['pmra'])       #Proper Motion Right Ascension
        self.pmdec = float(df_row['pmdec'])     #Proper Motion Declination 
        self.dist = float(df_row['dist'])       #Distance

        #Visual Variables
        self.mag = float(df_row['mag'])         #Apparent Visual Magnitude
        self.ci = float(df_row['ci'])           #Color Index

        #Fallback Variables

        #Identification Variables
        self.proper = str(df_row['proper'])     #Proper Name
        self.con = str(df_row['con']) or None   #Constellation

        #Variables that'll be calculated
        self.calc_ci = None
        self.calc_pos = None    #This might be broken up into azimuth & altitude or both could be combined into 1 array for star's pos
        self.calc_size = None
        self.calc_luminosity = None

    def setVar(self):
        pass

    def returnVar(self):
        pass


    def returnCalcVars(self):
        return [self.calc_pos, self.calc_ci, self.calc_luminosity, self.calc_size]