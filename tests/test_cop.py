from core_help import PDReader
from core_help import Analizer
from core_help import Copier
import pandas as pd

r = PDReader()
adr = r'C:\tmp\tf_custom_loop_fit\PROJ3\tests\res_loss_001.csv'
df = r.get_table(adr)

a = Analizer(df)
dfk = a.get_table()

r0 = PDReader()
adr0 = r'C:\tmp\tf_custom_loop_fit\PROJ3\tests\files_grouped.csv'
df0 = r0.get_table(adr0)

c = Copier(dfk,df0,3)
c.copy()