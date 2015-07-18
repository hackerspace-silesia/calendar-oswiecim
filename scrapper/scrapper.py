#!/usr/bin/env python3.4
import aiohttp
import asyncio

URI = 'http://kalendarz.oiloswiecim.pl/index.php'


def get_data(future):
    return [
        (yield from get_calendar_data(eid))
        for eid 
    ]


@asyncio.coroutine
def get_calendar_data(eid):
    html = yield from get_html(eid)
    data = yield from scrape_html(html)


@asyncio.coroutine
def get_html(eid):
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
    pass

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    data = loop.run_until_complete(get_body('http://python.org'))

