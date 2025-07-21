

#Going to be extracting only the named stars from the csv dataset that's hyglike
#This is done to reduce the computations for initial runtime for testing
#Will probably use the csv made from only named stars until multithreading or more efficient calculation
#functions are made to calculate the star's position, luminosity, and size in correlation to where the initial
#viewing is from on Earth also based on what time it is



import pandas as pd

class ExtractNamedStars:

    def __init__(self):
        pass
    
    '''
    The goal of this function is to extract the rows that have a non-blank value in the corresponding col being called upon
    For example, if only the rows with something in column G or 'proper' for this specific csv dataset is being called upon
    then it'll only return the rows with a non-blank value in column G / 'proper'
    '''
    def extractRowToCol(self):
        df = pd.read_csv("hyg_v42.csv")

        if 'proper' in df.columns:
            target_col = 'proper'
        else:
            target_col = df.columns[6]
        
        #For some reason converting a blank slot makes it into nan so had to check for 'nan' rather than ''
        filtered_df = df[ df[target_col].astype(str).str.strip() != 'nan']

        filtered_df.to_csv('filtered_output.csv', index = False)

        print(f"Filtered {len (filtered_df) } rows. Saved to 'filtered_output.csv' ")


test = ExtractNamedStars()
test.extractRowToCol()

