// ==UserScript==
// @name         twitter
// @namespace    http://tampermonkey.net/
// @version      0.0.1
// @description  try to take over the world!
// @author       UFOdestiny
// @match        https://twitter.com/UFOdestiny/*
// @match        http://twitter.com/UFOdestiny/*
// @grant    GM_setValue
// @grant    GM_getValue
// @grant    GM_xmlhttpRequest
// @grant    GM_registerMenuCommand
// @grant    GM_unregisterMenuCommand

// ==/UserScript==

(function () {
    "use strict";
    Array.prototype.contains = function (obj) {
        var index = this.length;
        while (index--) {
            if (this[index] === obj) { return true; }
        }
        return false;
    }

    var url = "http://81.70.102.186:8000/twitter/write"
    var all_pic = []
    var button = GM_registerMenuCommand("关闭", click);
    GM_setValue("status", false)



    function click() {
        var status = GM_getValue("status")
        GM_unregisterMenuCommand(button);
        GM_setValue("status", !status)
        if (!status) {
            button = GM_registerMenuCommand("开启", click);
            post()
        }
        else {
            button = GM_registerMenuCommand("关闭", click);
        }
    }


    async function dome(fuc) {
        function delay(num) {
            return new Promise((resolve, reject) => {
                setTimeout(() => {
                    resolve()
                }, num)
            })
        };

        for (let index = 0; index < 1000; index++) {
            let status = GM_getValue("status")
            if (status) {
                fuc()
            }
            await delay(10000)

        }
    }

    function get() {
        let img = Array.from(document.getElementsByTagName("img"))
        var cache = []
        const reg = /(?<=name=).+/
        img.forEach((elem, index) => {
            let src = elem.src
            if (src.includes("media")) {
                src = src.replace(reg, "large")
                cache.push(src)
            }
        });
        let new_pic = []
        cache.forEach((elem, index) => {
            if (!(all_pic.contains(elem))) {
                new_pic.push(elem)
            }
        })

        console.log(new_pic.length)
        if (new_pic.length > 0) {
            let post_json = { "data": new_pic }
            post(post_json)
        }


        all_pic = all_pic.concat(new_pic)


    };




    function post(data) {
        let json = {
            "data": [
                "https://pbs.twimg.com/media/FZ__GHhUUAAEWMl?format=jpg&name=small",
                "https://pbs.twimg.com/media/FZ__GHhUUAAEWMl?format=jpg&name=small"
            ]
        }


        GM_xmlhttpRequest({
            method: "POST",
            url: url,
            data: JSON.stringify(data),
            headers: { "Content-Type": "application/json; charset=utf-8" },
            onload: function (response) {
                console.log("发送成功");
            },
            onerror: function (response) {
                console.log("发送失败");
            }
        });

    }



    dome(get);


})()
