

#Object class for Star


class Star:

    #Should be initiated with a DF ? Or just a row taken from the DF when grabbing the data from 
    def __init__(self, df_row):

        #Initial variables required for calculations
        self.ra = float(df_row['ra'])
        self.dec = float(df_row['dec'])
        self.pmra = float(df_row['pmra'])
        self.pmdec = float(df_row['pmdec'])
        self.dist = float(df_row['dist'])

        #Visual Variables
        self.mag = float(df_row['mag'])
        self.ci = float(df_row['ci'])

        #Fallback Variables

        #Identification Variables
        self.proper = str(df_row['proper'])
        self.con = str(df_row['con'])

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