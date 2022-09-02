# -*- coding: utf-8 -*-
# @Name     : test.py
# @Date     : 2022/9/2 14:41
# @Auth     : Yu Dahai
# @Email    : yudahai@pku.edu.cn
# @Desc     :

import json


def save_json(data, file_name="cache.json"):
    f = open(file_name, "a+", encoding="utf-8")
    if type(data) == list:
        data = {"id": data}
    json.dump(data, f)
    f.close()


def load_json(file_name="cache.json"):
    f = open(file_name, encoding="utf-8")
    data = json.load(f)
    f.close()
    return data["id"]


if __name__ == '__main__':
    a = load_json()
    save_json([1, 23, 4])
