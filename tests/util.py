import os
import kenall

def get_csv_path():
    return os.getcwd() + "/tests/tmp/test.csv"

# @pytest.fixture
def write_item(value):
    file = open(get_csv_path(), 'w')
    file.write(value)
    file.close()

def generate_parser():
    return kenall.Parser(
        path=get_csv_path(),
        encoding='utf-8',
        alnum_z2h=True,
        katakana_h2z=True,
    )