from core import ModelHandler, DataRaiser
from core_help import PDReader, Analizer, Copier
from pathlib import Path
from constants import ap_obj

dr = DataRaiser()
X_inp, Y_inp, I_inp, _ = dr.dater()

mh = ModelHandler()
mh.complex_train(X_inp, Y_inp, I_inp)

# copy files
#======================
print('INITIATE COPYING')
r0 = PDReader()
adr0 = ap_obj.getData('DUMP_FILE')
df0 = r0.get_table(adr0)

exp_fldr = ap_obj.getData('CHECK_POINT_FLDR')
csv_files = [child for child in Path(exp_fldr).iterdir() if child.suffix == '.csv']

for f in csv_files:
    r = PDReader()
    adr = str(f)
    df = r.get_table(adr)

    a = Analizer(df)
    dfk = a.get_table()

    i = int(f.stem[-3:])
    print(f'file {i} / len(csv_files)')
    c = Copier(dfk,df0,i)
    c.copy()

print('ALL DONE')