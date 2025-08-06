

class StarCalculations:

    def __init__(self):
        pass

    def calculatePosition(self):
        pass

    def calculateLuminosity(self):
        pass
    
    def calculateSize(self):
        pass


    '''
    Takes in a flaot value for ci (color index) that would be given as blue magnitude - visual magnitude from a distance of 10 parsecs.
    The goal of this function is to see what range the ci falls within and then return it as an RGB value that the human eye can
    visualize.
    Returns color (triple float list)
    '''
    def calculateColor(self, ci):
        
        #Convert B-V color index to RGB using temperature approximation 

        if ci < -0.3:                   #Extremely blue (0/B Stars)
            return (0.6, 0.7, 0.8) 
        elif ci < 0.0:                  #Blue-white (A Stars)
            return (0.8, 0.9, 1.0)
        elif ci < 0.3:                  #White (F Stars)
            return (1.0, 1.0, 1.0)
        elif ci < 0.6:                  #Yellow-white (G Stars)
            return (1.0, 1.0, 0.8)
        elif ci < 1.0:                  #Orange (K Stars)
            return (1.0, 0.8, 0.6)
        else:                           #Red (M Stars)
            return (1.0, 0.6, 0.4)
