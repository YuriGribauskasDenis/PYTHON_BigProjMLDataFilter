import pandas as pd


class Analizer:

    def __init__(self, df):
        self.__df = df

    def get_table(self):
        dfk = self.__df.groupby('B')['A'].apply(list).reset_index(name='AAA')
        return dfk