from abc import ABC, abstractmethod

class ParameterPattern(ABC):

    def __init__(self):
        self.__keyword = self.setKeyword()
        self.__collection = {}
        self.__parameters = self.setParameterList()

    @property
    def keyword(self):
        return self.__keyword

    @property
    def parameters(self):
        return self.__parameters

    @abstractmethod
    def setKeyword(self):
        pass

    @abstractmethod
    def setParameterList(self):
        pass

    def getData(self, key):
        if key not in self.__parameters:
            astr = ' '.join(self.__parameters)
            raise ValueError(f'{key} key not in {astr}')
        return self.__collection[key]

    def initDic(self, params):
        for k, v in params.items():
            k = k.upper()
            if k in self.__parameters:
                self.__collection[k] = v