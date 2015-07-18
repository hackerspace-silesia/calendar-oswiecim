#!/usr/bin/env python3.4
from bs4 import BeautifulSoup as BS

import aiohttp
import asyncio
import json
import sys

URI = 'http://kalendarz.oiloswiecim.pl/index.php'


@asyncio.coroutine
def get_data(start, end):
    data = []
    couroutines = [
        set_calendar_data(data, eid)
        for eid in range(start, end)
    ]
    yield from asyncio.wait(couroutines)
    return data


@asyncio.coroutine
def set_calendar_data(data_list, eid):
    html = yield from get_html(eid)
    data = yield from scrape_html(eid, html)
    if data is not None:
        data_list.append(data)


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
    if len(sys.argv) < 3:
        sys.stderr.write('usage: scrapper.py FIRST_ID LAST_ID\n')
        exit(-1)
    start, end = sys.argv[1:3]
    loop = asyncio.get_event_loop()
    gen = get_data(int(start), int(end) + 1)
    data = loop.run_until_complete(gen)
    loop.close()
    json.dump(data, sys.stdout, indent=4)

