from .util import *

def test_other():
    write_item(
        '23105,"450  ","4500002","ｱｲﾁｹﾝ","ﾅｺﾞﾔｼﾅｶﾑﾗｸ","ﾒｲｴｷ(ｿﾉﾀ)","愛知県","名古屋市中村区","名駅（その他）",1,0,1,0,0,0'
    )
    postal = generate_parser()
    item = next(postal)
    assert item.town == '名駅'
    assert item.town_kana == 'メイエキ'
