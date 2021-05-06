import csv
import re
import codecs
from .row import Row


class Parser:
    record_queue = []
    __opt = {}

    def __init__(self, path="", encoding="shift_jis", katakana_h2z=False, alnum_z2h=False):
        self.__opt = {
            'path': path,
            'katakana_h2z': katakana_h2z,
            'alnum_z2h': alnum_z2h,
            'current_build_town': '',
            'current_build_town_kana': '',
        }
        self.__fp = codecs.open(path, 'r', encoding=encoding)

    def __iter__(self):
        return self

    def __next__(self):
        row = self.__get_line()
        return Row(
            row=row,
            opt={
                'build_town': self.__opt['current_build_town'],
                'build_town_kana': self.__opt['current_build_town_kana'],
                'katakana_h2z': self.__opt['katakana_h2z'],
                'alnum_z2h': self.__opt['alnum_z2h'],
            }
        )

    def __get_line(self):
        row = self.__read_line()
        if re.search(r"（.+[^）]$", row[8]):
            past_town_kana = row[5]
            while True:
                tmp = self.__read_line()
                if not past_town_kana == tmp[5]:
                    row[5] += tmp[5]
                row[8] += tmp[8]
                if re.search(r"\）$", row[8]):
                    break
                past_town_kana = tmp[5]
        town = row[8]
        if re.search(r"^(.+)（次のビルを除く）$", row[8]):
            self.__opt['current_build_town'] = list(
                filter(None, re.split(r"^(.+)（次のビルを除く）$", row[8])))[0]
            self.__opt['current_build_town_kana'] = list(
                filter(None, re.split(r"^(.+)\(", row[5])))[0]
        elif row[2] == '4530002' and re.search(r"^名駅\（", town):
            self.__opt['current_build_town'] = '名駅'
            self.__opt['current_build_town_kana'] = 'ﾒｲｴｷ'
        else:
            current_build_town = self.__opt['current_build_town']
            if not re.search(r"^" + re.escape(current_build_town) + r".+（.+階.*）$", town):
                self.__opt['current_build_town'] = ''
                self.__opt['current_build_town_kana'] = ''
        return row

    def __read_line(self):
        row = csv.reader(
            self.__fp,
            delimiter=",",
            doublequote=True,
            lineterminator="\r\n",
            quotechar='"',
            skipinitialspace=True
        )
        try:
            return next(row)
        except StopIteration:
            self.__fp.close()
            raise StopIteration()
