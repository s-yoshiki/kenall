from .util import *

def test_notuginibanchigakurubaai():
    write_item(
        '21207,"50137","5013701","ｷﾞﾌｹﾝ","ﾐﾉｼ","ﾐﾉｼﾉﾂｷﾞﾆﾊﾞﾝﾁｶﾞｸﾙﾊﾞｱｲ","岐阜県","美濃市","美濃市の次に番地がくる場合",0,0,0,0,0,0\r\n'+
        '20448,"39972","3997201","ﾅｶﾞﾉｹﾝ","ﾋｶﾞｼﾁｸﾏｸﾞﾝｲｸｻｶﾑﾗ","ｲｸｻｶﾑﾗﾉﾂｷﾞﾆﾊﾞﾝﾁｶﾞｸﾙﾊﾞｱｲ","長野県","東筑摩郡生坂村","生坂村の次に番地がくる場合",0,0,0,0,0,0'
    )
    postal = generate_parser()
    item = next(postal)
    assert item.zip == '5013701'
    assert item.pref_kana == 'ギフケン'
    assert item.region_kana == 'ミノシ'
    assert item.town_kana == ''
    assert item.pref == '岐阜県'
    assert item.region == '美濃市'
    assert item.town == ''

    item = next(postal)
    assert item.zip == '3997201'
    assert item.pref_kana == 'ナガノケン'
    assert item.region_kana == 'ヒガシチクマグンイクサカムラ'
    assert item.town_kana == ''
    assert item.pref == '長野県'
    assert item.region == '東筑摩郡生坂村'
    assert item.town == ''

