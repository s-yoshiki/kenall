
# kenall (KEN_ALL.csv Parser for 日本郵政)

[![unit-test-ci](https://github.com/s-yoshiki/kenall/workflows/unit-test-ci/badge.svg)](https://github.com/s-yoshiki/kenall)

[![codecov](https://codecov.io/gh/s-yoshiki/kenall/branch/main/graph/badge.svg)](https://codecov.io/gh/s-yoshiki/kenall)

## Description

日本郵政が提供している郵便番号ファイル(通称: KEN_ALL.csv)をパースするPython用パッケージです。

**特徴**

 - 複数行に分割された行をマージします
 - 不要な情報を除去します
 - 地域名の中の市町村名やビル名などの詳細情報を抽出します
 - 半角カナを全角カナに変換します
 - 全角数字を半角数字に変換します

## Installation

```shell
$ pip install kenall
```

## Usage

```py
import kenall

# Iterator objects
postal = kenall.Parser(path="./KEN_ALL.csv")

for item in postal:
    print(item.pref)          # 県名
    print(item.pref_kana)     # 県名カナ
    print(item.region)        # 市区町村名
    print(item.region_kana)   # 市区町村名カナ
    print(item.district)      # 郡名
    print(item.district_kana) # 郡名カナ
    print(item.city)          # 市名
    print(item.city_kana)     # 市名カナ
    print(item.ward)          # 区名
    print(item.ward_kana)     # 区名カナ
    print(item.town)          # 町域名
    print(item.town_kana)     # 町域名カナ
    print(item.buiild)        # ビル名
    print(item.buiild_kana)   # ビル名カナ
    print(item.floor)         # ビル階層
    print(item.dict)          # dictionary形式で取得
```

## Interface

## Link

 - [郵便番号データダウンロード - 日本郵便](https://www.post.japanpost.jp/zipcode/download.html)

## Acknowledgements

 - [日本郵便](https://www.post.japanpost.jp/)
 - [yappo](https://github.com/yappo)
    - [Parse::JapanesePostalCode](https://github.com/yappo/p5-Parse-JapanesePostalCode)
 - [inouet](https://github.com/inouet)
    - [ken-all](https://github.com/inouet/ken-all)

## License

[MIT](./LICENSE)

このソースコードの使用にて生じた故障又は損害などに関しては一切の責任を負いかねます。