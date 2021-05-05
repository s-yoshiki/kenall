from .util import *

def test_chiwari():
    write_item("\r\n".join([
        '03366,"02955","0295513","ｲﾜﾃｹﾝ","ﾜｶﾞｸﾞﾝﾆｼﾜｶﾞﾏﾁ","ｶｯﾁ51ﾁﾜﾘ","岩手県","和賀郡西和賀町","甲子５１地割",0,0,0,1,0,0',
        '03366,"02955","0295523","ｲﾜﾃｹﾝ","ﾜｶﾞｸﾞﾝﾆｼﾜｶﾞﾏﾁ","ｶﾂﾗｺﾞｻﾞﾜ75ﾁﾜﾘ､ｶﾂﾗｺﾞｻﾞﾜ76ﾁﾜﾘ","岩手県","和賀郡西和賀町","桂子沢７５地割、桂子沢７６地割",0,0,0,1,0,0',
        '03366,"02955","0295521","ｲﾜﾃｹﾝ","ﾜｶﾞｸﾞﾝﾆｼﾜｶﾞﾏﾁ","ｺﾂﾅｷﾞｻﾞﾜ54ﾁﾜﾘ-ｺﾂﾅｷﾞｻﾞﾜ56ﾁﾜﾘ","岩手県","和賀郡西和賀町","小繋沢５４地割〜小繋沢５６地割",0,0,0,1,0,0',
        '03366,"02955","0240341","ｲﾜﾃｹﾝ","ﾜｶﾞｸﾞﾝﾆｼﾜｶﾞﾏﾁ","ｽｷﾞﾅﾊﾀ44ﾁﾜﾘ(ﾕﾀﾞﾀﾞﾑｶﾝﾘｼﾞﾑｼｮ､ｳｼﾛｸﾞﾁﾔﾏ､ｱﾃﾗｸ)","岩手県","和賀郡西和賀町","杉名畑４４地割（湯田ダム管理事務所、後口山、当楽）",1,0,0,0,0,0',
        '03507,"02879","0287911","ｲﾜﾃｹﾝ","ｸﾉﾍｸﾞﾝﾋﾛﾉﾁｮｳ","ﾀﾈｲﾁﾀﾞｲ39ﾁﾜﾘ-ﾀﾞｲ45ﾁﾜﾘ(ｶﾄﾞﾉﾊﾏ､ﾃﾞﾝｷﾁ)","岩手県","九戸郡洋野町","種市第３９地割〜第４５地割（角浜、伝吉）",0,1,0,0,0,0',
    ]))
    postal = generate_parser()
    # 1
    item = next(postal)
    assert item.town == '甲子'
    assert item.town_kana == 'カッチ'
    assert item.has_subtown
    assert item.subtown[0] == '第51地割'
    assert item.subtown_kana[0] == 'ダイ51チワリ'
    # 2
    item = next(postal)
    assert item.town == '桂子沢'
    assert item.town_kana == 'カツラゴザワ'
    assert item.has_subtown
    assert item.subtown[0] == '第75地割'
    assert item.subtown_kana[0] == 'ダイ75チワリ'
    assert item.subtown[1] == '第76地割'
    assert item.subtown_kana[1] == 'ダイ76チワリ'
    # 3
    item = next(postal)
    assert item.town == '小繋沢'
    assert item.town_kana == 'コツナギザワ'
    assert item.has_subtown
    assert item.subtown[0] == '第54地割〜第56地割'
    assert item.subtown_kana[0] == 'ダイ54チワリ-ダイ56チワリ'
    # 4
    item = next(postal)
    assert item.town == '杉名畑'
    assert item.town_kana == 'スギナハタ'
    assert item.has_subtown
    assert item.subtown[0] == '第44地割 湯田ダム管理事務所'
    assert item.subtown_kana[0] == 'ダイ44チワリ ユダダムカンリジムショ'
    assert item.subtown[1] == '第44地割 後口山'
    assert item.subtown_kana[1] == 'ダイ44チワリ ウシログチヤマ'
    assert item.subtown[2] == '第44地割 当楽'
    assert item.subtown_kana[2] == 'ダイ44チワリ アテラク'
    # 5
    item = next(postal)
    assert item.town == '種市'
    assert item.town_kana == 'タネイチ'
    assert item.has_subtown
    assert item.subtown[0] == '第39地割〜第45地割 角浜'
    assert item.subtown_kana[0] == 'ダイ39チワリ-ダイ45チワリ カドノハマ'
    assert item.subtown[1] == '第39地割〜第45地割 伝吉'
    assert item.subtown_kana[1] == 'ダイ39チワリ-ダイ45チワリ デンキチ'

