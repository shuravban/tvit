#!/usr/bin/python3

# standard modules
import sys
import os
import time

# logging
import logging as L
L.basicConfig(
    format='%(levelname)s: %(message)s')
# TODO
if os.environ.get('DEBUG', False):
    L.getLogger().setLevel(L.INFO)

# TwitterAPI
sys.path.insert(0, '../TwitterAPI')
import TwitterAPI as T

# my modules
import keys
import error

def timed_query(api, query, params, times=0):
    rst = None
    for i in range(times):
        try:
            rst = api.request(query, params)
            return rst
        except T.TwitterConnectionError:
            t = 2**i
            L.info('Sleeping ' + str(t) + ' seconds')
            time.sleep(t)
    # here only if unsuccess
    raise error.TConnectionError(
        'Unsuccess in `timed_query` after ' + str(i) + ' attempts')

if __name__ == '__main__':
    # just some testing code TODO remove
    q = 'account/verify_credentials'
    p = {}
    api = T.TwitterAPI(*keys.keys())

    r = timed_query(api, q, p, 3)

    import pprint
    pprint.pprint(r.json())
