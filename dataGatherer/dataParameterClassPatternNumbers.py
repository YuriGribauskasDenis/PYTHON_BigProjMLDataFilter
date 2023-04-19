from dataGatherer.dataParameterClassPattern import ParameterPattern

class ParameterNumbers(ParameterPattern):

    def setKeyword(self):
        return 'numerical_constants'

    def setParameterList(self):
        plist = [
            'BATCH_SIZE',
            'DND_RATIO',
            'TVT_RATIO',
            'EPOCHS'
        ]
        return plist