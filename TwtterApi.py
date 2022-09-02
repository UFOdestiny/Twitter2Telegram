#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Name     : TwitterApi.py
# @Date     : 2022/9/2 16:54
# @Auth     : UFOdestiny
# @Desc     : TwitterApi


import json

import tweepy
from config import TwitterAccount
from Telegram import Telegram
from Logger import Logger


class TwitterApi(TwitterAccount):
    def __init__(self):

        self.client = tweepy.Client(self.bearer_token)
        self.images = None
        self.cache = self.load_json()
        self.new = None
        self.logger = Logger(mode="file")

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

    def get_likes(self, max_results=100):
        response = self.client.get_liked_tweets(
            self.user_id,
            max_results=max_results,
            # tweet_fields=["text"],
            media_fields=['type', 'url'],
            expansions="attachments.media_keys")

        media = response.includes["media"]

        self.images = [img.url for img in media if img.type == "photo"]

        # print(response.includes)
        # print(self.images)

    def check_update(self):
        self.new = [i for i in self.images if i not in self.cache]
        self.save_json(self.new + self.cache)

    def send(self, send=True):
        if self.new:
            if send:
                self.logger.info(f"正在更新{len(self.new)}张收藏到telegram")
                telegram = Telegram()
                telegram.send_twitter(self.new)
                self.logger.info(f"更新完毕")
        else:
            self.logger.info("收藏没更新")

    def run(self, likes=100, send=False):
        self.get_likes(likes)
        self.check_update()
        self.send(send)


if __name__ == '__main__':
    t = TwitterApi()
    t.run(likes=100, send=False)
