import json

class ParameterReaderSingle:

    def __init__(self, address, data_parameter_class):
        self.__address = address
        self.__data_parameter_class = data_parameter_class

    def getDic(self):
        params = self.read_json(self.__data_parameter_class.keyword)
        self.__data_parameter_class.initDic(params)
        return self.__data_parameter_class

    def read_json(self, key):
        return json.load(open(self.__address, 'r'))[key]