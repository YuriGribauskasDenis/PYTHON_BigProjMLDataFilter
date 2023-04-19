from stuff.generatePath import get_folder_adr

fname = 'smth.csv'
address_csv = get_folder_adr(__file__) / fname

res = {
    1053 : 16.118095397949,
    1054 : 16.118095397949,
    1439 : 16.118095397949,
    1450 : 16.118095397949,
    1459 : 16.118095397949,
    1465 : 16.118095397949,
    1495 : 16.118095397949,
    1525 : 16.118095397949,
    1536 : 16.118095397949,
    1546 : 16.118095397949,
    1579 : 16.118095397949,
    1977 : 16.118095397949,
    1978 : 16.118095397949,
    1979 : 16.118095397949,
    1980 : 16.118095397949,
    1981 : 16.118095397949,
    1982 : 16.118095397949,
    1995 : 16.118095397949,
    1998 : 16.118095397949,
    1999 : 16.118095397949,
    2000 : 16.118095397949,
    2007 : 16.118095397949,
    2008 : 16.118095397949
}
res_sorted = {k : v for k, v in sorted(res.items(), key = lambda x: x[1], reverse=True)}

import csv
with open(address_csv, 'w', newline='') as f:
    writer = csv.writer(f)
    #for i, (k, v) in enumerate(sorted(res.items(), key = lambda x: x[1], reverse=True).items()):
    for i, (k, v) in enumerate(res_sorted.items()):
        writer.writerow([k,v])
        if i > 10:
            break