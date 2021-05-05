from .util import *

def test_chome():
    write_item("\r\n".join([
        '01106,"005  ","0050030","ﾎｯｶｲﾄﾞｳ","ｻｯﾎﾟﾛｼﾐﾅﾐｸ","ﾐﾅﾐ30ｼﾞｮｳﾆｼ(8ﾁｮｳﾒ)","北海道","札幌市南区","南三十条西（８丁目）",0,0,1,0,0,0',
        '01207,"080  ","0800848","ﾎｯｶｲﾄﾞｳ","ｵﾋﾞﾋﾛｼ","ｼﾞﾕｳｶﾞｵｶ(1､2ﾁｮｳﾒ)","北海道","帯広市","自由が丘（１、２丁目）",1,0,1,0,0,0',
        '01101,"060  ","0600042","ﾎｯｶｲﾄﾞｳ","ｻｯﾎﾟﾛｼﾁｭｳｵｳｸ","ｵｵﾄﾞｵﾘﾆｼ(1-19ﾁｮｳﾒ)","北海道","札幌市中央区","大通西（１〜１９丁目）",1,0,1,0,0,0',
        '01207,"080  ","0800029","ﾎｯｶｲﾄﾞｳ","ｵﾋﾞﾋﾛｼ","ﾆｼ19ｼﾞｮｳﾐﾅﾐ(35-38､41､42ﾁｮｳﾒ)","北海道","帯広市","西十九条南（３５〜３８、４１、４２丁目）",1,0,1,0,0,0',
    ]))
    postal = generate_parser()
    # 1
    item = next(postal)
    assert item.town == '南三十条西'
    assert item.town_kana == 'ミナミ30ジョウニシ'
    assert item.has_subtown
    assert item.subtown[0] == '8丁目'
    assert item.subtown_kana[0] == '8チョウメ'
    # 2
    item = next(postal)
    assert item.town == '自由が丘'
    assert item.town_kana == 'ジユウガオカ'
    assert item.has_subtown
    assert item.subtown == ['1丁目', '2丁目']
    assert item.subtown_kana == ['1チョウメ', '2チョウメ']
    # 3
    item = next(postal)
    assert item.town == '大通西'
    assert item.town_kana == 'オオドオリニシ'
    assert item.has_subtown
    assert (item.subtown == [
        '1丁目',
        '2丁目',
        '3丁目',
        '4丁目',
        '5丁目',
        '6丁目',
        '7丁目',
        '8丁目',
        '9丁目',
        '10丁目',
        '11丁目',
        '12丁目',
        '13丁目',
        '14丁目',
        '15丁目',
        '16丁目',
        '17丁目',
        '18丁目',
        '19丁目',
    ])
    assert (item.subtown_kana == [
        '1チョウメ',
        '2チョウメ',
        '3チョウメ',
        '4チョウメ',
        '5チョウメ',
        '6チョウメ',
        '7チョウメ',
        '8チョウメ',
        '9チョウメ',
        '10チョウメ',
        '11チョウメ',
        '12チョウメ',
        '13チョウメ',
        '14チョウメ',
        '15チョウメ',
        '16チョウメ',
        '17チョウメ',
        '18チョウメ',
        '19チョウメ',
    ])
    # 4
    item = next(postal)
    assert item.town == '西十九条南'
    assert item.town_kana == 'ニシ19ジョウミナミ'
    assert item.has_subtown
    assert (item.subtown == [
        '35丁目',
        '36丁目',
        '37丁目',
        '38丁目',
        '41丁目',
        '42丁目',
    ])
    assert (item.subtown_kana == [
        '35チョウメ',
        '36チョウメ',
        '37チョウメ',
        '38チョウメ',
        '41チョウメ',
        '42チョウメ',
    ])


