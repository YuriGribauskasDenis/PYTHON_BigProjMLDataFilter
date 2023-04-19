from core_help import PDReader
from core_help import Analizer
import pandas as pd

r = PDReader()
adr = r'C:\tmp\tf_custom_loop_fit\PROJ3\tests\res_loss_001.csv'
df = r.get_table(adr)

a = Analizer(df)
dfk = a.get_table()

print(dfk.head().to_markdown())