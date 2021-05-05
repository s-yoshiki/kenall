from .util import *

def test_normal():
    write_item("\r\n".join([
        '01101,"064  ","0640941","ﾎｯｶｲﾄﾞｳ","ｻｯﾎﾟﾛｼﾁｭｳｵｳｸ","ｱｻﾋｶﾞｵｶ","北海道","札幌市中央区","旭ケ丘",0,0,1,0,0,0',
        '13113,"151  ","1510064","ﾄｳｷｮｳﾄ","ｼﾌﾞﾔｸ","ｳｴﾊﾗ","東京都","渋谷区","上原",0,0,1,0,0,0',
        '13307,"19002","1900223","ﾄｳｷｮｳﾄ","ﾆｼﾀﾏｸﾞﾝﾋﾉﾊﾗﾑﾗ","ﾅﾝｺﾞｳ","東京都","西多摩郡檜原村","南郷",0,0,0,0,0,0',
    ]))
    postal = generate_parser()
    counter = 0
    items = []
    for item in postal:
        items.append(item)
    # 0
    assert len(items) == 3
    # 1
    item = items[0]
    assert item.region_id == '01101'
    assert item.old_zip == '064  '
    assert item.zip == '0640941'
    assert item.pref_kana == 'ホッカイドウ'
    assert item.region_kana == 'サッポロシチュウオウク'
    assert item.town_kana == 'アサヒガオカ'
    assert item.pref == '北海道'
    assert item.region == '札幌市中央区'
    assert item.town == '旭ケ丘'
    assert item.is_multi_zip == '0'
    assert item.has_koaza_banchi == '0'
    assert item.has_chome == '1'
    assert item.is_multi_town == '0'
    assert item.update_status == '0'
    assert item.update_reason == '0'
    # 2
    item = items[1]
    assert item.region_id == '13113'
    assert item.old_zip == '151  '
    assert item.zip == '1510064'
    assert item.pref_kana == 'トウキョウト'
    assert item.region_kana == 'シブヤク'
    assert item.town_kana == 'ウエハラ'
    assert item.pref == '東京都'
    assert item.region == '渋谷区'
    assert item.town == '上原'
    assert item.is_multi_zip == '0'
    assert item.has_koaza_banchi == '0'
    assert item.has_chome == '1'
    assert item.is_multi_town == '0'
    assert item.update_status == '0'
    assert item.update_reason == '0'
    # 3
    item = items[2]
    assert item.region_id == '13307'
    assert item.old_zip == '19002'
    assert item.zip == '1900223'
    assert item.pref_kana == 'トウキョウト'
    assert item.region_kana == 'ニシタマグンヒノハラムラ'
    assert item.town_kana == 'ナンゴウ'
    assert item.pref == '東京都'
    assert item.region == '西多摩郡檜原村'
    assert item.town == '南郷'
    assert item.is_multi_zip == '0'
    assert item.has_koaza_banchi == '0'
    assert item.has_chome == '0'
    assert item.is_multi_town == '0'
    assert item.update_status == '0'
    assert item.update_reason == '0'
