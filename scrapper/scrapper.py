#!/usr/bin/env python3.4
from bs4 import BeautifulSoup as BS

import aiohttp
import asyncio
import json
import sys

URI = 'http://kalendarz.oiloswiecim.pl/index.php'


def get_data():
    if len(sys.argv) < 3:
        sys.stderr.write('usage: scrapper.py FIRST_ID LAST_ID \n')
        exit(-1)
    start, end = sys.argv[1:3]
    return [
        (yield from get_calendar_data(eid))
        for eid in range(int(start), int(end) + 1)
    ]


@asyncio.coroutine
def get_calendar_data(eid):
    html = yield from get_html(eid)
    data = yield from scrape_html(eid, html)
    return data


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
    html = yield from response.read()
    return html


@asyncio.coroutine
def scrape_html(eid, html):
    soup = BS(html, 'html.parser')
    query = soup.select('.evtForm tr')
    table_data = {
        tds[0][:-1].lower(): tds[1] or None
        for tds in (
            [td.get_text().strip() for td in tr.find_all('td')]
            for tr in query
        )
        if len(tds) > 1
    }

    if table_data.get('tytuł') is None:
        return None

    return {
        'id': str(eid),
        'title': table_data['tytuł'],
        'place': table_data['miejsce'],
        'description': table_data['opis'],
        'add_date': table_data['dodany'],
        'event_date': table_data['data / godzina'],
    } 

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    data = loop.run_until_complete(get_data())
    loop.close()
    json.dump(data, sys.stdout, indent=4)

