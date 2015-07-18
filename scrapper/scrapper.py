#!/usr/bin/env python3.4
import aiohttp
import asyncio
import json
import sys

URI = 'http://kalendarz.oiloswiecim.pl/index.php'


def get_data():
    return [
        (yield from get_calendar_data(eid))
        for eid in range(1, 501) 
    ]


@asyncio.coroutine
def get_calendar_data(eid):
    html = yield from get_html(eid)
    data = yield from scrape_html(html)
    return data


@asyncio.coroutine
def get_html(eid):
    return "" 
    response = yield from aiohttp.request(
        'GET', URI,
        params={
            'mode': 'edit',
            'xP': '10',
            'eid': str(eid)
        }
    )
    return (yield from response.read())


@asyncio.coroutine
def scrape_html(html):
    return {} 

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    data = loop.run_until_complete(get_data())
    loop.close()
    json.dump(data, sys.stdout, indent=4)

