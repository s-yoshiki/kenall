from .util import *

def test_ichien():
    write_item("\r\n".join([
        '13362,"10003","1000301","ﾄｳｷｮｳﾄ","ﾄｼﾏﾑﾗ","ﾄｼﾏﾑﾗｲﾁｴﾝ","東京都","利島村","利島村一円",0,0,0,0,0,0',
        '47356,"90136","9013601","ｵｷﾅﾜｹﾝ","ｼﾏｼﾞﾘｸﾞﾝﾄﾅｷｿﾝ","ﾄﾅｷｿﾝｲﾁｴﾝ","沖縄県","島尻郡渡名喜村","渡名喜村一円",0,0,0,0,0,0',
        '25443,"52203","5220317","ｼｶﾞｹﾝ","ｲﾇｶﾐｸﾞﾝﾀｶﾞﾁｮｳ","ｲﾁｴﾝ","滋賀県","犬上郡多賀町","一円",0,0,0,0,0,0',
    ]))
    postal = generate_parser()
    
    item = next(postal)
    assert item.zip == '1000301'
    assert item.town == ''
    assert item.town_kana == ''

    item = next(postal)
    assert item.zip == '9013601'
    assert item.town == ''
    assert item.town_kana == ''

    item = next(postal)
    assert item.zip == '5220317'
    assert item.town == '一円'
    assert item.town_kana == 'イチエン'

