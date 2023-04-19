from pathlib import Path
from stuff.generatePath import get_folder_adr

fname = 'constants.json'
address_constants = get_folder_adr(__file__) / fname

from dataGatherer.dataParameterClassReader import ParameterReaderSingle

from dataGatherer.dataParameterClassPatternAddresses import ParameterAddresses
ap_reader = ParameterReaderSingle(str(address_constants), ParameterAddresses())
ap_obj = ap_reader.getDic()

from dataGatherer.dataParameterClassPatternNumbers import ParameterNumbers
np_reader = ParameterReaderSingle(str(address_constants), ParameterNumbers())
np_obj = np_reader.getDic()

from dataGatherer.dataParameterClassPatternSwitches import ParameterSwitches
sp_reader = ParameterReaderSingle(str(address_constants), ParameterSwitches())
sp_obj = sp_reader.getDic()