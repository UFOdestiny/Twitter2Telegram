#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Name     : config.py
# @Date     : 2022/9/2 13:26
# @Auth     : UFOdestiny
# @Desc     : config

import os
import platform


class TelegramAccount:
    api_id = 1
    api_hash = 'dc3'

    plat = platform.system().lower()
    if plat == 'windows':
        proxy = dict(scheme="http", hostname="127.0.0.1", port=7890)
    elif plat == 'linux':
        proxy = dict(hostname="127.0.0.1", port=7891)


class LogSetting:
    path = "log"


class TwitterAccount:
    bearer_token = ""
    user_id = 3
    json_name = "cache.json"

    plat = platform.system().lower()
    if plat == 'windows':
        os.environ['http_proxy'] = 'http://127.0.0.1:7890'
        os.environ['https_proxy'] = 'http://127.0.0.1:7890'
    elif plat == 'linux':
        os.environ['http_proxy'] = 'http://127.0.0.1:7891'
        os.environ['https_proxy'] = 'http://127.0.0.1:7891'


if __name__ == "__main__":
    print(TelegramAccount.proxy)
