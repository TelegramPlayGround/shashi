#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
#  t.me/ReQuestChat
#  Copyright (C) 2021 The Authors

#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.

#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.

#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.


""" logging things """

import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        logging.StreamHandler()
    ]
)

def LOGGER(name: str) -> logging.Logger:
    """ get a Logger object """
    return logging.getLogger(name)

""" mandatory imports """

import asyncio
from bs4 import BeautifulSoup
from json import dumps
from urllib.parse import urlencode

""" bloated imports """

import aiohttp
import os
from typing import Dict

""" helper function to make an HTTP request """

async def fetch_website(
    input_url: str,
    custom_headers: Dict = None
) -> str:
    # LOGGER(__name__).info(input_url)
    second_response = None
    async with aiohttp.ClientSession() as session:
        try:
            one_response = await session.get(
                input_url,
                headers=custom_headers
            )
            second_response = await one_response.text()
        except:  # noqa: E722
            return False
    # LOGGER(__name__).info(second_response)
    return second_response

""" wrapper for getting the credentials """

def get_config(name: str, d_v=None, should_prompt=False):
    """ accepts one mandatory variable
    and prompts for the value, if not available """
    val = os.environ.get(name, d_v)
    if not val and should_prompt:
        try:
            val = input(f"enter {name}'s value: ")
        except EOFError:
            val = d_v
        print("\n")
    return val

""" fetch posts and returns in the required format """

async def ig(a: str):
    io = "https://t.me/ReQuestChat"
    F = get_config("F", "A B C D E F A B C D E F")
    G = get_config("G", "G")
    H = get_config("H", "H")
    b = await fetch_website(
        a,
        {
            H: G
        }
    )
    LOGGER("io").info(b)
    hp = "html.parser"
    bp1, cp, lp, pi, lta, otb, gmi, ilu, src, lui, pp, cc = F.split(" ")
    s = BeautifulSoup(b, hp)
    d = s.find(lui, class_=bp1)
    e = d.find_all(ilu)
    f = []
    for g in e:
        p = g.find(gmi, class_=pi)
        j = g.find(otb, class_=lp).text.strip()
        k = g.find(otb, class_=cp).text.strip()
        i = p.get(src)
        c = p.get(lta)
        f.append({
            "photo": i,
            "caption": c,
            "reply_markup": dumps({
                "inline_keyboard": [
                    [
                        {
                            "text": f"{j} {pp}",
                            "url": io,
                        },
                        {
                            "text": f"{k} {cc}",
                            "url": io,
                        }
                    ]
                ]
            })
        })
    return f


async def shashi():
    A = get_config("A", "A")
    B = get_config("B", "B")
    C = get_config("C", "C")
    D = get_config("D", "D")
    E = get_config("E", "E")
    a = await ig(A)
    for e in a:
        e["chat_id"] = C
        e["message_thread_id"] = E
        c = f"{D}/bot{B}/sendPhoto?{urlencode(e)}"
        await fetch_website(c)


asyncio.run(shashi())
