import kenall
from .util import *

def test_katakana_h2z_alnum_z2h():
    write_item('23105,"450  ","4506001","ｱｲﾁｹﾝ","ﾅｺﾞﾔｼﾅｶﾑﾗｸ","ﾒｲｴｷｼﾞｪｲｱｰﾙｾﾝﾄﾗﾙﾀﾜｰｽﾞ(1ｶｲ)","愛知県","名古屋市中村区","名駅ＪＲセントラルタワーズ（１階）",0,0,0,0,0,0')
    # 1
    postal = kenall.Parser({
        'path': get_csv_path(),
        'encoding': 'utf-8',
        # 'katakana_h2z': False,
        # 'alnum_z2h': False,
    })
    item = next(postal)
    assert item.build == '名駅ＪＲセントラルタワーズ'
    assert item.build_kana == 'ﾒｲｴｷｼﾞｪｲｱｰﾙｾﾝﾄﾗﾙﾀﾜｰｽﾞ'
    # 2
    postal = kenall.Parser({
        'path': get_csv_path(),
        'encoding': 'utf-8',
        'katakana_h2z': False,
        'alnum_z2h': True,
    })
    item = next(postal)
    assert item.build == '名駅JRセントラルタワーズ'
    assert item.build_kana == 'ﾒｲｴｷｼﾞｪｲｱｰﾙｾﾝﾄﾗﾙﾀﾜｰｽﾞ'
    # 3
    postal = kenall.Parser({
        'path': get_csv_path(),
        'encoding': 'utf-8',
        'katakana_h2z': True,
        'alnum_z2h': False,
    })
    item = next(postal)
    assert item.build == '名駅ＪＲセントラルタワーズ'
    assert item.build_kana == 'メイエキジェイアールセントラルタワーズ'

def test_parse_choume():
    write_item(
        '01101,"060  ","0600042","ﾎｯｶｲﾄﾞｳ","ｻｯﾎﾟﾛｼﾁｭｳｵｳｸ","ｵｵﾄﾞｵﾘﾆｼ(1-3ﾁｮｳﾒ)","北海道","札幌市中央区","大通西（１～３丁目）",1,0,1,0,0,0\r\n'
    )
    postal = kenall.Parser({
        'path': get_csv_path(),
        'encoding': 'utf-8',
        'katakana_h2z': False,
        'alnum_z2h': True,
    })
    item = next(postal)
    assert item.town == '大通西'
    assert item.town_kana == 'ｵｵﾄﾞｵﾘﾆｼ'
    assert len(item.subtown) == 3
    assert item.subtown[0] == '1丁目'
    assert item.subtown[1] == '2丁目'
    assert item.subtown[2] == '3丁目'
    assert len(item.subtown_kana) == 3
    assert item.subtown_kana[0] == '1ﾁｮｳﾒ'
    assert item.subtown_kana[1] == '2ﾁｮｳﾒ'
    assert item.subtown_kana[2] == '3ﾁｮｳﾒ'
