from constants import ap_obj

class Reporter:

    def __init__(self, tester):
        self.__tester = tester
        self.__save_to_fldr = ap_obj.getData('CHECK_POINT_FLDR')

    @property
    def tester(self):
        return self.__tester
    
    @property
    def save_to_fldr(self):
        return self.__save_to_fldr