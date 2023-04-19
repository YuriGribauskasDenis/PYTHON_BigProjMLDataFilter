
from core_help import PDReader
import pandas as pd

r = PDReader()
adr = r'C:\tmp\tf_custom_loop_fit\PROJ3\tests\res_loss_001.csv'
df = r.get_table(adr)

print(df.head().to_markdown())

r2 = PDReader()
adr2 = r'C:\tmp\tf_custom_loop_fit\PROJ3\tests\files_grouped.csv'
df2 = r2.get_table(adr2)

print(df2.head().to_markdown())