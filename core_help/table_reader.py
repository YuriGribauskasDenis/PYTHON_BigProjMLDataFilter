import pandas as pd


class PDReader:

    def __init__(self, sep=',', header=None, index_col=False):
        self.__sep = sep
        self.__header = header
        self.__index_colint = index_col

        @property
        def sep(self):
            return self.__sep
        @sep.setter
        def sep(self, sep):
            self.__sep = sep

        @property
        def header(self):
            return self.__header
        @header.setter
        def header(self, header):
            self.__header = header

        @property
        def index_col(self):
            return self.__index_colint
        @index_col.setter
        def index_col(self, index_col):
            self.__index_colint = index_col

    def __gen_one_name(self, col):
        LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        result = []
        while col:
            col, rem = divmod(col - 1, len(LETTERS))
            result[:0] = LETTERS[rem]
        return ''.join(result)

    def __gen_name_list(self, n):
        cols_names = [self.__gen_one_name(i) for i in range(1, n + 1)]
        return cols_names

    def get_table(self, file_path):
        file_path = str(file_path)
        df = pd.read_csv(file_path, sep=self.__sep, header=self.__header, index_col=self.__index_colint)
        n = len(df.columns)
        df.columns = self.__gen_name_list(n)
        return df