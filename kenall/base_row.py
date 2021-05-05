import sys

class BaseRow:
    _item = {
        'region_id': '',
        'old_zip': '',
        'zip': '',
        'pref_kana': '',
        'region_kana': '',
        'town_kana': '',
        'pref': '',
        'region': '',
        'town': '',
        'is_multi_zip': '',
        'has_koaza_banchi': '',
        'has_chome': '',
        'is_multi_town': '',
        'update_status': '',
        'update_reason': '',
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
    _line = []

    @property
    def list(self):
        return self._line

    @property
    def dict(self):
        return self._item

    @property
    def region_id(self):
        return self._item[sys._getframe().f_code.co_name]

    @property
    def old_zip(self):
        return self._item[sys._getframe().f_code.co_name]

    @property
    def zip(self):
        return self._item[sys._getframe().f_code.co_name]

    @property
    def pref_kana(self):
        return self._item[sys._getframe().f_code.co_name]

    @property
    def region_kana(self):
        return self._item[sys._getframe().f_code.co_name]

    @property
    def town_kana(self):
        return self._item[sys._getframe().f_code.co_name]

    @property
    def pref(self):
        return self._item[sys._getframe().f_code.co_name]

    @property
    def region(self):
        return self._item[sys._getframe().f_code.co_name]

    @property
    def town(self):
        return self._item[sys._getframe().f_code.co_name]

    @property
    def is_multi_zip(self):
        return self._item[sys._getframe().f_code.co_name]

    @property
    def has_koaza_banchi(self):
        return self._item[sys._getframe().f_code.co_name]

    @property
    def has_chome(self):
        return self._item[sys._getframe().f_code.co_name]

    @property
    def is_multi_town(self):
        return self._item[sys._getframe().f_code.co_name]

    @property
    def update_status(self):
        return self._item[sys._getframe().f_code.co_name]

    @property
    def update_reason(self):
        return self._item[sys._getframe().f_code.co_name]

    @property
    def city(self):
        return self._item[sys._getframe().f_code.co_name]

    @property
    def city_kana(self):
        return self._item[sys._getframe().f_code.co_name]

    @property
    def district(self):
        return self._item[sys._getframe().f_code.co_name]

    @property
    def district_kana(self):
        return self._item[sys._getframe().f_code.co_name]

    @property
    def ward(self):
        return self._item[sys._getframe().f_code.co_name]

    @property
    def ward_kana(self):
        return self._item[sys._getframe().f_code.co_name]

    @property
    def build(self):
        return self._item[sys._getframe().f_code.co_name]

    @property
    def build_kana(self):
        return self._item[sys._getframe().f_code.co_name]

    @property
    def floor(self):
        return self._item[sys._getframe().f_code.co_name]

    @property
    def subtown(self):
        return self._item[sys._getframe().f_code.co_name]

    @property
    def subtown_kana(self):
        return self._item[sys._getframe().f_code.co_name]

    @property
    def has_subtown(self):
        return len(self._item['subtown']) > 0
