

import astropy  #Might remove this and do manual calculations later ? I'm unsure if it would be faster though than the library
import astronomy
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
from astropy.time import Time
import astropy.units as u

class StarCalculations:

    def __init__(self):
        pass

    def calculatePosition(self, star, time, location):
        #Create star object with proper motion
        star_coord = SkyCoord(
            ra = star.ra * u.degree,
            dec = star.dec * u.degree,
            pm_ra_cosdec = star.pmra * u.mas / u.yr,
            pm_dec = star.pmdec * u.mas / u.yr,
            distance = star.dist * u.pc,
            obstime = 'J2000'
        )

        #Convert to observer's position / time
        obs_time = Time(time, format = 'jd')
        observer_location = EarthLocation(
            lat = location[0] * u.deg,
            lon = location[1] * u.deg,
            height = 0 * u.m
        )

        altaz = star_coord.transform_to(
            AltAz(obstime = obs_time, location = observer_location)
        )

        return altaz.az.degree, altaz.alt.degree

    '''
    This was originally going to take in some values but because of the mag value existing then this is no longer necessary. Will probably
    remove this function once all of the calculations are done and completed.
    '''
    def calculateLuminosity(self):
        pass
    
    '''
    Converts magnitude to visual display size
    '''
    def calculateSize(self, mag):
        # Scale: Mag 0 = largest, Mag 6 = smallest visible
        # Logarithmic scaling: 
        # mag -1.5 -> size 3.0, mag 8.0 -> size 0.05
        return 10 ** (-0.35 * mag + 0.2)
        


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



    '''
    def calculate_actual_size(star):
        """Calculate true angular size (advanced feature)"""
    if not star.dist or star.dist >= 100000:
        return 0.0  # Unknown distance
    
    # Estimate temperature from spectral type
    temp = spectral_to_temp(star.spect) if star.spect else 5500
    
    # Estimate physical radius (solar units)
    radius = (star.lum ** 0.5) / (temp/5800)**2 if star.lum else 1.0
    
    # Calculate angular size
    return (2 * radius * 0.00465) / star.dist  # arcseconds
    '''