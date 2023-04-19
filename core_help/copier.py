import pandas as pd
from pathlib import Path
import shutil
from constants import ap_obj

class Copier:
    def __init__(self, df_copy_groups, df_addresses, subfldr):
        self.__df_groups = df_copy_groups
        self.__df_addresses = df_addresses
        self.__subfldr = subfldr
        adr = ap_obj.getData('DUMP_FLDR')
        self.__destination = adr

    def __check(self):
        pass

    def __create_concrete_dir(self, dir, subdir):
        p = Path(dir) / subdir
        p.mkdir(parents=True, exist_ok=True)
        return p

    def copy(self):
        i = int(self.__subfldr)
        p_global = self.__create_concrete_dir(self.__destination, f'{i:03d}')

        for index, row in self.__df_groups.iterrows():
            # 1.9E-07
            # 2E-07
            if float(row.B) < 0.0000002:
                continue
            p_local = self.__create_concrete_dir(p_global, str(row.B))
            for el in row.AAA:
                seri = self.__df_addresses[self.__df_addresses.A == el].B
                if not seri.empty:
                    str_file = str(seri.item())
                    str_file_name = str_file.split('\\')[-1]
                    my_file = Path(str_file)
                    to_file = p_local / str_file_name
                    try:
                        shutil.copy(my_file, to_file)
                    except:
                        print(el)
                        print(my_file.name)
                        print()
            # if index % 500 == 0:
            #     print(f'{index:03d}')
        print('COPYING DONE')