#!/usr/bin/env python3
# coding: utf-8
__version__ = '0.0.1'

import sys

import requests


def _tabular_to_dataframe(data):
    import pandas
    return pandas.DataFrame(data['rows'], columns=data['keys'])


def download(unikey):
    url = 'https://frozflame.github.io/data/{}.json'.format(unikey)
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp.json()
    return {
        'title': 'Document NOT found', 'type': 'dict',
        'data': {'status_code': resp.status_code, 'unikey': unikey}
    }


def get(unikey, raw=False, quiet=False):
    document = download(unikey)
    if not quiet:
        print(document['title'], file=sys.stderr)
    if not raw and document['type'] == 'tabular':
        return _tabular_to_dataframe(document['data'])
    return document['data']
