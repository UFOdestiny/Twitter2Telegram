#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Name     : Logger.py
# @Date     : 2022/9/2 10:45
# @Auth     : UFOdestiny
# @Desc     : logger
import json

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
from config import CacheSetting
from Telegram import Telegram
from Logger import Logger

app = FastAPI(title="Twitter2Telegram", version="1.0", )

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=False, allow_methods=["*"],
                   allow_headers=["*"], )


class Info(BaseModel):
    data: list


class Cache(CacheSetting):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.cache = self.load_json()

    def save_json(self, data=None):
        if not data:
            data = self.cache
        f = open(self.json_name, "w+", encoding="utf-8")
        if type(data) == list:
            data = {"id": data}
        json.dump(data, f)
        f.close()

    def load_json(self):
        f = open(self.json_name, encoding="utf-8")
        data = json.load(f)
        f.close()
        return data["id"]

    def __getitem__(self, item):
        return item in self.cache

    def __setitem__(self, k, v):
        if v:
            self.cache.append(k)


logger = Logger(mode="file")


@app.post("/twitter/write")
async def twitter_write(info: Info):  # form_data通过表单数据来发送信息
    cache = Cache()
    telegram = Telegram()
    data = []
    for i in info.data:
        if not cache[i]:
            data.append(i)
            cache[i] = True
    cache.save_json()

    logger.info(f"接收{len(info.data)}张图片，去重后应更新{len(data)}张图片。")
    # print(len(info.data), len(data))
    # telegram.send_twitter(data)


if __name__ == '__main__':
    uvicorn.run('Twitter:app', host='0.0.0.0', port=8000, reload=True, debug=True, workers=1)
    # tg.send_pixiv({"1": ["https://pbs.twimg.com/media/FZ__GHhUUAAEWMl?format=jpg&name=small"]})
    # tg.send_twitter(["https://pbs.twimg.com/media/FZ__GHhUUAAEWMl?format=jpg&name=small"])
    # Pixiv_Favorite()()
