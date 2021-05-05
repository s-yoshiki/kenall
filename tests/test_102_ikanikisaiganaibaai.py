from .util import *

def test_ikanikisaiganaibaai():
    write_item('13113,"150  ","1500000","ﾄｳｷｮｳﾄ","ｼﾌﾞﾔｸ","ｲｶﾆｹｲｻｲｶﾞﾅｲﾊﾞｱｲ","東京都","渋谷区","以下に掲載がない場合",0,0,0,0,0,0')
    postal = generate_parser()
    item = next(postal)
    assert item.town == ''
    assert item.town_kana == ''
    assert item.zip == '1500000'
    assert item.pref_kana == 'トウキョウト'
    assert item.region_kana == 'シブヤク'
    assert item.town_kana == ''
    assert item.pref == '東京都'
    assert item.region == '渋谷区'
    assert item.town == ''