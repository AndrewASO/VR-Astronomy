

#Object class for Star


class Star:

    #Should be initiated with a DF ? Or just a row taken from the DF when grabbing the data from 
    def __init__(self, df_row):

        #Initial variables required for calculations
        self.ra = float(df_row['ra'])
        self.dec = None
        self.pmra = None
        self.pmdec = None
        self.dist = None
        self.mag = None
        self.ci = None
        self.rv = None


        #Identification Variables
        self.proper = None
        self.con = None

        #Variables that'll be calculated
        self.calc_ci = None
        self.calc_pos = None    #This might be broken up into azimuth & altitude or both could be combined into 1 array for star's pos
        self.calc_size = None
        self.calc_luminosity = None

    def setVariable(self):
        pass

    def returnVariable(self):
        pass


    def returnCalcVars(self):
        return [self.calc_pos, self.calc_ci, self.calc_luminosity, self.calc_size]