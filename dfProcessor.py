
#This'll process df's and return the rows, columns, and labels


class DataFrameProcessor:

    def __init__(self, df):
        self.df = df

    def returnLabels(self):
        labels = self.df.columns.tolist()
        return labels
    
    def returnColumn(self, colLabel):
        col = self.df[colLabel]
        return col
    
    def returnRow(self, rowNum):
        row = self.df.iloc[rowNum]
        return row