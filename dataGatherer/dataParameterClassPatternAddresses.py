from dataGatherer.dataParameterClassPattern import ParameterPattern

class ParameterAddresses(ParameterPattern):

    def setKeyword(self):
        return 'input_addresses'

    def setParameterList(self):
        plist = [
            'DEFECT_FLDR',
            'NODEFECT_FLDR',
            'DUMP_FLDR',
            'DUMP_FILE',
            'ZIP_FILE',
            'CHECK_POINT_FLDR'
        ]
        return plist