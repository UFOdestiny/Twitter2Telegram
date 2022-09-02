#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Name     : config.py
# @Date     : 2022/9/2 13:26
# @Auth     : UFOdestiny
# @Desc     : config

import platform


class TelegramAccount:
    api_id = 123
    api_hash = 'abc'

    plat = platform.system().lower()
    if plat == 'windows':
        proxy = dict(scheme="http", hostname="127.0.0.1", port=7890)
    elif plat == 'linux':
        proxy = dict(hostname="127.0.0.1", port=7891)


class LogSetting:
    path = "log"


class CacheSetting:
    json_name = "cache.json"


if __name__ == "__main__":
    print(TelegramAccount.proxy)
