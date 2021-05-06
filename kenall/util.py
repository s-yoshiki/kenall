

def str_zen2han(arg: str) -> str:
    ZEN2HAN = str.maketrans("０１２３４５６７８９", "0123456789")
    return arg.translate(ZEN2HAN)

# todo:
# def remove_empty_str(arg: list) -> list:
#     return list(filter(None, arg))
