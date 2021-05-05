from .util import *

def test_banchi():
    write_item("\r\n".join([
        '01106,"005  ","0050865","ﾎｯｶｲﾄﾞｳ","ｻｯﾎﾟﾛｼﾐﾅﾐｸ","ﾄｷﾜ(1-131ﾊﾞﾝﾁ)","北海道","札幌市南区","常盤（１〜１３１番地）",1,0,0,0,0,0',
        '01106,"005  ","0050840","ﾎｯｶｲﾄﾞｳ","ｻｯﾎﾟﾛｼﾐﾅﾐｸ","ﾌｼﾞﾉ(400､400-2ﾊﾞﾝﾁ)","北海道","札幌市南区","藤野（４００、４００−２番地）",1,0,0,0,0,0',
        '01106,"005  ","0050008","ﾎｯｶｲﾄﾞｳ","ｻｯﾎﾟﾛｼﾐﾅﾐｸ","ﾏｺﾏﾅｲ(17ﾊﾞﾝﾁ)","北海道","札幌市南区","真駒内（１７番地）",1,0,0,0,0,0',
        '01204,"07801","0780186","ﾎｯｶｲﾄﾞｳ","ｱｻﾋｶﾜｼ","ｶﾑｲﾁｮｳﾆｼｵｶ(8-22ﾊﾞﾝﾁ)","北海道","旭川市","神居町西丘（８−２２番地）",1,0,0,0,0,',
        '01207,"08023","0802333","ﾎｯｶｲﾄﾞｳ","ｵﾋﾞﾋﾛｼ","ﾋﾞｴｲﾁｮｳ(ﾆｼ5-8ｾﾝ79-110ﾊﾞﾝﾁ)","北海道","帯広市","美栄町（西５〜８線７９〜１１０番地）",1,0,0,0,0,0',
        '01210,"06831","0683161","ﾎｯｶｲﾄﾞｳ","ｲﾜﾐｻﾞﾜｼ","ｸﾘｻﾜﾁｮｳﾐﾔﾑﾗ(248､339､726､780､800､806ﾊﾞﾝﾁ)","北海道","岩見沢市","栗沢町宮村（２４８、３３９、７２６、７８０、８００、８０６番地）",1,0,0,0,0,0',
    ]))
    postal = generate_parser()
    # 1
    item = next(postal)
    assert item.town == '常盤'
    assert item.town_kana == 'トキワ'
    assert item.has_subtown
    assert item.subtown[0] == '1〜131番地'
    assert item.subtown_kana[0] == '1-131バンチ'
    # 2
    item = next(postal)
    assert item.town == '藤野'
    assert item.town_kana == 'フジノ'
    assert item.has_subtown
    assert item.subtown[0] == '400'
    assert item.subtown_kana[0] == '400'
    assert item.subtown[1] == '400-2番地'
    assert item.subtown_kana[1] == '400-2バンチ'
    # 3
    item = next(postal)
    assert item.town == '真駒内'
    assert item.town_kana == 'マコマナイ'
    assert item.has_subtown
    assert item.subtown[0] == '17番地'
    assert item.subtown_kana[0] == '17バンチ'
    # 4
    item = next(postal)
    assert item.town == '神居町西丘'
    assert item.town_kana == 'カムイチョウニシオカ'
    assert item.has_subtown
    assert item.subtown[0] == '8-22番地'
    assert item.subtown_kana[0] == '8-22バンチ'
    # 5
    item = next(postal)
    assert item.town == '美栄町'
    assert item.town_kana == 'ビエイチョウ'
    assert item.has_subtown
    assert item.subtown[0] == '西5〜8線79〜110番地'
    assert item.subtown_kana[0] == 'ニシ5-8セン79-110バンチ'
    # 6
    item = next(postal)
    assert item.town == '栗沢町宮村'
    assert item.town_kana == 'クリサワチョウミヤムラ'
    assert item.has_subtown
    assert item.subtown[0] == '248'
    assert item.subtown_kana[0] == '248'
    assert item.subtown[1] == '339'
    assert item.subtown_kana[1] == '339'
    assert item.subtown[2] == '726'
    assert item.subtown_kana[2] == '726'
    assert item.subtown[3] == '780'
    assert item.subtown_kana[3] == '780'
    assert item.subtown[4] == '800'
    assert item.subtown_kana[4] == '800'
    assert item.subtown[5] == '806番地'
    assert item.subtown_kana[5] == '806バンチ'

