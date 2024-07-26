import json
import os

from config import BASE_DIR


def get_json_data(path):

    with open(path, 'r', encoding='utf-8') as f:
        test_data = json.load(f)
    return test_data


if __name__ == '__main__':
    data_dir = os.path.join(BASE_DIR, 'testdatas')
    login_data_dir = os.path.join(data_dir, 'send_email_data.json')
    print(get_json_data(login_data_dir))