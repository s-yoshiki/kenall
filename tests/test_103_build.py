from .util import *


def test_build():
    write_item("\r\n".join([
        '13113,"150  ","1500013","ﾄｳｷｮｳﾄ","ｼﾌﾞﾔｸ","ｴﾋﾞｽ(ﾂｷﾞﾉﾋﾞﾙｦﾉｿﾞｸ)","東京都","渋谷区","恵比寿（次のビルを除く）",0,0,1,0,0,0',
        '13113,"150  ","1506090","ﾄｳｷｮｳﾄ","ｼﾌﾞﾔｸ","ｴﾋﾞｽｴﾋﾞｽｶﾞｰﾃﾞﾝﾌﾟﾚｲｽ(ﾁｶｲ･ｶｲｿｳﾌﾒｲ)","東京都","渋谷区","恵比寿恵比寿ガーデンプレイス（地階・階層不明）",0,0,0,0,0,0',
        '13113,"150  ","1506001","ﾄｳｷｮｳﾄ","ｼﾌﾞﾔｸ","ｴﾋﾞｽｴﾋﾞｽｶﾞｰﾃﾞﾝﾌﾟﾚｲｽ(1ｶｲ)","東京都","渋谷区","恵比寿恵比寿ガーデンプレイス（１階）",0,0,0,0,0,0',
        '13113,"150  ","1500021","ﾄｳｷｮｳﾄ","ｼﾌﾞﾔｸ","ｴﾋﾞｽﾆｼ","東京都","渋谷区","恵比寿西",0,0,1,0,0,0',
        '23105,"453  ","4530002","ｱｲﾁｹﾝ","ﾅｺﾞﾔｼﾅｶﾑﾗｸ","ﾒｲｴｷ(1-1-8､1-1-12､1-1-13､1-1-14､1-3-4､","愛知県","名古屋市中村区","名駅（１−１−８、１−１−１２、１−１−１３、１−１−１４、１−３−４、",1,0,1,0,0,0',
        '23105,"453  ","4530002","ｱｲﾁｹﾝ","ﾅｺﾞﾔｼﾅｶﾑﾗｸ","1-3-7)","愛知県","名古屋市中村区","１−３−７）",1,0,1,0,0,0',
        '23105,"450  ","4506051","ｱｲﾁｹﾝ","ﾅｺﾞﾔｼﾅｶﾑﾗｸ","ﾒｲｴｷｼﾞｪｲｱｰﾙｾﾝﾄﾗﾙﾀﾜｰｽﾞ(51ｶｲ)","愛知県","名古屋市中村区","名駅ＪＲセントラルタワーズ（５１階）",0,0,0,0,0,0',
        '23105,"450  ","4506290","ｱｲﾁｹﾝ","ﾅｺﾞﾔｼﾅｶﾑﾗｸ","ﾒｲｴｷﾐｯﾄﾞﾗﾝﾄﾞｽｸｴｱ(ｺｳｿｳﾄｳ)(ﾁｶｲ･ｶｲｿｳﾌﾒｲ)","愛知県","名古屋市中村区","名駅ミッドランドスクエア（高層棟）（地階・階層不明）",0,0,0,0,0,0',
        '23105,"450  ","4506201","ｱｲﾁｹﾝ","ﾅｺﾞﾔｼﾅｶﾑﾗｸ","ﾒｲｴｷﾐｯﾄﾞﾗﾝﾄﾞｽｸｴｱ(ｺｳｿｳﾄｳ)(1ｶｲ)","愛知県","名古屋市中村区","名駅ミッドランドスクエア（高層棟）（１階）",0,0,0,0,0,0',
    ]))
    postal = generate_parser()
    # 1
    item = next(postal)
    assert item.zip == '1500013'
    assert item.town == '恵比寿'
    assert item.town_kana == 'エビス'
    assert item.build == ''
    assert item.build_kana == ''
    assert item.floor == ''
    # 2
    item = next(postal)
    assert item.zip == '1506090'
    assert item.town == '恵比寿'
    assert item.town_kana == 'エビス'
    assert item.build == '恵比寿ガーデンプレイス'
    assert item.build_kana == 'エビスガーデンプレイス'
    assert item.floor == ''
    # 3
    item = next(postal)
    assert item.zip == '1506001'
    assert item.town == '恵比寿'
    assert item.town_kana == 'エビス'
    assert item.build == '恵比寿ガーデンプレイス'
    assert item.build_kana == 'エビスガーデンプレイス'
    assert item.floor == '1'
    # 4
    item = next(postal)
    assert item.zip == '1500021'
    assert item.town == '恵比寿西'
    assert item.town_kana == 'エビスニシ'
    assert item.build == ''
    assert item.build_kana == ''
    assert item.floor == ''
    # 5
    item = next(postal)
    assert item.zip == '4530002'
    assert item.town == '名駅'
    assert item.town_kana == 'メイエキ'
    assert item.build == ''
    assert item.build_kana == ''
    assert item.floor == ''
    # 6
    item = next(postal)
    assert item.zip == '4506051'
    assert item.town == '名駅'
    assert item.town_kana == 'メイエキ'
    assert item.build == 'JRセントラルタワーズ'
    assert item.build_kana == 'ジェイアールセントラルタワーズ'
    assert item.floor == '51'
    # 7
    item = next(postal)
    assert item.zip == '4506290'
    assert item.town == '名駅'
    assert item.town_kana == 'メイエキ'
    assert item.build == 'ミッドランドスクエア'
    assert item.build_kana == 'ミッドランドスクエア'
    assert item.floor == ''
    # 8
    item = next(postal)
    assert item.zip == '4506201'
    assert item.town == '名駅'
    assert item.town_kana == 'メイエキ'
    assert item.build == 'ミッドランドスクエア'
    assert item.build_kana == 'ミッドランドスクエア'
    assert item.floor == '1'





