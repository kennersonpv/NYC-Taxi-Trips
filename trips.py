class Trips:

    def __init__(self, df):
        self.df = df

    def has_tip(self, column):
        self.df['tip'] = 0
        for i, row in self.df.iterrows():
            if row[column] > 0:
                self.df.at[i,'tip'] = 1
        return self.df