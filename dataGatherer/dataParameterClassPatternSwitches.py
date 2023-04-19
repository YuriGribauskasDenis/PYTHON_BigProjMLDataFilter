from dataGatherer.dataParameterClassPattern import ParameterPattern

class ParameterSwitches(ParameterPattern):

    def setKeyword(self):
        return 'switch_constants'

    def setParameterList(self):
        plist = [
            'FROM_FLDR',
            'GEN_CSV',
            'FROM_CSV',
            'GEN_ZIP',
            'FROM_ZIP',
            'CONT_TRAIN'
        ]
        return plist