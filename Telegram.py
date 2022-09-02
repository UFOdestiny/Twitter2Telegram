#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Name     : pixiv.py
# @Date     : 2022/9/2 10:19
# @Auth     : UFOdestiny
# @Desc     : Telegram

import asyncio

from pyrogram import Client
from pyrogram.errors.exceptions.bad_request_400 import WebpageCurlFailed, ExternalUrlInvalid, MediaEmpty

from config import TelegramAccount
from Logger import Logger
import nest_asyncio

nest_asyncio.apply()


class Telegram(TelegramAccount):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.app = Client("TG", api_id=self.api_id, api_hash=self.api_hash, proxy=self.proxy)
        self.logger = Logger(file_name="telegram", mode="file")

    async def send_one_picture(self, url):
        try:
            await self.app.send_photo("me", url)
        except WebpageCurlFailed:
            self.logger.error(f"{url}")
        except ExternalUrlInvalid:
            self.logger.error(f"{url}")
        except MediaEmpty:
            self.logger.error(f"{url}")

    async def pic_twitter(self, urls):
        task = []
        async with self.app:
            for t in urls:
                t = asyncio.create_task(self.send_one_picture(t))
                task.append(t)
            await asyncio.gather(*task)

    def send_twitter(self, d):
        self.app.run(self.pic_twitter(d))


if __name__ == '__main__':
    tg = Telegram()
    tg.send_twitter(["https://img1.baidu.com/it/u=2499746705,704592304&fm=253&fmt=auto&app=138&f=PNG?w=980&h=500"])
