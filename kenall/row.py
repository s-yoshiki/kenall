from .base_row import BaseRow
from .util import *
import mojimoji
import re


class Row(BaseRow):
    __opt = {
        'build_town': '',
        'town_kana': '',
        'katakana_h2z': False,
        'alnum_z2h': False,
    }

    def __init__(self, row=[], opt={}):
        self.__opt.update(opt)
        self._line = row
        self.__parse(row)

    def __parse(self, arg):
        r = arg
        self._item = {
            'region_id': r[0],
            'old_zip': r[1],
            'zip': r[2],
            'pref_kana': r[3],
            'region_kana': r[4],
            'town_kana': r[5],
            'pref': r[6],
            'region': r[7],
            'town': r[8],
            'is_multi_zip': r[9],
            'has_koaza_banchi': r[10],
            'has_chome': r[11],
            'is_multi_town': r[12],
            'update_status': r[13],
            'update_reason': r[14],
            'district': '',
            'district_kana': '',
            'city': '',
            'city_kana': '',
            'ward': '',
            'ward_kana': '',
            'build': '',
            'build_kana': '',
            'floor': '',
            'subtown': [],
            'subtown_kana': [],
        }
        self.__fix_region()
        self.__fix_town()
        self.__fix_build()
        self.__fix_subtown()
        self.__fix_kana_alnum()

    # 市,区,群,町,村をパースする
    def __fix_region(self):
        region = list(filter(None, re.split(r"^(.+?郡)(.+[町村])$", self.region)))
        if len(region) == 2:
            [district, city] = region
            [district_kana, city_kana] = list(
                filter(None, re.split(r"^((?:ｷﾀｸﾞﾝﾏ|.+?)ｸﾞﾝ)(.+)$", self.region_kana)))
            self._item['district'] = district
            self._item['district_kana'] = district_kana
            self._item['city'] = city
            self._item['city_kana'] = city_kana
        else:
            region = list(filter(None, re.split(r"^(.+市)(.+区)$", self.region)))
            if len(region) == 2:
                region_kana = list(filter(None, re.split(
                    r"^((?:ﾋﾛｼﾏ|ｷﾀｷｭｳｼｭｳ|.+?)ｼ)(.+)$", self.region_kana)))
                [city, ward] = region
                [city_kana, ward_kana] = region_kana
                self._item['city'] = city
                self._item['city_kana'] = city_kana
                self._item['ward'] = ward
                self._item['ward_kana'] = ward_kana
            elif re.search(r"区$", self.region):
                self._item['ward'] = self.region
                self._item['ward_kana'] = self.region_kana
            else:
                self._item['city'] = self.region
                self._item['city_kana'] = self.region_kana

    # 町名の調整
    def __fix_town(self):
        if self.town == '以下に掲載がない場合':
            self._item['town'] = ''
            self._item['town_kana'] = ''
        elif re.search(r"の次に番地がくる場合", self.town):
            region = list(filter(None, re.split(
                r"の次に番地がくる場合", self.town)))[0]
            reg = "群" + region
            if self.city == region or re.search(reg, self.city):
                self._item['town'] = ''
                self._item['town_kana'] = ''
        elif re.search(r"その他", self.town):
            self._item['town'] = self.town.replace("（その他）", "")
            self._item['town_kana'] = self.town_kana.replace("(ｿﾉﾀ)", "")
        elif re.search(r"^(.+[町村])一円$", self.town):
            town = list(filter(None, re.split(r"^(.+[町村])一円$", self.town)))[0]
            if self.city == town:
                self._item['town'] = ''
                self._item['town_kana'] = ''
        self._item['town'] = self.town.replace("～", "〜")

    # ビル名の調整
    def __fix_build(self):
        build_town = self.__opt['build_town']
        build_town_kana = self.__opt['build_town_kana']
        if len(build_town) == 0:
            if not (len(self.town) > 0 and re.search(r"（.+?階.*?）$", self.town)):
                return
        
        town = self.town.replace("（高層棟）", "")
        town_kana = self.town_kana.replace("(ｺｳｿｳﾄｳ)", "")
        if re.search(r"（次のビルを除く）$", town):
            self._item['town'] = self.town.replace("（次のビルを除く）", "")
            self._item['town_kana'] = self.town_kana.replace(
                "(ﾂｷﾞﾉﾋﾞﾙｦﾉｿﾞｸ)", ""
            )
        else:
            [build, floor] = town.split("（")
            floor = str_zen2han(floor)
            floor = re.findall(r'(\d+)階', floor)
            if len(floor) == 1:
                self._item['floor'] = floor[0]
            # build = list(filter(None, re.split(r"^" + re.escape(build_town) + r"(.+)（(.+)）$", town)))[0]
            build = list(filter(None, re.split(r"^" + re.escape(build_town) + r"(.+)$", build)))[0]
            if build == build_town:
                build = ''
            [build_kana, _] = town_kana.split("(")
            build_kana = list(filter(None, re.split(r"^" + re.escape(build_town_kana) + r"(.+)\(.+$", town_kana)))[0]
            build_kana = build_kana.split("(")[0]
            if build_kana == build_town_kana:
                build_kana = ''
            self._item['town'] = build_town
            self._item['town_kana'] = build_town_kana
            self._item['build'] = build
            self._item['build_kana'] = build_kana

    # 町名の調整 (丁目)
    def __fix_subtown(self):
        if len(self.town) == 0:
            return
        subtown = []
        subtown_kana = []
        if re.search(r"（([\d〜、]+)丁目）$", self.town):
            # 丁目
            town = str_zen2han(self.town).replace("、", ",").split(",")
            for num in town:
                range_choume = re.search(r"(\d+)〜(\d+)", num)
                if range_choume:
                    text = ""
                    for group in range_choume.group():
                        text += group
                    index = re.findall(r'\d+', text)
                    for i in range(int(index[0]), int(index[1]) + 1):
                        subtown.append(str(i) + '丁目')
                        subtown_kana.append(str(i) + 'ﾁｮｳﾒ')
                else:
                    num = re.findall(r'\d+', num)
                    subtown.append(num[0] + '丁目')
                    subtown_kana.append(num[0] + 'ﾁｮｳﾒ')
            self._item['town'] = re.sub(r'（([\d〜、]+)丁目）$', '', self.town)
            self._item['town_kana'] = re.sub(r'\([\d\-､]+ﾁｮｳﾒ\)$', '', self.town_kana)
        elif re.search(r"^[^\（]+地割", self.town):
            # 地割
            town = list(filter(None, re.split(
                r"^(.+\d+地割)(?:（(.+)）)?$", str_zen2han(self.town))))
            town_kana = list(filter(None, re.split(
                r"^(.+\d+ﾁﾜﾘ)(?:\((.+)\))?$", self.town_kana)))
            [prefix, koaza] = [town[0], '']
            [prefix_kana, koaza_kana] = [town_kana[0], '']
            if len(town) == 2:
                koaza = town[1]
                koaza_kana = town_kana[1]
            [aza, chiwari] = list(
                filter(None, re.split(r"^(.+?)第?(\d+地割.*)$", prefix)))
            [aza_kana, chiwari_kana] = list(
                filter(None, re.split(r"^(.+?)(?:ﾀﾞｲ)?(\d+ﾁﾜﾘ.*)$", prefix_kana)))
            chiwari = chiwari.replace(aza, "")
            chiwari = chiwari.replace("第", "")
            chiwari = chiwari.replace("地割", "")
            tmp_index = []
            tmp_index_kana = []
            for chiwari_split in list(filter(None, re.split("、", chiwari))):
                if re.search("〜", chiwari_split):
                    tmp_index.append(chiwari_split.replace("〜", "地割〜第"))
                    tmp_index_kana.append(chiwari_split.replace("〜", "ﾁﾜﾘ-ﾀﾞｲ"))
                else:
                    tmp_index.append(int(chiwari_split))
                    tmp_index_kana.append(int(chiwari_split))
            if len(chiwari) > 0:
                for index in tmp_index:
                    for item in koaza.split("、"):
                        item = "第" + str(index) + '地割 ' + item
                        item = item.strip()
                        subtown.append(item)
                for index in tmp_index_kana:
                    for item in koaza_kana.split("､"):
                        item = "ﾀﾞｲ" + str(index) + 'ﾁﾜﾘ ' + item
                        item = item.strip()
                        subtown_kana.append(item)
            else:
                for item in tmp_index:
                    subtown.append("第" + str(item) + '地割')
                for item in tmp_index_kana:
                    subtown_kana.append("ﾀﾞｲ" + str(item) + 'ﾁﾜﾘ')
            self._item['town'] = aza
            self._item['town_kana'] = aza_kana
        elif re.search(r"（(.+?)）$", self.town):
            banchi = re.findall(r"（(.+?)）$", self.town)
            self._item['town'] = self.town.split("（")[0]
            if len(banchi) > 0:
                banchi = banchi[0]
                # 「」内の"、"をエスケープする
                braces = re.findall(r"「(.+?)」", banchi)
                if len(braces) > 0:
                    for item in braces:
                        banchi = banchi.replace(item, '%s')
                banchi = banchi.replace("、", ",")
                if len(braces) > 0:
                    banchi = banchi % tuple(braces)
                subtown = banchi.split(",")
            # kana
            banchi_kana = re.findall(r"\((.+?)\)$", self.town_kana)
            self._item['town_kana'] = self.town_kana.split("(")[0]
            if len(banchi_kana) > 0:
                banchi_kana = banchi_kana[0]
                # <>内の"、"をエスケープする
                banchi_kana = banchi_kana.replace("､", ",")
                braces = re.findall(r"<(.+?)>", banchi_kana)
                if len(braces) > 0:
                    for item in braces:
                        banchi_kana = banchi_kana.replace(item, '%s')
                banchi_kana = banchi_kana.replace(",", "､")
                if len(braces) > 0:
                    banchi_kana = banchi_kana % tuple(braces)
                subtown_kana = banchi_kana.split("､")
        self._item['subtown'] = subtown
        self._item['subtown_kana'] = subtown_kana

    # 半角<=>全角の調整
    def __fix_kana_alnum(self):
        katakana_h2z = bool(self.__opt['katakana_h2z'])
        alnum_z2h = bool(self.__opt['alnum_z2h'])
        if not (katakana_h2z or alnum_z2h):
            return
        item_keys = [
            'pref_kana', 'region_kana', 'district_kana', 'city_kana', 'ward_kana', 'town_kana', 'build_kana',
            'pref', 'region', 'district', 'city', 'ward', 'town', 'build'
        ]
        for key in item_keys:
            if self._item[key] == '':
                continue
            if katakana_h2z:
                self._item[key] = mojimoji.han_to_zen(
                    self._item[key], ascii=False)
            if alnum_z2h:
                self._item[key] = mojimoji.zen_to_han(
                    self._item[key], kana=False)
        tmp = []
        for item in self._item['subtown']:
            if katakana_h2z:
                item = mojimoji.han_to_zen(item, ascii=False)
            if alnum_z2h:
                item = mojimoji.zen_to_han(item, kana=False)
            # note: マイナスをハイフンへ変換
            item = item.replace("−", "-") 
            tmp.append(item)
        self._item['subtown'] = tmp
        tmp = []
        for item in self._item['subtown_kana']:
            if katakana_h2z:
                item = mojimoji.han_to_zen(item, ascii=False)
            if alnum_z2h:
                item = mojimoji.zen_to_han(item, kana=False)
            tmp.append(item)
        self._item['subtown_kana'] = tmp